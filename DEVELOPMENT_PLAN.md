# Development Plan

## Guardian Shield: 16-Week Development Roadmap

**Project**: AI-Based Real-Time Threat Detection System  
**Duration**: 16 weeks  
**Status**: Week 2 of 16 complete

---

## Project Phases Overview

| Phase | Weeks | Focus Area | Status |
|-------|-------|-----------|--------|
| Phase 1 | 1-2 | Foundation & URL Detection | Complete |
| Phase 2 | 3-4 | Android MVP & Integration | Not Started |
| Phase 3 | 5-6 | Dataset Expansion | Not Started |
| Phase 4 | 7-8 | Image Detection ML | Not Started |
| Phase 5 | 9-10 | QR Code Detection | Complete |
| Phase 6 | 11-12 | System Integration | Not Started |
| Phase 7 | 13-14 | Testing & Optimization | Not Started |
| Phase 8 | 15-16 | Deployment & Documentation | Not Started |

---

## Phase 1: Foundation & URL Detection (Week 1-2)

### Objectives
- Establish project infrastructure
- Collect and prepare URL dataset
- Train URL classification model
- Develop initial applications

### Deliverables
- [x] GitHub repository with version control
- [x] Project documentation structure
- [x] URL dataset (651,199 samples)
- [x] Trained URL classifier (89.59% accuracy)
- [x] Three desktop applications
- [x] Web application deployment
- [x] QR code classifier (85.50% accuracy)

### Status: Complete (150% of objectives)

---

## Phase 2: Android MVP (Week 3-4)

### Objectives
- Set up Android development environment
- Implement basic Android application
- Integrate URL classification model
- Develop notification monitoring

### Tasks

**Week 3: Environment Setup**
- Install Android Studio
- Configure Kotlin development environment
- Create project structure with Jetpack Compose
- Set up Room database
- Implement basic UI components

**Week 4: Core Functionality**
- Integrate TensorFlow Lite models
- Implement notification listener service
- Create threat detection pipeline
- Add warning dialog system
- Implement basic settings

### Deliverables
- [ ] Android Studio project setup
- [ ] Basic UI with threat scanning
- [ ] Notification monitoring service
- [ ] TensorFlow Lite model integration
- [ ] Local threat database

### Dependencies
- Completed URL model (Phase 1)
- Android development knowledge
- TensorFlow Lite conversion

---

## Phase 3: Dataset Expansion (Week 5-6)

### Objectives
- Collect comprehensive image datasets
- Acquire malware samples
- Gather phishing screenshots
- Organize and label data

### Data Collection Strategy

**Malware Images** (Target: 10,000)
- Sources: theZoo, VirusTotal, Kaggle
- Categories: Ransomware screens, fake alerts, system warnings
- Format: PNG, JPG
- Size: ~3 GB

**Phishing Images** (Target: 15,000)
- Sources: PhishTank, OpenPhish, research datasets
- Categories: Fake login pages, credential harvesting
- Format: Screenshots
- Size: ~2 GB

**Legitimate Images** (Target: 20,000)
- Sources: ImageNet, COCO, Common Crawl
- Categories: Normal screenshots, legitimate websites
- Format: Various
- Size: ~8 GB

### Deliverables
- [ ] Malware image dataset (10,000 samples)
- [ ] Phishing image dataset (15,000 samples)
- [ ] Legitimate image dataset (20,000 samples)
- [ ] Data labeling completed
- [ ] Train/test split (80/20)

### Quality Assurance
- Manual verification of samples
- Removal of duplicates
- Balanced class distribution
- Proper metadata documentation

---

## Phase 4: Image Detection ML (Week 7-8)

### Objectives
- Implement transfer learning pipeline
- Train image classification model
- Integrate OCR capabilities
- Optimize for mobile deployment

### Technical Approach

**Model Architecture**
- Base: MobileNetV2 (pre-trained on ImageNet)
- Custom layers: 2 dense layers with dropout
- Output: 3 classes (safe, phishing, malware)
- Optimization: TensorFlow Lite quantization

