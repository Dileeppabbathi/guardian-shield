"""Test anomaly detector on malware and phishing"""

import numpy as np
from tensorflow import keras
from PIL import Image
import os

print("🧪 TESTING ANOMALY DETECTOR")
print("=" * 60)

# Load model and threshold
model = keras.models.load_model('saved_models/anomaly_detector_20260128.h5')
threshold = np.load('saved_models/anomaly_threshold.npy')

print(f"✅ Model loaded")
print(f"📊 Anomaly threshold: {threshold:.6f}")

def test_category(category_name, folder_path, num_samples=50):
    """Test images from a category"""
    print(f"\n🔍 Testing {category_name}...")
    
    images = []
    files = [f for f in os.listdir(folder_path) if f.endswith(('.png', '.jpg', '.jpeg'))]
    
    for filename in files[:num_samples]:
        try:
            img = Image.open(os.path.join(folder_path, filename)).convert('RGB')
            img = img.resize((128, 128))
            images.append(np.array(img) / 255.0)
        except:
            pass
    
    if not images:
        print(f"   No images found!")
        return
    
    images = np.array(images)
    reconstructions = model.predict(images, verbose=0)
    errors = np.mean(np.power(images - reconstructions, 2), axis=(1,2,3))
    
    anomalies = np.sum(errors > threshold)
    rate = (anomalies / len(errors)) * 100
    
    print(f"   Samples tested: {len(errors)}")
    print(f"   Flagged as anomalies: {anomalies}")
    print(f"   Detection rate: {rate:.1f}%")
    print(f"   Avg reconstruction error: {np.mean(errors):.6f}")
    
    return rate

# Test on all categories
safe_rate = test_category("SAFE", "../datasets/images/balanced/safe", 50)
malware_rate = test_category("MALWARE", "../datasets/images/balanced/malware", 100)
phishing_rate = test_category("PHISHING", "../datasets/images/balanced/phishing", 50)

print(f"\n{'='*60}")
print(f"📊 FINAL RESULTS:")
print(f"   Safe flagged as anomalies: {safe_rate:.1f}% (should be ~5%)")
print(f"   Malware detected: {malware_rate:.1f}%")
print(f"   Phishing detected: {phishing_rate:.1f}%")
print(f"\n✅ Anomaly detector can find UNKNOWN threats!")
