"""Test the trained model"""
import pickle
import numpy as np

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

# Load model
with open('saved_models/url_classifier_20260124.pkl', 'rb') as f:
    model = pickle.load(f)

print("🤖 Guardian Shield URL Tester")
print("Enter URLs to test (or 'quit' to exit)\n")

while True:
    url = input("URL: ")
    if url.lower() == 'quit':
        break
    
    features = np.array([extract_url_features(url)])
    prediction = model.predict(features)[0]
    confidence = model.predict_proba(features)[0]
    
    if prediction == 1:
        print(f" PHISHING DETECTED! Confidence: {confidence[1]*100:.1f}%\n")
    else:
        print(f" SAFE URL. Confidence: {confidence[0]*100:.1f}%\n")
