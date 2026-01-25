import streamlit as st
import pickle
import numpy as np
import pandas as pd
from datetime import datetime
import plotly.graph_objects as go

st.set_page_config(page_title="Guardian Shield", page_icon="🛡️", layout="wide")

@st.cache_resource
def load_model():
    try:
        with open('ml-models/saved_models/url_classifier_20260124.pkl', 'rb') as f:
            return pickle.load(f)
    except:
        st.error("Model not found!")
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

if 'total_scans' not in st.session_state:
    st.session_state.total_scans = 0
    st.session_state.threats = 0
    st.session_state.safe = 0
    st.session_state.history = []

st.title("🛡️ GUARDIAN SHIELD")
st.subheader("AI-Powered URL Threat Detection")

col1, col2, col3 = st.columns(3)
col1.metric("Total Scans", st.session_state.total_scans)
col2.metric("🚨 Threats", st.session_state.threats)
col3.metric("✅ Safe", st.session_state.safe)

st.markdown("---")

url = st.text_input("Enter URL to scan:", placeholder="https://example.com")

if st.button("⚡ SCAN NOW"):
    if url and model:
        features = np.array([extract_url_features(url)])
        prediction = model.predict(features)[0]
        confidence = model.predict_proba(features)[0]
        
        st.session_state.total_scans += 1
        
        if prediction == 1:
            st.session_state.threats += 1
            st.error(f"🚨 THREAT DETECTED! Confidence: {confidence[1]*100:.1f}%")
        else:
            st.session_state.safe += 1
            st.success(f"✅ SAFE URL! Confidence: {confidence[0]*100:.1f}%")
        
        st.rerun()
