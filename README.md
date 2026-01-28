# Guardian Shield

Multi-Layer AI-Based Threat Detection System

## Overview

Guardian Shield is a comprehensive machine learning-powered security system that detects malicious URLs, QR codes, images, and unknown zero-day threats in real-time. The system employs four independent ML models working in concert to provide multi-layer protection against cyber threats.

## Project Information

- **Author**: Dileep Pabbathi
- **Institution**: Arizona State University
- **Course**: CSE 543 - Information Assurance and Security
- **Date**: January 2026
- **Status**: Complete - Phase 1

## Features

- Multi-layer threat detection using 4 ML models
- Real-time URL phishing detection (89.59% accuracy)
- QR code malware detection (85.50% accuracy)
- Image-based threat classification (83.10% accuracy)
- Zero-day anomaly detection (62.7% detection rate)
- Desktop applications with visual analytics
- Web-based interface (deployed on Streamlit Cloud)

## Machine Learning Models

### 1. URL Threat Classifier
- **Algorithm**: Random Forest (100 estimators)
- **Training Data**: 651,199 URLs from Kaggle
- **Features**: 9 URL-based indicators
- **Accuracy**: 89.59%

### 2. QR Code Classifier
- **Algorithm**: Random Forest (100 estimators)
- **Training Data**: 2,000 generated QR codes
- **Features**: 8 combined features (image + URL analysis)
- **Accuracy**: 85.50%

### 3. Image Threat Classifier
- **Algorithm**: Transfer Learning with MobileNetV2
- **Training Data**: 3,201 images (balanced: 1,500 malware, 550 phishing, 1,151 safe)
- **Accuracy**: 83.10% validation, 80% real-world

### 4. Anomaly Detection Model
- **Algorithm**: Convolutional Autoencoder
- **Training Data**: 1,151 safe images only
- **Detection Rate**: 62.7% on unknown malware

## Performance Summary

| Model | Accuracy/Detection | Training Samples |
|-------|-------------------|------------------|
| URL Classifier | 89.59% | 651,199 |
| QR Classifier | 85.50% | 2,000 |
| Image Classifier | 83.10% | 3,201 |
| Anomaly Detector | 62.7% | 1,151 |

## Installation

### Prerequisites
- Python 3.11+
- 8GB RAM minimum
- 5GB free disk space

### Setup
```bash
git clone https://github.com/Dileeppabbathi/guardian-shield.git
cd guardian-shield
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

### Desktop Application
```bash
python3 desktop-app/guardian_shield_ultra.py
```

### Web Application
```bash
streamlit run web_app.py
```

**Live Demo**: https://guardian-shield-wsm3t93teo7alrauatsc3x.streamlit.app/

## Technology Stack

- **ML Frameworks**: scikit-learn, TensorFlow, Keras
- **Computer Vision**: OpenCV, PIL
- **Web**: Streamlit
- **Desktop**: Tkinter
- **Data**: Pandas, NumPy

## Datasets

- **URLs**: 651,199 samples (Kaggle)
- **Malware Images**: 22,056 samples
- **Phishing Screenshots**: 550 samples
- **Safe Images**: 1,151 samples

## Project Structure
```
guardian-shield/
├── ml-models/              # ML models and training scripts
├── desktop-app/            # Desktop applications
├── datasets/               # Training data
├── web_app.py             # Streamlit web app
└── requirements.txt       # Dependencies
```

## Known Limitations

1. Image model has limited phishing detection (40%) due to small dataset
2. Anomaly detector has 16% false positive rate
3. Large model files (>100MB) not included in repository

## Future Work

- Android mobile application
- Expand phishing image dataset to 10K+ samples
- Real-time notification monitoring
- API for third-party integration

## Contact

- **Author**: Dileep Pabbathi
- **GitHub**: https://github.com/Dileeppabbathi/guardian-shield
- **Email**: dpabbath@asu.edu

## License

Academic project - Arizona State University

---

**Status**: Active Development | **Version**: 3.0 | **Updated**: January 28, 2026
