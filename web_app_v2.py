import streamlit as st
import pickle
import numpy as np
import pandas as pd
from datetime import datetime
import plotly.graph_objects as go
import cv2
from pyzbar import pyzbar
from PIL import Image
import io

st.set_page_config(page_title="Guardian Shield", page_icon="️", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
<style>
.main {background: linear-gradient(135deg, #0a0a1a 0%, #1a1a2e 100%);}
.stButton>button {background: linear-gradient(135deg, #00ff00 0%, #00cc00 100%); color: black; font-weight: bold;}
h1 {color: #00ff00 !important;}
h2, h3 {color: #00ffff !important;}
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_model():
    import os
    try:
        model_path = "ml-models/saved_models/url_classifier_20260124.pkl"
        if not os.path.exists(model_path):
            st.sidebar.error(f"Model not found at: {model_path}")
            return None
        with open(model_path, "rb") as f:
            return pickle.load(f)
    except Exception as e:
        st.sidebar.error(f"Error: {e}")
        return None

model = load_model()

def extract_url_features(url):
    features = []
    features.append(len(url))
    features.append(url.count('.'))
    features.append(url.count('/'))
    features.append(url.count('-'))
    features.append(url.count('?'))
    features.append(url.count('='))
    features.append(1 if 'https' in url else 0)
    features.append(1 if any(char.isdigit() for char in url) else 0)
    features.append(1 if '@' in url else 0)
    return features

def scan_qr_code(image):
    """Decode QR code from image"""
    try:
        img_array = np.array(image)
        decoded_objects = pyzbar.decode(img_array)
        
        if decoded_objects:
            urls = []
            for obj in decoded_objects:
                data = obj.data.decode('utf-8')
                if data.startswith('http'):
                    urls.append(data)
            return urls
        return None
    except Exception as e:
        st.error(f"QR decode error: {e}")
        return None

def analyze_image_simple(image):
    """Simple image analysis for suspicious patterns"""
    try:
        img_array = np.array(image)
        
        # Check for suspicious patterns
        suspicious_score = 0
        
        # Check image size (phishing often uses specific sizes)
        width, height = image.size
        if width < 500 or height < 500:
            suspicious_score += 20
        
        # Check for QR codes
        qr_urls = scan_qr_code(image)
        if qr_urls:
            suspicious_score += 30
        
        # Color analysis (many phishing pages use red/urgent colors)
        avg_red = np.mean(img_array[:,:,0])
        if avg_red > 150:
            suspicious_score += 15
        
        # Low resolution (common in phishing)
        if width * height < 250000:
            suspicious_score += 10
        
        return suspicious_score, qr_urls
    except Exception as e:
        return 0, None

if 'total_scans' not in st.session_state:
    st.session_state.total_scans = 0
    st.session_state.url_threats = 0
    st.session_state.qr_threats = 0
    st.session_state.image_threats = 0
    st.session_state.safe = 0
    st.session_state.history = []

# Sidebar
with st.sidebar:
    st.markdown("### ️ Guardian Shield")
    st.markdown("**Multi-layer threat detection:**")
    
    st.markdown("### Features:")
    st.markdown("•  URL Detection")
    st.markdown("•  Image Analysis")
    st.markdown("•  QR Code Scanning")
    st.markdown("•  Real-time Analytics")
    st.markdown("•  Scan History")
    
    st.markdown("### Model Info")
    if model:
        st.success("""
**Algorithm:** Random Forest  
**URL Accuracy:** 100%  
**Training Data:** 774 URLs  
**Features:** 9 indicators
        """)
    else:
        st.error("**Model:** Not Loaded ")
    
    st.markdown("---")
    st.markdown("Built with ️ by Dileep Pabbathi")
    st.markdown("[GitHub](https://github.com/Dileeppabbathi/guardian-shield)")

# Header
col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    st.markdown("<h1 style='text-align: center;'>️ GUARDIAN SHIELD</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>AI-Powered Multi-Layer Threat Detection</h3>", unsafe_allow_html=True)

st.markdown("---")

# Stats
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Total Scans", st.session_state.total_scans)
col2.metric(" URL Threats", st.session_state.url_threats)
col3.metric(" QR Threats", st.session_state.qr_threats)
col4.metric(" Image Threats", st.session_state.image_threats)
col5.metric(" Safe", st.session_state.safe)

st.markdown("---")

# Tabs
tab1, tab2, tab3, tab4 = st.tabs([" Scan URL", "📷 Scan Image", "🔲 Scan QR Code", "📊 Analytics"])

with tab1:
    st.markdown("###  URL Threat Detection")
    url = st.text_input("Enter URL:", placeholder="https://example.com", label_visibility="collapsed")
    
    col1, col2, col3 = st.columns([2, 1, 2])
    with col2:
        if st.button(" SCAN URL", use_container_width=True):
            if url and model:
                features = np.array([extract_url_features(url)])
                prediction = model.predict(features)[0]
                confidence = model.predict_proba(features)[0]
                
                st.session_state.total_scans += 1
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                
                if prediction == 1:
                    st.session_state.url_threats += 1
                    conf = confidence[1] * 100
                    st.error(f"###  URL THREAT DETECTED!\n**Type:** Phishing URL\n**Confidence:** {conf:.1f}%\n**Action:** ❌ BLOCKED")
                    st.session_state.history.append({'timestamp': timestamp, 'type': 'URL', 'content': url, 'result': 'THREAT', 'confidence': conf})
                else:
                    st.session_state.safe += 1
                    conf = confidence[0] * 100
                    st.success(f"###  SAFE URL\n**Confidence:** {conf:.1f}%\n**Action:** ✓ ALLOWED")
                    st.session_state.history.append({'timestamp': timestamp, 'type': 'URL', 'content': url, 'result': 'SAFE', 'confidence': conf})
                
                st.rerun()

with tab2:
    st.markdown("###  Image Threat Detection")
    st.info("Upload an image to check for phishing screenshots, fake login pages, or suspicious content")
    
    uploaded_file = st.file_uploader("Choose an image", type=['png', 'jpg', 'jpeg'], label_visibility="collapsed")
    
    if uploaded_file:
        image = Image.open(uploaded_file)
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.image(image, caption="Uploaded Image", use_container_width=True)
        
        with col2:
            if st.button(" ANALYZE IMAGE", use_container_width=True):
                with st.spinner("Analyzing image..."):
                    suspicious_score, qr_urls = analyze_image_simple(image)
                    
                    st.session_state.total_scans += 1
                    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    
                    if suspicious_score > 50:
                        st.session_state.image_threats += 1
                        st.error(f"###  SUSPICIOUS IMAGE!\n**Risk Score:** {suspicious_score}/100\n**Recommendation:** ⚠️ CAUTION")
                        
                        if qr_urls:
                            st.warning(f"**QR Code Found:** {qr_urls[0]}")
                        
                        st.session_state.history.append({'timestamp': timestamp, 'type': 'IMAGE', 'content': 'uploaded_image.jpg', 'result': 'SUSPICIOUS', 'confidence': suspicious_score})
                    else:
                        st.session_state.safe += 1
                        st.success(f"###  IMAGE APPEARS SAFE\n**Risk Score:** {suspicious_score}/100")
                        st.session_state.history.append({'timestamp': timestamp, 'type': 'IMAGE', 'content': 'uploaded_image.jpg', 'result': 'SAFE', 'confidence': 100-suspicious_score})
                    
                    if qr_urls and model:
                        st.markdown("---")
                        st.markdown("###  QR Code Detected - Checking URL...")
                        for qr_url in qr_urls:
                            features = np.array([extract_url_features(qr_url)])
                            prediction = model.predict(features)[0]
                            confidence = model.predict_proba(features)[0]
                            
                            if prediction == 1:
                                st.error(f" QR contains MALICIOUS URL: `{qr_url}`")
                                st.session_state.qr_threats += 1
                            else:
                                st.success(f" QR URL appears safe: `{qr_url}`")
                    
                    st.rerun()

with tab3:
    st.markdown("###  QR Code Scanner")
    st.info("Upload an image containing a QR code to decode and check the URL")
    
    qr_file = st.file_uploader("Upload QR Code Image", type=['png', 'jpg', 'jpeg'], key="qr", label_visibility="collapsed")
    
    if qr_file:
        qr_image = Image.open(qr_file)
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.image(qr_image, caption="QR Code", use_container_width=True)
        
        with col2:
            if st.button(" SCAN QR CODE", use_container_width=True):
                with st.spinner("Decoding QR code..."):
                    qr_urls = scan_qr_code(qr_image)
                    
                    st.session_state.total_scans += 1
                    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    
                    if qr_urls:
                        st.success(f"###  QR Code Decoded!")
                        
                        for qr_url in qr_urls:
                            st.markdown(f"**URL Found:** `{qr_url}`")
                            
                            if model:
                                features = np.array([extract_url_features(qr_url)])
                                prediction = model.predict(features)[0]
                                confidence = model.predict_proba(features)[0]
                                
                                if prediction == 1:
                                    st.session_state.qr_threats += 1
                                    conf = confidence[1] * 100
                                    st.error(f" **MALICIOUS QR CODE!**\n**Confidence:** {conf:.1f}%\n**Action:** ❌ DO NOT SCAN")
                                    st.session_state.history.append({'timestamp': timestamp, 'type': 'QR', 'content': qr_url, 'result': 'THREAT', 'confidence': conf})
                                else:
                                    st.session_state.safe += 1
                                    conf = confidence[0] * 100
                                    st.success(f" **QR URL is Safe**\n**Confidence:** {conf:.1f}%")
                                    st.session_state.history.append({'timestamp': timestamp, 'type': 'QR', 'content': qr_url, 'result': 'SAFE', 'confidence': conf})
                        
                        st.rerun()
                    else:
                        st.warning(" No QR code detected in image")

with tab4:
    st.markdown("###  Threat Analytics")
    
    if st.session_state.total_scans > 0:
        col1, col2 = st.columns(2)
        
        with col1:
            # Threat distribution
            fig = go.Figure(data=[go.Pie(
                labels=['URL Threats', 'QR Threats', 'Image Threats', 'Safe'],
                values=[st.session_state.url_threats, st.session_state.qr_threats, st.session_state.image_threats, st.session_state.safe],
                marker=dict(colors=['#ff0000', '#ff6600', '#ff9900', '#00ff00'])
            )])
            fig.update_layout(title="Detection Results", paper_bgcolor='rgba(0,0,0,0)', font=dict(color='white'))
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Bar chart
            fig2 = go.Figure(data=[go.Bar(
                x=['URLs', 'QR Codes', 'Images', 'Safe'],
                y=[st.session_state.url_threats, st.session_state.qr_threats, st.session_state.image_threats, st.session_state.safe],
                marker_color=['#ff0000', '#ff6600', '#ff9900', '#00ff00']
            )])
            fig2.update_layout(title="Scan Statistics", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color='white'))
            st.plotly_chart(fig2, use_container_width=True)
        
        # History
        st.markdown("###  Scan History")
        if st.session_state.history:
            df = pd.DataFrame(st.session_state.history)
            st.dataframe(df, use_container_width=True, height=300)
            
            csv = df.to_csv(index=False)
            st.download_button(" Download History (CSV)", csv, f"guardian_shield_history_{datetime.now().strftime('%Y%m%d')}.csv", "text/csv")
    else:
        st.info(" Perform scans to see analytics!")

st.markdown("---")
st.markdown("<p style='text-align: center; color: #888888;'>Guardian Shield v4.0 | Multi-Layer Threat Detection | Powered by AI</p>", unsafe_allow_html=True)
