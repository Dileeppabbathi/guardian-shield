"""
Simple URL Classifier for Guardian Shield
Trains a basic model to detect phishing URLs
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
from datetime import datetime

def extract_url_features(url):
    """Extract basic features from URL"""
    features = []
    features.append(len(url))  # URL length
    features.append(url.count('.'))  # Number of dots
    features.append(url.count('/'))  # Number of slashes
    features.append(url.count('-'))  # Number of hyphens
    features.append(url.count('?'))  # Has query params
    features.append(url.count('='))  # Number of equals
    features.append(1 if 'https' in url else 0)  # Is HTTPS
    features.append(1 if any(char.isdigit() for char in url) else 0)  # Has numbers
    features.append(1 if '@' in url else 0)  # Has @ symbol
    return features

print(" Guardian Shield - URL Classifier Training")
print("=" * 50)

# Load datasets
print("\n Loading datasets...")
phishing = pd.read_csv('../datasets/phishing_urls/openphish_20260122.csv')
legitimate1 = pd.read_csv('../datasets/legitimate_urls/legitimate_20260124.csv')
legitimate2 = pd.read_csv('../datasets/legitimate_urls/legitimate_expanded_20260124.csv')

legitimate = pd.concat([legitimate1, legitimate2])

print(f" Loaded {len(phishing)} phishing URLs")
print(f" Loaded {len(legitimate)} legitimate URLs")

# Prepare data
print("\n Preparing features...")
X = []
y = []

# Add phishing URLs
for url in phishing['url']:
    X.append(extract_url_features(str(url)))
    y.append(1)  # 1 = phishing

# Add legitimate URLs
for url in legitimate['url']:
    X.append(extract_url_features(str(url)))
    y.append(0)  # 0 = legitimate

X = np.array(X)
y = np.array(y)

print(f" Extracted features from {len(X)} URLs")

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f" Training set: {len(X_train)} samples")
print(f" Test set: {len(X_test)} samples")

# Train model
print("\n🤖 Training Random Forest model...")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
train_score = model.score(X_train, y_train)
test_score = model.score(X_test, y_test)

print(f"\n Training accuracy: {train_score*100:.2f}%")
print(f" Test accuracy: {test_score*100:.2f}%")

# Save model
model_filename = f'saved_models/url_classifier_{datetime.now().strftime("%Y%m%d")}.pkl'
with open(model_filename, 'wb') as f:
    pickle.dump(model, f)

print(f"\n Model saved to: {model_filename}")

# Test with examples
print("\n🧪 Testing with examples:")
test_urls = [
    "https://www.google.com",
    "http://phishing-site-123.suspicious.cc/login",
    "https://www.github.com",
    "http://secure-login.verify-account.tk"
]

for url in test_urls:
    features = np.array([extract_url_features(url)])
    prediction = model.predict(features)[0]
    confidence = model.predict_proba(features)[0]
    label = " PHISHING" if prediction == 1 else "✅ SAFE"
    print(f"{label} ({confidence[prediction]*100:.1f}%): {url[:50]}...")

print("\n" + "=" * 50)
print(" Training complete! Model ready to use!")
