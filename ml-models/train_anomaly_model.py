"""
Guardian Shield - Anomaly Detection Model
Detects unknown threats using autoencoder reconstruction error
"""

import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import os
from PIL import Image
from sklearn.model_selection import train_test_split

print(" GUARDIAN SHIELD - ANOMALY DETECTION TRAINING")
print("=" * 60)

# Load ONLY safe images
data_dir = '../datasets/images/balanced/safe'
print(f"\n Loading safe images from: {data_dir}")

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
print(f" Loaded {len(images)} safe images")

# Split
X_train, X_test = train_test_split(images, test_size=0.2, random_state=42)
print(f"\n Training: {len(X_train)}, Testing: {len(X_test)}")

# Build Autoencoder
print(f"\n Building Autoencoder...")

encoder_input = layers.Input(shape=(128, 128, 3))
x = layers.Conv2D(32, (3, 3), activation='relu', padding='same')(encoder_input)
x = layers.MaxPooling2D((2, 2), padding='same')(x)
x = layers.Conv2D(64, (3, 3), activation='relu', padding='same')(x)
x = layers.MaxPooling2D((2, 2), padding='same')(x)
x = layers.Conv2D(128, (3, 3), activation='relu', padding='same')(x)
encoded = layers.MaxPooling2D((2, 2), padding='same')(x)

x = layers.Conv2D(128, (3, 3), activation='relu', padding='same')(encoded)
x = layers.UpSampling2D((2, 2))(x)
x = layers.Conv2D(64, (3, 3), activation='relu', padding='same')(x)
x = layers.UpSampling2D((2, 2))(x)
x = layers.Conv2D(32, (3, 3), activation='relu', padding='same')(x)
x = layers.UpSampling2D((2, 2))(x)
decoder_output = layers.Conv2D(3, (3, 3), activation='sigmoid', padding='same')(x)

autoencoder = keras.Model(encoder_input, decoder_output)
autoencoder.compile(optimizer='adam', loss='mse')

print("\n Training for 50 epochs...")

history = autoencoder.fit(
    X_train, X_train,
    epochs=50,
    batch_size=32,
    validation_data=(X_test, X_test),
    verbose=1
)

# Calculate threshold
reconstructions = autoencoder.predict(X_test, verbose=0)
mse = np.mean(np.power(X_test - reconstructions, 2), axis=(1,2,3))
threshold = np.percentile(mse, 95)

print(f"\n Anomaly threshold: {threshold:.6f}")

# Save
autoencoder.save('saved_models/anomaly_detector_20260128.h5')
np.save('saved_models/anomaly_threshold.npy', threshold)

print(f"\n Model saved!")
print(f" ANOMALY DETECTION COMPLETE!")
