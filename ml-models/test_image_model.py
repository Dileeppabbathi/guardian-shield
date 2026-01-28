"""
Test Image Model with Real Examples
"""

import tensorflow as tf
from tensorflow import keras
import numpy as np
from PIL import Image
import sys

print("🧪 TESTING IMAGE MODEL")
print("=" * 50)

# Load model
print("\n Loading model...")
model = keras.models.load_model('saved_models/image_classifier_20260127.h5')
print(" Model loaded!")

# Class mapping
classes = {0: 'malware', 1: 'phishing', 2: 'safe'}

def test_image(image_path):
    """Test a single image"""
    try:
        # Load and preprocess
        img = Image.open(image_path).convert('RGB')
        img = img.resize((224, 224))
        img_array = np.array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)
        
        # Predict
        predictions = model.predict(img_array, verbose=0)
        predicted_class = np.argmax(predictions[0])
        confidence = predictions[0][predicted_class] * 100
        
        print(f"\n Image: {image_path}")
        print(f"   Prediction: {classes[predicted_class].upper()}")
        print(f"   Confidence: {confidence:.2f}%")
        print(f"   All probabilities:")
        for i, prob in enumerate(predictions[0]):
            print(f"      {classes[i]}: {prob*100:.2f}%")
        
        return classes[predicted_class], confidence
    except Exception as e:
        print(f" Error: {e}")
        return None, None

# Check what images we actually have
import os
print("\n Checking dataset structure...")
data_dir = '../datasets/images/raw'
for category in ['safe', 'malware', 'phishing']:
    path = os.path.join(data_dir, category)
    if os.path.exists(path):
        files = [f for f in os.listdir(path) if f.endswith(('.jpg', '.png', '.jpeg'))][:5]
        print(f"\n{category.upper()} folder samples:")
        for f in files:
            full_path = os.path.join(path, f)
            test_image(full_path)
