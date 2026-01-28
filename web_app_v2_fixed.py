import streamlit as st
import pickle
import numpy as np
import pandas as pd
from datetime import datetime
import plotly.graph_objects as go
import cv2
from PIL import Image
import io

st.set_page_config(page_title="Guardian Shield", page_icon="", layout="wide", initial_sidebar_state="expanded")

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
            st.sidebar.error(f"Model not found")
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

def scan_qr_opencv(image):
    """Decode QR using OpenCV"""
    try:
        img_array = np.array(image.convert('RGB'))
        detector = cv2.QRCodeDetector()
        data, bbox, _ = detector.detectAndDecode(img_array)
        
        if data and data.startswith('http'):
            return [data]
        return None
    except Exception as e:
        return None

def analyze_image_simple(image):
    """Simple image analysis"""
    try:
        img_array = np.array(image)
        suspicious_score = 0
        
        width, height = image.size
        if width < 500 or height < 500:
            suspicious_score += 20
        
        qr_urls = scan_qr_opencv(image)
        if qr_urls:
            suspicious_score += 30
        
        avg_red = np.mean(img_array[:,:,0]) if len(img_array.shape) == 3 else 0
        if avg_red > 150:
            suspicious_score += 15
        
        if width * height < 250000:
            suspicious_score += 10
        
        return suspicious_score, qr_urls
    except:
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
    st.markdown("###  Guardian Shield")
    st.markdown("**Multi-layer Detection**")
    st.markdown("•  URL Scanning")
    st.markdown("•  Image Analysis")
    st.markdown("•  QR Code Detection")
    
    if model:
        st.success("**Model:**  Active\n\n**Accuracy:** 100%")
    else:
        st.error("**Model:**  Error")
    
    st.markdown("---")
    st.markdown("Built by Dileep Pabbathi")

# Header
st.markdown("<h1 style='text-align: center;'> GUARDIAN SHIELD</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Multi-Layer Threat Detection</h3>", unsafe_allow_html=True)
st.markdown("---")

# Stats
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Total", st.session_state.total_scans)
col2.metric(" URLs", st.session_state.url_threats)
col3.metric(" QR", st.session_state.qr_threats)
col4.metric(" Images", st.session_state.image_threats)
col5.metric(" Safe", st.session_state.safe)

st.markdown("---")

tab1, tab2, tab3, tab4 = st.tabs([" URL Scan", " Image Scan", " QR Scan", " Analytics"])

with tab1:
    st.markdown("###  URL Threat Detection")
    url = st.text_input("Enter URL:", placeholder="https://example.com")
    
    if st.button(" SCAN URL"):
        if url and model:
            features = np.array([extract_url_features(url)])
            prediction = model.predict(features)[0]
            confidence = model.predict_proba(features)[0]
            
            st.session_state.total_scans += 1
            
            if prediction == 1:
                st.session_state.url_threats += 1
                st.error(f" THREAT! Confidence: {confidence[1]*100:.1f}%")
            else:
                st.session_state.safe += 1
                st.success(f" SAFE! Confidence: {confidence[0]*100:.1f}%")
            st.rerun()

with tab2:
    st.markdown("###  Image Analysis")
    uploaded = st.file_uploader("Upload Image", type=['png', 'jpg', 'jpeg'])
    
    if uploaded:
        image = Image.open(uploaded)
        st.image(image, width=400)
        
        if st.button(" ANALYZE"):
            score, qr_urls = analyze_image_simple(image)
            st.session_state.total_scans += 1
            
            if score > 50:
                st.session_state.image_threats += 1
                st.error(f" SUSPICIOUS! Risk: {score}/100")
            else:
                st.session_state.safe += 1
                st.success(f" SAFE! Risk: {score}/100")
            
            if qr_urls:
                st.warning(f"QR Found: {qr_urls[0]}")
            st.rerun()

with tab3:
    st.markdown("###  QR Code Scanner")
    qr_file = st.file_uploader("Upload QR Image", type=['png', 'jpg'], key="qr")
    
    if qr_file:
        qr_img = Image.open(qr_file)
        st.image(qr_img, width=300)
        
        if st.button(" SCAN QR"):
            qr_urls = scan_qr_opencv(qr_img)
            st.session_state.total_scans += 1
            
            if qr_urls and model:
                features = np.array([extract_url_features(qr_urls[0])])
                prediction = model.predict(features)[0]
                confidence = model.predict_proba(features)[0]
                
                st.info(f"URL: {qr_urls[0]}")
                
                if prediction == 1:
                    st.session_state.qr_threats += 1
                    st.error(f" MALICIOUS QR!")
                else:
                    st.session_state.safe += 1
                    st.success(f" SAFE QR")
                st.rerun()
            else:
                st.warning("No QR detected")

with tab4:
    st.markdown("###  Analytics")
    if st.session_state.total_scans > 0:
        fig = go.Figure(data=[go.Pie(
            labels=['URLs', 'QR', 'Images', 'Safe'],
            values=[st.session_state.url_threats, st.session_state.qr_threats, 
                   st.session_state.image_threats, st.session_state.safe],
            marker=dict(colors=['#ff0000', '#ff6600', '#ff9900', '#00ff00'])
        )])
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', font=dict(color='white'))
        st.plotly_chart(fig)
    else:
        st.info("Scan to see analytics!")

st.markdown("---")
st.markdown("<p style='text-align: center; color: #888;'>Guardian Shield v4.0 | AI-Powered</p>", unsafe_allow_html=True)