**Training Strategy**
- Batch size: 32
- Epochs: 15-20
- Learning rate: 0.001 with decay
- Augmentation: Rotation, flip, zoom, shift
- Early stopping: Patience 3 epochs

**OCR Integration**
- Library: Tesseract or EasyOCR
- Purpose: Extract text from images
- Processing: DistilBERT for text classification
- Use case: Detect suspicious phrases

### Deliverables
- [ ] Trained image classifier (>90% accuracy target)
- [ ] TensorFlow Lite model (<50 MB)
- [ ] OCR text extraction pipeline
- [ ] Text classification model
- [ ] Performance benchmarks

### Success Metrics
- Accuracy: >90%
- False positive rate: <5%
- Inference time: <2 seconds
- Model size: <50 MB

---

## Phase 5: QR Code Detection (Week 9-10)

### Status: Complete

### Achieved Objectives
- [x] QR code generation from URL dataset
- [x] Feature extraction pipeline
- [x] Random Forest classifier training
- [x] Model evaluation and validation
- [x] 85.50% test accuracy achieved

### Technical Implementation
- Dataset: 2,000 QR codes (50% benign, 50% malicious)
- Features: 8 (image statistics + URL features)
- Algorithm: Random Forest (100 estimators)
- Training time: 10 minutes

---

## Phase 6: System Integration (Week 11-12)

### Objectives
- Combine all detection models
- Create unified threat detection pipeline
- Implement Android application UI
- Add background monitoring

### Integration Architecture
```
User Input (URL/Image/QR)
         |
         v
   Input Router
         |
    /----+----\
   /     |     \
  v      v      v
URL    Image    QR
Model  Model   Model
  \     |      /
   \----+-----/
         |
         v
  Threat Aggregator
         |
         v
    User Warning
```

### Android Application Features
- Real-time notification scanning
- Manual URL/QR scanning
- Image upload analysis
- Threat history
- Whitelist management
- Settings and preferences

### Deliverables
- [ ] Unified detection pipeline
- [ ] Complete Android UI
- [ ] Background service implementation
- [ ] Database integration
- [ ] Settings management
- [ ] Help and documentation

---

## Phase 7: Testing & Optimization (Week 13-14)

### Objectives
- Comprehensive testing across all modules
- Performance optimization
- Bug fixing and refinement
- User experience improvements

### Testing Strategy

**Unit Testing**
- Model inference functions
- Feature extraction
- Database operations
- API integrations

**Integration Testing**
- End-to-end detection pipeline
- Multi-model coordination
- Notification monitoring
- Background services

**Performance Testing**
- Battery consumption analysis
- Memory usage profiling
- Network efficiency
- Model inference speed

**User Acceptance Testing**
- Real-world usage scenarios
- False positive analysis
- User interface feedback
- Edge case handling

### Optimization Targets
- Battery impact: <5% additional drain
- Memory footprint: <100 MB
- Startup time: <2 seconds
- Detection latency: <1 second

### Deliverables
- [ ] Test suite with >80% coverage
- [ ] Performance benchmarks
- [ ] Bug fixes implemented
- [ ] Optimization improvements
- [ ] Testing documentation

---

## Phase 8: Deployment & Documentation (Week 15-16)

### Objectives
- Final deployment preparation
- Comprehensive documentation
- Demonstration materials
- Research paper preparation

### Deployment Checklist
- [ ] Google Play Store submission preparation
- [ ] Privacy policy and terms of service
- [ ] App store assets (screenshots, description)
- [ ] Beta testing program
- [ ] Monitoring and analytics setup

### Documentation Deliverables
- [ ] User manual
- [ ] Developer documentation
- [ ] API documentation (if applicable)
- [ ] Architecture diagrams
- [ ] Deployment guide
- [ ] Troubleshooting guide

### Academic Deliverables
- [ ] Technical report (20+ pages)
- [ ] Research paper draft
- [ ] Presentation slides
- [ ] Demonstration video (5-10 minutes)
- [ ] Project poster

