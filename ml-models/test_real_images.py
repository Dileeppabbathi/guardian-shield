import tensorflow as tf
from tensorflow import keras
import numpy as np
from PIL import Image
import os
import random

print("🧪 TESTING IMAGE MODEL WITH REAL SAMPLES")
print("=" * 50)

# Load model
model = keras.models.load_model('saved_models/image_classifier_20260127.h5')
classes = {0: 'malware', 1: 'phishing', 2: 'safe'}

def test_image(image_path, true_label):
    """Test a single image"""
    img = Image.open(image_path).convert('RGB')
    img = img.resize((224, 224))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    
    predictions = model.predict(img_array, verbose=0)
    predicted_class = np.argmax(predictions[0])
    confidence = predictions[0][predicted_class] * 100
    
    correct = "✅" if classes[predicted_class] == true_label else "❌"
    
    print(f"{correct} True: {true_label:10s} | Predicted: {classes[predicted_class]:10s} | Confidence: {confidence:.1f}%")
    return classes[predicted_class] == true_label

# Test samples from each category
data_dir = '../datasets/images/raw'
results = []

print("\n📊 Testing Random Samples:")
print("-" * 50)

for category in ['malware', 'phishing', 'safe']:
    path = os.path.join(data_dir, category)
    files = [f for f in os.listdir(path) if f.endswith(('.png', '.jpg', '.jpeg'))]
    
    # Test 5 random samples from each
    samples = random.sample(files, min(5, len(files)))
    
    print(f"\n{category.upper()} samples:")
    for sample in samples:
        correct = test_image(os.path.join(path, sample), category)
        results.append(correct)

# Summary
accuracy = sum(results) / len(results) * 100
print(f"\n{'='*50}")
print(f"Manual Test Accuracy: {accuracy:.1f}%")
print(f"Correct: {sum(results)}/{len(results)}")
