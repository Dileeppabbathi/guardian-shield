# Guardian Shield

AI-Based Real-Time Threat Detection System for URLs and QR Codes

## Overview

Guardian Shield is a machine learning-powered security application that detects malicious URLs and QR codes in real-time. The system uses Random Forest classifiers trained on over 650,000 URLs to identify phishing attempts, malware distribution sites, and other cyber threats.

## Features

- **URL Threat Detection**: Analyzes URLs using 9 extracted features with 89.59% accuracy
- **QR Code Analysis**: Decodes and validates QR codes with 85.50% accuracy
- **Real-Time Scanning**: Instant threat detection and classification
- **Multi-Platform Support**: Desktop applications and web interface
- **Visual Analytics**: Real-time charts and statistics dashboard
- **Export Capabilities**: CSV export for scan history and analysis

## Technical Specifications

### Machine Learning Models

**URL Classifier**
- Algorithm: Random Forest (100 estimators)
- Training Dataset: 651,199 URLs
- Features: 9 URL-based indicators
- Accuracy: 89.59%
- Model Size: 158 KB

**QR Code Classifier**
- Algorithm: Random Forest (100 estimators)
- Training Dataset: 2,000 QR codes
- Features: 8 image and URL features
- Accuracy: 85.50%
- Model Size: ~2 MB

### Technology Stack

- **Languages**: Python 3.11, Kotlin
- **ML Frameworks**: Scikit-learn, TensorFlow
- **Web Framework**: Streamlit
- **GUI**: Tkinter
- **Data Processing**: Pandas, NumPy
- **Visualization**: Matplotlib, Plotly

## Project Structure
```
guardian-shield/
├── ml-models/              # Machine learning models and training scripts
│   ├── saved_models/       # Trained model files
│   ├── train_url_model_kaggle.py
│   └── train_qr_model.py
├── desktop-app/            # Desktop applications
│   ├── guardian_shield_app.py
│   ├── guardian_shield_pro.py
│   └── guardian_shield_ultra.py
├── datasets/               # Training datasets
│   ├── urls_kaggle/       # URL datasets (651K URLs)
│   └── images/            # Image datasets
├── web_app.py             # Web application
├── docs/                  # Documentation and GitHub Pages
└── android-app/           # Android application structure
```

## Installation

### Prerequisites

- Python 3.11 or higher
- pip package manager
- 2GB free disk space

### Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/Dileeppabbathi/guardian-shield.git
cd guardian-shield
```

2. Create virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Desktop Application

Run the ULTRA version with visual analytics:
```bash
python3 desktop-app/guardian_shield_ultra.py
```

Run the PRO version with batch scanning:
```bash
python3 desktop-app/guardian_shield_pro.py
```

### Web Application

Run locally:
```bash
streamlit run web_app.py
```

Access the live deployment:
[https://guardian-shield-wsm3t93teo7alrauatsc3x.streamlit.app/](https://guardian-shield-wsm3t93teo7alrauatsc3x.streamlit.app/)

### Training Models

Retrain URL classifier:
```bash
cd ml-models
python3 train_url_model_kaggle.py
```

Train QR classifier:
```bash
python3 train_qr_model.py
```

## Performance Metrics

### URL Classifier Results
- Training Samples: 520,952
- Test Samples: 130,239
- Training Accuracy: 91.23%
- Test Accuracy: 89.59%
- Precision: 0.86
- Recall: 0.85
- F1-Score: 0.85

### QR Classifier Results
- Training Samples: 1,600
- Test Samples: 400
- Training Accuracy: 99.88%
- Test Accuracy: 85.50%
- Precision: 0.86
- Recall: 0.85
- F1-Score: 0.86

## Development Roadmap

### Completed (Week 1-2)
- [x] URL classification model (89.59% accuracy)
- [x] QR code detection model (85.50% accuracy)
- [x] Desktop applications (3 versions)
- [x] Web application with Streamlit
- [x] Data collection (651K URLs)
- [x] Real-time analytics dashboard
- [x] Documentation and deployment

### In Progress (Week 3-4)
- [ ] Android application development
- [ ] Image-based malware detection
- [ ] Notification monitoring service

### Future Enhancements (Week 5+)
- [ ] Anomaly detection for zero-day threats
- [ ] Continuous learning pipeline
- [ ] Threat intelligence API integration
- [ ] Mobile deployment with TensorFlow Lite

## Dataset Information

### URL Dataset
- Source: Kaggle (malicious-urls-dataset)
- Total URLs: 651,199
- Categories: Benign, Phishing, Defacement, Malware
- Format: CSV
- Size: 44 MB

### QR Code Dataset
- Source: Generated from URL dataset
- Total QR Codes: 2,000
- Categories: Benign (1,000), Malicious (1,000)
- Generation Method: qrcode library

## Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Dileep Pabbathi**
- GitHub: [@Dileeppabbathi](https://github.com/Dileeppabbathi)
- Project Link: [https://github.com/Dileeppabbathi/guardian-shield](https://github.com/Dileeppabbathi/guardian-shield)

## Acknowledgments

- Kaggle for providing the malicious URLs dataset
- OpenPhish for phishing URL feeds
- TensorFlow and Scikit-learn communities
- Streamlit for web deployment platform

## Citation

If you use this project in your research or work, please cite:
```bibtex
@software{guardian_shield_2026,
  author = {Pabbathi, Dileep},
  title = {Guardian Shield: AI-Based Real-Time Threat Detection System},
  year = {2026},
  url = {https://github.com/Dileeppabbathi/guardian-shield}
}
```

## Project Statistics

- Lines of Code: 3,000+
- Commits: 25+
- Files: 40+
- Training Time: ~4 hours
- Development Time: ~16 hours
- Models Trained: 2
- Accuracy Range: 85-90%

---

**Status**: Active Development | **Version**: 3.0 | **Last Updated**: January 2026
