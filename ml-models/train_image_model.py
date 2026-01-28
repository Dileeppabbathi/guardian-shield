"""
Image Malware Detector - CNN with Transfer Learning
Using MobileNetV2 for efficient mobile deployment
"""

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense, Dropout
from tensorflow.keras.optimizers import Adam
import os
from datetime import datetime
import numpy as np

print(" GUARDIAN SHIELD - IMAGE MODEL TRAINING")
print("=" * 60)

# Paths
data_dir = '../datasets/images/balanced'
model_save_path = 'saved_models/image_classifier_20260127.h5'

# Check dataset
print(f"\n Checking dataset at: {data_dir}")
categories = os.listdir(data_dir)
print(f"Categories found: {categories}")

for cat in categories:
    path = os.path.join(data_dir, cat)
    if os.path.isdir(path):
        count = len([f for f in os.listdir(path) if f.endswith(('.jpg', '.png', '.jpeg'))])
        print(f"  {cat}: {count:,} images")

# Image parameters
IMG_SIZE = 224
BATCH_SIZE = 32
EPOCHS = 10

# Data augmentation
print("\n Setting up data generators...")
train_datagen = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    horizontal_flip=True,
    zoom_range=0.2,
    shear_range=0.2,
    fill_mode='nearest'
)

# Load training data
train_generator = train_datagen.flow_from_directory(
    data_dir,
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    subset='training',
    shuffle=True
)

# Load validation data
validation_generator = train_datagen.flow_from_directory(
    data_dir,
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    subset='validation',
    shuffle=False
)

num_classes = len(train_generator.class_indices)
print(f"\n Data loaded:")
print(f"   Training samples: {train_generator.samples:,}")
print(f"   Validation samples: {validation_generator.samples:,}")
print(f"   Classes: {train_generator.class_indices}")

# Build model
print("\n Building MobileNetV2 model...")
base_model = MobileNetV2(
    weights='imagenet',
    include_top=False,
    input_shape=(IMG_SIZE, IMG_SIZE, 3)
)

# Freeze base model
base_model.trainable = False

# Add custom layers
model = keras.Sequential([
    base_model,
    GlobalAveragePooling2D(),
    Dense(512, activation='relu'),
    Dropout(0.5),
    Dense(256, activation='relu'),
    Dropout(0.3),
    Dense(num_classes, activation='softmax')
])

# Compile
model.compile(
    optimizer=Adam(learning_rate=0.001),
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

print("\n Model Summary:")
model.summary()

# Callbacks
callbacks = [
    keras.callbacks.EarlyStopping(
        monitor='val_loss',
        patience=3,
        restore_best_weights=True
    ),
    keras.callbacks.ReduceLROnPlateau(
        monitor='val_loss',
        factor=0.5,
        patience=2,
        min_lr=0.00001
    ),
    keras.callbacks.ModelCheckpoint(
        model_save_path,
        monitor='val_accuracy',
        save_best_only=True,
        verbose=1
    )
]

# Train
print("\n Starting training...")
print(f"   Epochs: {EPOCHS}")
print(f"   Batch size: {BATCH_SIZE}")
print(f"   Image size: {IMG_SIZE}x{IMG_SIZE}")

history = model.fit(
    train_generator,
    epochs=EPOCHS,
    validation_data=validation_generator,
    callbacks=callbacks,
    verbose=1
)

# Evaluate
print("\n Final Evaluation:")
train_loss, train_acc = model.evaluate(train_generator, verbose=0)
val_loss, val_acc = model.evaluate(validation_generator, verbose=0)

print(f"   Training Accuracy: {train_acc*100:.2f}%")
print(f"   Validation Accuracy: {val_acc*100:.2f}%")

# Convert to TensorFlow Lite for mobile
print("\n Converting to TensorFlow Lite...")
converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
tflite_model = converter.convert()

tflite_path = 'saved_models/image_classifier_20260127.tflite'
with open(tflite_path, 'wb') as f:
    f.write(tflite_model)

print(f" TFLite model saved: {tflite_path}")
print(f"   Size: {len(tflite_model)/1024/1024:.2f} MB")

print("\n IMAGE MODEL TRAINING COMPLETE!")
print(f" Final Stats:")
print(f"   Training samples: {train_generator.samples:,}")
print(f"   Validation Accuracy: {val_acc*100:.2f}%")
print(f"   Model saved: ")
print(f"   TFLite saved: ")
