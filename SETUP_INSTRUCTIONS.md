# Guardian Shield - Complete Setup Instructions

## Prerequisites

### Required Software
- **Android Studio**: Hedgehog (2023.1.1) or later
- **Python**: 3.8 or later
- **Git**: Latest version
- **JDK**: 17 (comes with Android Studio)

### Required Accounts
- **GitHub Account**: For version control
- **Google Account**: For Safe Browsing API key

---

## Step-by-Step Setup

### 1. Clone Repository
```bash
git clone https://github.com/Dileeppabbathi/guardian-shield.git
cd guardian-shield
```

### 2. Setup Python Environment
```bash
# Create virtual environment
python3 -m venv venv

# Activate (macOS/Linux)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate

# Install dependencies
pip install --upgrade pip
pip install -r ml-models/requirements.txt
```

### 3. Collect Training Data
```bash
cd scripts/data_collection

# Collect phishing URLs
python3 collect_urls.py

# Collect legitimate URLs
python3 collect_legitimate_urls.py
python3 collect_more_urls.py

cd ../..
```

### 4. Setup Android Studio

1. **Download Android Studio**
   - Visit: https://developer.android.com/studio
   - Download and install

2. **Install Android SDK**
   - Open Android Studio
   - Go to: Tools → SDK Manager
   - Install: Android 14.0 (API 34)

3. **Open Project**
   - File → Open
   - Navigate to: `guardian-shield/android-app`
   - Click OK
   - Wait for Gradle sync (5-10 minutes first time)

### 5. Get API Keys

#### Google Safe Browsing API

1. Go to: https://console.cloud.google.com
2. Create new project: "Guardian Shield"
3. Enable: Safe Browsing API
4. Create credentials: API Key
5. Copy API key

6. Add to project:
```bash
echo "SAFE_BROWSING_API_KEY=your_key_here" > android-app/local.properties
```

### 6. Build Android App
```bash
cd android-app
./gradlew build
```

Or in Android Studio:
- Build → Make Project
- Run → Run 'app'

---

## Verification

### Test Python Setup
```bash
python3 -c "import tensorflow, torch, sklearn; print('All packages installed!')"
```

### Test Data Collection
```bash
ls -lh datasets/*/*.csv
```

### Test Android Build
- Should see: BUILD SUCCESSFUL
- APK location: `app/build/outputs/apk/`

---

## Troubleshooting

### Python Issues
```bash
# If packages fail to install
pip install --upgrade pip setuptools wheel
pip install -r ml-models/requirements.txt --no-cache-dir
```

### Android Studio Issues
- **Gradle sync failed**: File → Invalidate Caches → Invalidate and Restart
- **SDK not found**: Tools → SDK Manager → Install Android 14.0
- **Build errors**: Build → Clean Project, then Build → Rebuild Project

### API Key Issues
- Ensure key is in `local.properties`
- Check API is enabled in Google Console
- Verify billing is enabled (free tier available)

---

## Next Steps

After setup:
1. Review DEVELOPMENT_PLAN.md for weekly tasks
2. Start with Week 3: Android MVP development
3. Follow QUICK_START.md for immediate next actions

---

## Support

- **Documentation**: Check all .md files in project root
- **Issues**: Open issue on GitHub
- **Updates**: Pull latest changes regularly

**Setup completed!** Ready to start development! 🚀
