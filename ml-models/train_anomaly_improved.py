"""
Improved Anomaly Detector with lower threshold and better features
"""

import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
import os
from PIL import Image
from sklearn.model_selection import train_test_split

print("🔍 IMPROVED ANOMALY DETECTION TRAINING")
print("=" * 60)

# Load safe images
data_dir = '../datasets/images/balanced/safe'
print(f"\n📂 Loading safe images from: {data_dir}")

images = []
for filename in os.listdir(data_dir):
    if filename.endswith(('.png', '.jpg', '.jpeg')):
        try:
            img_path = os.path.join(data_dir, filename)
            img = Image.open(img_path).convert('RGB')
            img = img.resize((128, 128))
            img_array = np.array(img) / 255.0
            images.append(img_array)
        except:
            pass

images = np.array(images)
print(f"✅ Loaded {len(images)} safe images")

X_train, X_test = train_test_split(images, test_size=0.2, random_state=42)
print(f"📊 Training: {len(X_train)}, Testing: {len(X_test)}")

# IMPROVED: Deeper autoencoder
print(f"\n🏗️ Building IMPROVED Autoencoder...")

encoder_input = layers.Input(shape=(128, 128, 3))
x = layers.Conv2D(32, (3, 3), activation='relu', padding='same')(encoder_input)
x = layers.MaxPooling2D((2, 2), padding='same')(x)
x = layers.Conv2D(64, (3, 3), activation='relu', padding='same')(x)
x = layers.MaxPooling2D((2, 2), padding='same')(x)
x = layers.Conv2D(128, (3, 3), activation='relu', padding='same')(x)
x = layers.MaxPooling2D((2, 2), padding='same')(x)
x = layers.Conv2D(256, (3, 3), activation='relu', padding='same')(x)  # ADDED
encoded = layers.MaxPooling2D((2, 2), padding='same')(x)

x = layers.Conv2D(256, (3, 3), activation='relu', padding='same')(encoded)  # ADDED
x = layers.UpSampling2D((2, 2))(x)
x = layers.Conv2D(128, (3, 3), activation='relu', padding='same')(x)
x = layers.UpSampling2D((2, 2))(x)
x = layers.Conv2D(64, (3, 3), activation='relu', padding='same')(x)
x = layers.UpSampling2D((2, 2))(x)
x = layers.Conv2D(32, (3, 3), activation='relu', padding='same')(x)
x = layers.UpSampling2D((2, 2))(x)
decoder_output = layers.Conv2D(3, (3, 3), activation='sigmoid', padding='same')(x)

autoencoder = keras.Model(encoder_input, decoder_output)
autoencoder.compile(optimizer='adam', loss='mse')

print("\n🚀 Training for 50 epochs...")

history = autoencoder.fit(
    X_train, X_train,
    epochs=50,
    batch_size=32,
    validation_data=(X_test, X_test),
    verbose=1
)

# IMPROVED: Lower threshold (85th percentile instead of 95th)
reconstructions = autoencoder.predict(X_test, verbose=0)
mse = np.mean(np.power(X_test - reconstructions, 2), axis=(1,2,3))
threshold = np.percentile(mse, 85)  # CHANGED from 95 to 85

print(f"\n📊 IMPROVED Anomaly threshold: {threshold:.6f} (was ~0.008)")

# Save
autoencoder.save('saved_models/anomaly_detector_improved.h5')
np.save('saved_models/anomaly_threshold_improved.npy', threshold)

print(f"\n✅ Improved model saved!")

# Test immediately
print(f"\n🧪 Quick test on malware...")
malware_dir = '../datasets/images/balanced/malware'
malware_imgs = []

for f in os.listdir(malware_dir)[:100]:
    if f.endswith('.png'):
        try:
            img = Image.open(os.path.join(malware_dir, f)).convert('RGB')
            img = img.resize((128, 128))
            malware_imgs.append(np.array(img) / 255.0)
        except:
            pass

if malware_imgs:
    malware_imgs = np.array(malware_imgs)
    mal_recon = autoencoder.predict(malware_imgs, verbose=0)
    mal_mse = np.mean(np.power(malware_imgs - mal_recon, 2), axis=(1,2,3))
    detected = np.sum(mal_mse > threshold)
    rate = (detected / len(mal_mse)) * 100
    print(f"   Malware detection: {rate:.1f}% (was 19%)")

print(f"\n🎉 IMPROVED ANOMALY DETECTOR COMPLETE!")
