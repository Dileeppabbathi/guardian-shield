"""
Enhanced URL Classifier - Training with 651K URLs from Kaggle
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import pickle
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

print(" GUARDIAN SHIELD - URL MODEL TRAINING")
print("=" * 50)

# Load Kaggle dataset
print("\n Loading dataset (651K URLs)...")
df = pd.read_csv('../datasets/urls_kaggle/malicious_phish.csv')

print(f" Loaded: {len(df):,} URLs")
print(f"\nDataset distribution:")
print(df['type'].value_counts())

# Feature extraction function
def extract_url_features(url):
    """Extract 9 features from URL"""
    features = []
    features.append(len(url))                                    # URL length
    features.append(url.count('.'))                              # Dot count
    features.append(url.count('/'))                              # Slash count
    features.append(url.count('-'))                              # Hyphen count
    features.append(url.count('?'))                              # Question mark
    features.append(url.count('='))                              # Equals sign
    features.append(1 if 'https' in url else 0)                  # HTTPS flag
    features.append(1 if any(char.isdigit() for char in url) else 0)  # Has digits
    features.append(1 if '@' in url else 0)                      # Has @ symbol
    return features

# Prepare data
print("\n Extracting features...")
X = []
y = []

for idx, row in df.iterrows():
    if idx % 50000 == 0:
        print(f"  Processing: {idx:,}/{len(df):,}")
    
    try:
        features = extract_url_features(row['url'])
        X.append(features)
        
        # Binary classification: benign=0, malicious=1
        label = 0 if row['type'] == 'benign' else 1
        y.append(label)
    except:
        continue

X = np.array(X)
y = np.array(y)

print(f"\n Features extracted: {X.shape}")
print(f"   Benign: {np.sum(y==0):,} ({np.sum(y==0)/len(y)*100:.1f}%)")
print(f"   Malicious: {np.sum(y==1):,} ({np.sum(y==1)/len(y)*100:.1f}%)")

# Split dataset
print("\n Splitting dataset (80-20)...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"   Training: {len(X_train):,} samples")
print(f"   Testing: {len(X_test):,} samples")

# Train model
print("\n🤖 Training Random Forest...")
model = RandomForestClassifier(
    n_estimators=100,
    max_depth=20,
    random_state=42,
    n_jobs=-1,
    verbose=1
)

model.fit(X_train, y_train)

# Evaluate
print("\n Evaluating model...")
train_acc = accuracy_score(y_train, model.predict(X_train))
test_acc = accuracy_score(y_test, model.predict(X_test))

print(f"\n Training Accuracy: {train_acc*100:.2f}%")
print(f" Testing Accuracy: {test_acc*100:.2f}%")

# Detailed metrics
y_pred = model.predict(X_test)
print("\n Classification Report:")
print(classification_report(y_test, y_pred, target_names=['Benign', 'Malicious']))

print("\n Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Feature importance
print("\n Feature Importance:")
features_names = ['length', 'dots', 'slashes', 'hyphens', 'questions', 'equals', 'https', 'digits', 'at_symbol']
importances = model.feature_importances_
for name, importance in sorted(zip(features_names, importances), key=lambda x: x[1], reverse=True):
    print(f"   {name:12s}: {importance:.4f}")

# Save model
timestamp = datetime.now().strftime('%Y%m%d')
model_path = f'saved_models/url_classifier_kaggle_{timestamp}.pkl'

print(f"\n Saving model to: {model_path}")
with open(model_path, 'wb') as f:
    pickle.dump(model, f)

print("\n TRAINING COMPLETE!")
print(f" Final Stats:")
print(f"   Dataset Size: {len(df):,} URLs")
print(f"   Training Samples: {len(X_train):,}")
print(f"   Test Accuracy: {test_acc*100:.2f}%")
print(f"   Model Saved: ")
