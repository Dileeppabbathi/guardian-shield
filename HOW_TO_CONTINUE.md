# Project Continuation Guide

## Guardian Shield: Quick Start and Continuation Instructions

**Purpose**: This document provides concise instructions for resuming work on Guardian Shield in new development sessions.

---

## Quick Start Commands

### Activate Development Environment
```bash
cd ~/Downloads/guardian-shield
source venv/bin/activate
```

### Run Applications

**Desktop Application (ULTRA version with analytics)**
```bash
python3 desktop-app/guardian_shield_ultra.py
```

**Web Application (local)**
```bash
streamlit run web_app.py
```

**Web Application (deployed)**
```
https://guardian-shield-wsm3t93teo7alrauatsc3x.streamlit.app/
```

### Train Models

**URL Classifier**
```bash
cd ml-models
python3 train_url_model_kaggle.py
```

**QR Code Classifier**
```bash
cd ml-models
python3 train_qr_model.py
```

**Image Classifier** (pending proper dataset)
```bash
cd ml-models
python3 train_image_model.py
```

---

## Project Structure
```
guardian-shield/
 ml-models/                    # Machine learning models
    saved_models/            # Trained model files (.pkl, .h5)
    train_url_model_kaggle.py
    train_qr_model.py
    train_image_model.py
 desktop-app/                 # Desktop applications
    guardian_shield_app.py        # Basic version
    guardian_shield_pro.py        # PRO version
    guardian_shield_ultra.py      # ULTRA version with charts
 datasets/                    # Training datasets
    urls_kaggle/            # 651K URLs
    images/                 # Image datasets
 web_app.py                  # Streamlit web application
 docs/                       # GitHub Pages documentation
 android-app/                # Android project structure
 requirements.txt            # Python dependencies
```

---

## Current Project Status

### Completed Components

**Models**
- URL Classifier: 89.59% accuracy, 651K training samples
- QR Classifier: 85.50% accuracy, 2K training samples

**Applications**
- Desktop: 3 versions (Basic, PRO, ULTRA)
- Web: Deployed on Streamlit Cloud

**Data**
- URLs: 651,199 samples collected
- QR Codes: 2,000 generated
- Images: 202,603 collected (pending proper categorization)

### In Progress
- Image classification model (requires malware/phishing datasets)
- Android application (structure created, implementation pending)

### Not Started
- Anomaly detection
- Continuous learning pipeline
- Threat intelligence integration

---

## Essential Commands Reference

### Python Virtual Environment
```bash
# Create virtual environment
python3 -m venv venv

# Activate (macOS/Linux)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate

# Deactivate
deactivate

# Install dependencies
pip install -r requirements.txt
```

### Git Operations
```bash
# Check status
git status

# Add files
git add .

# Commit changes
git commit -m "Description of changes"

# Push to GitHub
git push origin main

# Pull latest changes
git pull origin main

# View commit history
git log --oneline

# Create new branch
git checkout -b feature-name

# Switch branches
git checkout branch-name
```

### Dataset Operations
```bash
# Check dataset sizes
du -sh datasets/*/

# Count files in directories
find datasets/ -type f | wc -l

# View dataset samples
head -20 datasets/urls_kaggle/malicious_phish.csv
```

### Model Operations
```bash
# List trained models
ls -lh ml-models/saved_models/

# Check model size
du -sh ml-models/saved_models/*.pkl

# Test model loading
python3 -c "import pickle; m = pickle.load(open('ml-models/saved_models/url_classifier_kaggle_20260127.pkl', 'rb')); print('Model loaded successfully')"
```

---

## Common Tasks

### Add New Features to Web App

1. Edit `web_app.py`
2. Test locally: `streamlit run web_app.py`
3. Commit changes: `git commit -am "Add feature description"`
4. Push to GitHub: `git push`
5. Streamlit Cloud auto-deploys (wait 2-3 minutes)

### Retrain Models

1. Navigate to `ml-models/` directory
2. Run appropriate training script
3. Model saves to `saved_models/` directory
4. Update applications to use new model
5. Test thoroughly before deployment

### Update Documentation

1. Edit relevant `.md` files
2. Preview changes locally
3. Commit with descriptive message
4. Push to update GitHub Pages (if applicable)

### Collect New Data

