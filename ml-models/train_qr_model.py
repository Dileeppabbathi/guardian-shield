"""
QR Code Malware Detector
Generates QR dataset and trains classifier
"""

import qrcode
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd
from datetime import datetime

print(" GUARDIAN SHIELD - QR CODE MODEL TRAINING")
print("=" * 50)

# Load URLs from our trained dataset
print("\n Loading URL dataset...")
df = pd.read_csv('../datasets/urls_kaggle/malicious_phish.csv')

# Take subset for QR generation (1000 each)
benign_urls = df[df['type'] == 'benign']['url'].head(1000).tolist()
malicious_urls = df[df['type'] != 'benign']['url'].head(1000).tolist()

print(f" URLs loaded:")
print(f"   Benign: {len(benign_urls)}")
print(f"   Malicious: {len(malicious_urls)}")

# Generate QR codes
print("\n️ Generating QR codes...")
qr_features = []
labels = []

def extract_qr_features(url):
    """Generate QR and extract features"""
    # Generate QR code
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Convert to numpy array
    img_array = np.array(img.convert('L'))
    
    # Extract features
    features = []
    features.append(img_array.mean())  # Average pixel value
    features.append(img_array.std())   # Standard deviation
    features.append(img_array.min())   # Min value
    features.append(img_array.max())   # Max value
    features.append(len(url))          # URL length
    features.append(url.count('.'))    # Dots
    features.append(url.count('/'))    # Slashes
    features.append(1 if 'https' in url else 0)  # HTTPS
    
    return features

# Process benign QRs
print("  Processing benign QRs...")
for i, url in enumerate(benign_urls):
    if i % 100 == 0:
        print(f"    {i}/{len(benign_urls)}")
    try:
        features = extract_qr_features(url)
        qr_features.append(features)
        labels.append(0)  # Benign
    except:
        continue

# Process malicious QRs
print("  Processing malicious QRs...")
for i, url in enumerate(malicious_urls):
    if i % 100 == 0:
        print(f"    {i}/{len(malicious_urls)}")
    try:
        features = extract_qr_features(url)
        qr_features.append(features)
        labels.append(1)  # Malicious
    except:
        continue

X = np.array(qr_features)
y = np.array(labels)

print(f"\n QR features extracted: {X.shape}")
print(f"   Benign: {np.sum(y==0)}")
print(f"   Malicious: {np.sum(y==1)}")

# Split dataset
print("\n Splitting dataset...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
print("\n🤖 Training Random Forest...")
model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
model.fit(X_train, y_train)

# Evaluate
train_acc = accuracy_score(y_train, model.predict(X_train))
test_acc = accuracy_score(y_test, model.predict(X_test))

print(f"\n Training Accuracy: {train_acc*100:.2f}%")
print(f" Testing Accuracy: {test_acc*100:.2f}%")

# Classification report
y_pred = model.predict(X_test)
print("\n Classification Report:")
print(classification_report(y_test, y_pred, target_names=['Benign', 'Malicious']))

# Save model
model_path = 'saved_models/qr_classifier_20260127.pkl'
print(f"\n Saving model to: {model_path}")
with open(model_path, 'wb') as f:
    pickle.dump(model, f)

print("\n QR MODEL TRAINING COMPLETE!")
print(f" Final Stats:")
print(f"   Dataset Size: {len(X)} QR codes")
print(f"   Test Accuracy: {test_acc*100:.2f}%")
print(f"   Model Saved: ")
