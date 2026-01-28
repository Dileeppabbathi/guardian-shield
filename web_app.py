"""
Guardian Shield - Web Application
Deploy your ML model as a web app!
"""

import streamlit as st
import pickle
import numpy as np
import pandas as pd
from datetime import datetime
import plotly.graph_objects as go
import plotly.express as px

# Page config
st.set_page_config(
    page_title="Guardian Shield - URL Threat Detector",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #0a0a1a 0%, #1a1a2e 89.59%);
    }
    .stButton>button {
        background: linear-gradient(135deg, #00ff00 0%, #00cc00 89.59%);
        color: black;
        font-weight: bold;
        border-radius: 10px;
        padding: 15px 30px;
        font-size: 18px;
    }
    h1 {
        color: #00ff00 !important;
        text-shadow: 0 0 20px rgba(0, 255, 0, 0.5);
    }
    h2, h3 {
        color: #00ffff !important;
    }
    </style>
""", unsafe_allow_html=True)

# Load ML Model
@st.cache_resource
@st.cache_resource
def load_model():
    import os
    try:
        model_path = "ml-models/saved_models/url_classifier.pkl"
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
    """Extract features from URL"""
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

# Initialize session state
if 'scan_history' not in st.session_state:
    st.session_state.scan_history = []
if 'total_scans' not in st.session_state:
    st.session_state.total_scans = 0
if 'threats_detected' not in st.session_state:
    st.session_state.threats_detected = 0
if 'safe_urls' not in st.session_state:
    st.session_state.safe_urls = 0

# Header
col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    st.markdown("<h1 style='text-align: center;'> GUARDIAN SHIELD</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>AI-Powered URL Threat Detection</h3>", unsafe_allow_html=True)

st.markdown("---")

# Stats Dashboard
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Scans", st.session_state.total_scans, delta=None)
with col2:
    st.metric(" Threats Detected", st.session_state.threats_detected, delta=None)
with col3:
    st.metric(" Safe URLs", st.session_state.safe_urls, delta=None)

st.markdown("---")

# Main content
tab1, tab2, tab3 = st.tabs([" Scan URL", " Analytics", " History"])

with tab1:
    st.markdown("### Enter URL to Scan")
    
    url_input = st.text_input("URL", placeholder="https://example.com", label_visibility="collapsed")
    
    col1, col2, col3 = st.columns([2, 1, 2])
    with col2:
        scan_button = st.button(" SCAN NOW", use_container_width=True)
    
    if scan_button and url_input:
        if model is None:
            st.error("Model not loaded!")
        else:
            with st.spinner("Scanning URL..."):
                # Extract features
                features = np.array([extract_url_features(url_input)])
                prediction = model.predict(features)[0]
                confidence = model.predict_proba(features)[0]
                
                # Update stats
                st.session_state.total_scans += 1
                
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                
                if prediction == 1:
                    # THREAT
                    st.session_state.threats_detected += 1
                    conf = confidence[1] * 100
                    
                    st.error(f"###  THREAT DETECTED!")
                    st.markdown(f"""
                    **URL:** `{url_input}`  
                    **Classification:** PHISHING  
                    **Confidence:** {conf:.1f}%  
                    **Risk Level:** HIGH  
                    **Action:**  BLOCKED
                    """)
                    
                    st.session_state.scan_history.append({
                        'timestamp': timestamp,
                        'url': url_input,
                        'classification': 'PHISHING',
                        'confidence': conf,
                        'result': 'threat'
                    })
                else:
                    # SAFE
                    st.session_state.safe_urls += 1
                    conf = confidence[0] * 100
                    
                    st.success(f"###  SAFE URL")
                    st.markdown(f"""
                    **URL:** `{url_input}`  
                    **Classification:** LEGITIMATE  
                    **Confidence:** {conf:.1f}%  
                    **Risk Level:** LOW  
                    **Action:**  ALLOWED
                    """)
                    
                    st.session_state.scan_history.append({
                        'timestamp': timestamp,
                        'url': url_input,
                        'classification': 'LEGITIMATE',
                        'confidence': conf,
                        'result': 'safe'
                    })
                
                st.rerun()

with tab2:
    st.markdown("###  Real-Time Analytics")
    
    if st.session_state.total_scans > 0:
        col1, col2 = st.columns(2)
        
        with col1:
            # Pie chart
            fig_pie = go.Figure(data=[go.Pie(
                labels=['Safe URLs', 'Threats'],
                values=[st.session_state.safe_urls, st.session_state.threats_detected],
                marker=dict(colors=['#00ff00', '#ff0000']),
                hole=.3
            )])
            fig_pie.update_layout(
                title="Threat Distribution",
                height=400,
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font=dict(color='white')
            )
            st.plotly_chart(fig_pie, use_container_width=True)
        
        with col2:
            # Bar chart
            fig_bar = go.Figure(data=[
                go.Bar(name='Count', 
                       x=['Total Scans', 'Threats', 'Safe'],
                       y=[st.session_state.total_scans, 
                          st.session_state.threats_detected, 
                          st.session_state.safe_urls],
                       marker_color=['#00ffff', '#ff0000', '#00ff00'])
            ])
            fig_bar.update_layout(
                title="Scan Statistics",
                height=400,
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font=dict(color='white')
            )
            st.plotly_chart(fig_bar, use_container_width=True)
    else:
        st.info(" Scan some URLs to see analytics!")

with tab3:
    st.markdown("###  Scan History")
    
    if st.session_state.scan_history:
        # Convert to dataframe
        df = pd.DataFrame(st.session_state.scan_history)
        
        # Display table
        st.dataframe(df, use_container_width=True, height=400)
        
        # Download button
        csv = df.to_csv(index=False)
        st.download_button(
            label=" Download History (CSV)",
            data=csv,
            file_name=f"guardian_shield_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            mime="text/csv"
        )
    else:
        st.info(" No scan history yet. Start scanning URLs!")

# Sidebar
with st.sidebar:
    st.markdown("### About Guardian Shield")
    st.info("""
     **Guardian Shield** uses advanced machine learning to detect phishing URLs in real-time.
    
    **Features:**
    - 89.59% ML accuracy
    - Real-time detection
    - Visual analytics
    - Scan history
    - CSV export
    """)
    
    st.markdown("### Model Info")
    st.success("""
    **Algorithm:** Random Forest  
    **Accuracy:** 89.59%  
    **Training Data:** 651,199 URLs  
    **Features:** 9 URL indicators
    """)
    
    st.markdown("---")
    st.markdown("Built by Dileep Pabbathi")
    st.markdown("[GitHub](https://github.com/Dileeppabbathi/guardian-shield)")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: #888888;'>Guardian Shield v3.0 | Powered by Machine Learning</p>", unsafe_allow_html=True)