1. Identify data sources (Kaggle, research datasets)
2. Download to `datasets/` directory
3. Organize into appropriate subdirectories
4. Document data sources and statistics
5. Update README.md with new dataset information

---

## Troubleshooting

### Virtual Environment Issues

**Problem**: `command not found: python3`  
**Solution**: Use `python` instead of `python3`

**Problem**: `ModuleNotFoundError`  
**Solution**: Ensure venv is activated, then `pip install -r requirements.txt`

**Problem**: Permission denied  
**Solution**: `chmod +x script_name.sh` or run with `python3` instead of `./`

### Model Loading Issues

**Problem**: Model file not found  
**Solution**: Check file path, ensure you're in correct directory

**Problem**: Pickle loading error  
**Solution**: Verify Python version matches training environment (3.11)

**Problem**: Model accuracy changed  
**Solution**: Retrain model, check for data distribution changes

### Git Issues

**Problem**: Merge conflicts  
**Solution**: `git pull`, resolve conflicts manually, `git commit`

**Problem**: Detached HEAD state  
**Solution**: `git checkout main`

**Problem**: Large files rejected  
**Solution**: Use `.gitignore` for large files, consider Git LFS

### Application Issues

**Problem**: Streamlit port already in use  
**Solution**: `streamlit run web_app.py --server.port 8502`

**Problem**: Tkinter not displaying  
**Solution**: Install tkinter: `brew install python-tk` (macOS)

**Problem**: Charts not rendering  
**Solution**: Ensure matplotlib is installed: `pip install matplotlib`

---

## Development Workflow

### Starting a New Session

1. Open terminal
2. Navigate to project: `cd ~/Downloads/guardian-shield`
3. Activate environment: `source venv/bin/activate`
4. Pull latest changes: `git pull`
5. Check status: `git status`
6. Begin work

### Ending a Session

1. Test all changes
2. Stage files: `git add .`
3. Commit: `git commit -m "Description"`
4. Push: `git push`
5. Deactivate environment: `deactivate`
6. Document progress in PROGRESS.md

### Best Practices

- Commit frequently with clear messages
- Test before pushing
- Update documentation alongside code
- Keep models in `saved_models/` directory
- Use descriptive variable names
- Add comments for complex logic
- Follow PEP 8 style guidelines

---

## Next Steps (Week 3+)

### Immediate Priorities

1. **Acquire proper malware/phishing image datasets**
   - Source from theZoo, VirusTotal, Kaggle
   - Minimum 10K malware + 15K phishing images
   - Organize into proper directory structure

2. **Retrain image classification model**
   - Use proper malware/phishing samples
   - Achieve >90% accuracy target
   - Convert to TensorFlow Lite

3. **Integrate all models in web application**
   - Add image upload functionality
   - Combine URL + QR + Image detection
   - Update UI for multi-model results

### Secondary Objectives

1. **Begin Android development**
   - Set up Android Studio
   - Create basic UI with Jetpack Compose
   - Integrate TensorFlow Lite models

2. **Implement testing suite**
   - Unit tests for models
   - Integration tests for applications
   - Performance benchmarks

3. **Create demonstration materials**
   - Record demo video
   - Prepare presentation slides
   - Write technical report

---

## Resources

### Documentation
- README.md: Project overview
- DEVELOPMENT_PLAN.md: 16-week roadmap
- PROGRESS.md: Current status
- SETUP_INSTRUCTIONS.md: Installation guide

### External Resources
- Kaggle Datasets: https://www.kaggle.com/datasets
- Streamlit Docs: https://docs.streamlit.io
- Scikit-learn Docs: https://scikit-learn.org/stable/
- TensorFlow Docs: https://www.tensorflow.org/

### Repository
- GitHub: https://github.com/Dileeppabbathi/guardian-shield
- Live Demo: https://guardian-shield-wsm3t93teo7alrauatsc3x.streamlit.app/
- Documentation: https://dileeppabbathi.github.io/guardian-shield/

---

## Contact and Support

For questions or issues:
1. Check documentation in this repository
2. Review TROUBLESHOOTING section above
3. Check commit history for recent changes
4. Refer to DEVELOPMENT_PLAN.md for roadmap

---

## Version History

- **v2.0** (January 27, 2026): Professional documentation update
- **v1.0** (January 24, 2026): Initial creation

---

**Document Version**: 2.0  
**Last Updated**: January 27, 2026  
**Maintained By**: Dileep Pabbathi
