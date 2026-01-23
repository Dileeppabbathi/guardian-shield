# Guardian Shield - Development Plan

## 📅 16-Week Development Timeline

### ✅ Week 1-2: Foundation (CURRENT)
**Status**: In Progress

**Completed Tasks**:
- [x] Create project structure
- [x] Setup GitHub repository
- [x] Create documentation (README, QUICK_START)
- [x] Setup version control

**In Progress**:
- [ ] Install Android Studio
- [ ] Setup Python virtual environment
- [ ] Collect 10,000+ phishing URLs
- [ ] Collect 10,000+ legitimate URLs
- [ ] Setup development environment

**Deliverables**:
- Complete project structure
- Initial dataset (20,000+ URLs)
- Development environment ready

---

### 📱 Week 3-4: Android MVP
**Status**: Not Started

**Tasks**:
- [ ] Create Android project in Android Studio
- [ ] Implement NotificationListenerService
- [ ] Create notification content extractor
- [ ] Setup Room database
- [ ] Integrate Google Safe Browsing API
- [ ] Create basic URL scanner
- [ ] Design warning dialog UI
- [ ] Implement threat blocking mechanism
- [ ] Test notification interception

**Deliverables**:
- Working Android app
- Notification listener functional
- Basic URL scanning works
- Database stores threats

---

### 🤖 Week 5-6: ML - URL Classification
**Status**: Not Started

**Tasks**:
- [ ] Clean and preprocess URL dataset
- [ ] Extract URL features (length, domain, TLD, etc.)
- [ ] Train Random Forest classifier
- [ ] Train XGBoost classifier
- [ ] Evaluate models (accuracy, precision, recall)
- [ ] Select best model
- [ ] Save model for deployment
- [ ] Create inference script

**Target Metrics**:
- Accuracy: >95%
- Precision: >93%
- Recall: >92%
- F1-Score: >92%

**Deliverables**:
- Trained URL classifier
- Model evaluation report
- Saved model files (.pkl)

---

### 🖼️ Week 7-8: ML - Image Classification
**Status**: Not Started

**Tasks**:
- [ ] Collect malicious image dataset (10,000+)
- [ ] Collect safe image dataset (20,000+)
- [ ] Preprocess images (resize, normalize)
- [ ] Implement data augmentation
- [ ] Fine-tune MobileNetV2 model
- [ ] Train text classifier (DistilBERT)
- [ ] Integrate OCR (Tesseract/EasyOCR)
- [ ] Evaluate image model
- [ ] Convert models to TensorFlow Lite
- [ ] Optimize for mobile

**Target Metrics**:
- Image classification accuracy: >90%
- Text classification accuracy: >92%
- Model size: <50MB
- Inference time: <2 seconds

**Deliverables**:
- Image classification model (.tflite)
- Text classification model (.tflite)
- OCR pipeline
- Model conversion scripts

---

### 🔍 Week 9-10: Advanced Detection & Integration
**Status**: Not Started

**Tasks**:
- [ ] Implement QR code scanner (ZXing)
- [ ] Create QR code analyzer
- [ ] Implement steganography detection
- [ ] Add URL redirect analysis
- [ ] Integrate TensorFlow Lite in Android
- [ ] Create ML inference service
- [ ] Load models into app
- [ ] Test ML inference on device
- [ ] Optimize performance

**Deliverables**:
- QR code scanning functional
- Steganography detection working
- ML models integrated in app
- Complete threat detection pipeline

---

### 🎨 Week 11-12: User Interface & Features
**Status**: Not Started

**Tasks**:
- [ ] Design app
cat > CONTRIBUTING.md << 'EOF'
# Contributing to Guardian Shield

Thank you for your interest in contributing to Guardian Shield!

## Project Status

This is an academic project for a course. While it's open source, please note:
- Primary development by: Dileep Pabbathi
- Course project timeline: 16 weeks
- Feedback and suggestions welcome!

## How to Contribute

### Reporting Issues
- Use GitHub Issues to report bugs
- Provide detailed description
- Include steps to reproduce
- Attach screenshots if applicable

### Suggesting Features
- Open an issue with "Feature Request" label
- Describe the feature clearly
- Explain the use case

### Code Contributions
If you'd like to contribute code:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## Development Setup

See [QUICK_START.md](QUICK_START.md) for setup instructions.

## Code Style

- **Kotlin**: Follow Android Kotlin style guide
- **Python**: Follow PEP 8
- **Comments**: Write clear, concise comments

## Questions?

Open an issue or contact the maintainer.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