### Final Presentation
- [ ] Live demonstration
- [ ] Performance metrics showcase
- [ ] Code walkthrough
- [ ] Q&A preparation

---

## Technology Stack

### Programming Languages
- Python 3.11 (ML development, backend)
- Kotlin (Android application)
- Java (Android framework compatibility)

### Machine Learning
- Scikit-learn 1.3.2 (Random Forest)
- TensorFlow 2.15.0 (Deep learning)
- PyTorch 2.1.2 (Alternative framework)
- TensorFlow Lite (Mobile deployment)

### Computer Vision & OCR
- OpenCV 4.9.0 (Image processing)
- Tesseract/EasyOCR (Text extraction)
- Pillow 10.1.0 (Image manipulation)
- ZXing (QR code processing)

### Android Development
- Android Studio (IDE)
- Jetpack Compose (UI framework)
- Room Database (Local storage)
- CameraX (Camera integration)
- ML Kit (ML SDK)
- WorkManager (Background tasks)
- Hilt (Dependency injection)

### Web Development
- Streamlit (Web application)
- HTML/CSS/JavaScript (GitHub Pages)

### Data & Visualization
- Pandas 2.1.4 (Data manipulation)
- NumPy 1.24.3 (Numerical computing)
- Matplotlib 3.8.2 (Visualization)
- Plotly (Interactive charts)

### Development Tools
- Git/GitHub (Version control)
- Jupyter Notebook (Experimentation)
- pytest (Testing framework)
- Black (Code formatting)

---

## Risk Management

### Technical Risks

**Risk 1: Model Performance**
- Impact: High
- Probability: Medium
- Mitigation: Extensive testing, multiple model architectures
- Contingency: Ensemble methods, hybrid approaches

**Risk 2: Mobile Performance**
- Impact: Medium
- Probability: Medium
- Mitigation: TensorFlow Lite optimization, profiling
- Contingency: Cloud-based inference option

**Risk 3: Dataset Quality**
- Impact: High
- Probability: Low
- Mitigation: Multiple data sources, validation
- Contingency: Data augmentation, synthetic data

### Resource Risks

**Risk 4: Development Time**
- Impact: Medium
- Probability: Medium
- Mitigation: Agile methodology, weekly milestones
- Contingency: Scope reduction, phase prioritization

**Risk 5: Storage Limitations**
- Impact: Low
- Probability: Low
- Mitigation: Regular cleanup, cloud storage
- Contingency: External storage, compression

---

## Success Criteria

### Technical Success
- [ ] URL detection accuracy >85%
- [ ] QR detection accuracy >80%
- [ ] Image detection accuracy >90%
- [ ] Mobile app operational
- [ ] All components integrated

### Academic Success
- [ ] Complete documentation
- [ ] Research paper drafted
- [ ] Successful demonstration
- [ ] Grade: A or higher
- [ ] Publication potential

### Personal Success
- [ ] Portfolio-worthy project
- [ ] Industry-relevant skills
- [ ] Open-source contribution
- [ ] Professional networking

---

## Budget and Resources

### Financial Resources
- Development: $0 (open-source tools)
- Deployment: $0 (free tier services)
- Data: $0 (public datasets)
- Total: $0

### Time Resources
- Total estimated: 160 hours (16 weeks × 10 hours/week)
- Completed: 16 hours (Week 1-2)
- Remaining: 144 hours

### Computational Resources
- Development machine: MacBook Air M1
- Cloud services: Streamlit Cloud (free tier)
- Storage: GitHub (unlimited public repos)

---

## Conclusion

This development plan provides a comprehensive roadmap for completing Guardian Shield over 16 weeks. Phase 1 has been completed successfully with all objectives met. The plan remains flexible to accommodate challenges and opportunities as they arise.

---

**Document Version**: 2.0  
**Author**: Dileep Pabbathi  
**Last Updated**: January 27, 2026  
**Next Review**: Week 3
