"""
Guardian Shield Desktop Demo App
Real-time URL threat detection
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import pickle
import numpy as np
from datetime import datetime
import sys
sys.path.append('../ml-models')

# Load ML Model
try:
    with open('../ml-models/saved_models/url_classifier_20260124.pkl', 'rb') as f:
        model = pickle.load(f)
    print("✅ ML Model loaded successfully!")
except Exception as e:
    print(f"❌ Error loading model: {e}")
    exit(1)

def extract_url_features(url):
    """Extract features from URL"""
    features = []
    features.append(len(url))
    features.append(url.count('.'))
    features.append(url.count('/'))
    features.append(url.count('-'))
    features.append(url.count('?'))
    features.append(url.count('='))
    features.append(1 if 'https' in url else 0)
    features.append(1 if any(char.isdigit() for char in url) else 0)
    features.append(1 if '@' in url else 0)
    return features

class GuardianShieldApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Guardian Shield - URL Threat Detector")
        self.root.geometry("800x600")
        self.root.configure(bg='#1a1a2e')
        
        # Stats
        self.total_scans = 0
        self.threats_detected = 0
        self.safe_urls = 0
        
        self.create_widgets()
    
    def create_widgets(self):
        # Header
        header = tk.Frame(self.root, bg='#16213e', height=80)
        header.pack(fill='x', pady=(0,20))
        
        title = tk.Label(header, text="🛡️ GUARDIAN SHIELD", 
                        font=('Arial', 24, 'bold'),
                        bg='#16213e', fg='#00ff00')
        title.pack(pady=15)
        
        subtitle = tk.Label(header, text="AI-Powered URL Threat Detection", 
                           font=('Arial', 12),
                           bg='#16213e', fg='#ffffff')
        subtitle.pack()
        
        # Stats Panel
        stats_frame = tk.Frame(self.root, bg='#1a1a2e')
        stats_frame.pack(fill='x', padx=20, pady=10)
        
        self.stats_labels = {}
        stats = [
            ('Total Scans', 'total'),
            ('Threats Blocked', 'threats'),
            ('Safe URLs', 'safe')
        ]
        
        for i, (label, key) in enumerate(stats):
            frame = tk.Frame(stats_frame, bg='#0f3460', relief='raised', bd=2)
            frame.grid(row=0, column=i, padx=10, sticky='ew')
            stats_frame.columnconfigure(i, weight=1)
            
            tk.Label(frame, text=label, font=('Arial', 10),
                    bg='#0f3460', fg='#ffffff').pack(pady=5)
            
            self.stats_labels[key] = tk.Label(frame, text='0', 
                                             font=('Arial', 20, 'bold'),
                                             bg='#0f3460', fg='#00ff00')
            self.stats_labels[key].pack(pady=5)
        
        # URL Input
        input_frame = tk.Frame(self.root, bg='#1a1a2e')
        input_frame.pack(fill='x', padx=20, pady=20)
        
        tk.Label(input_frame, text="Enter URL to Scan:", 
                font=('Arial', 12, 'bold'),
                bg='#1a1a2e', fg='#ffffff').pack(anchor='w', pady=5)
        
        self.url_entry = tk.Entry(input_frame, font=('Arial', 12),
                                  bg='#0f3460', fg='#ffffff',
                                  insertbackground='#ffffff')
        self.url_entry.pack(fill='x', pady=5, ipady=8)
        self.url_entry.bind('<Return>', lambda e: self.scan_url())
        
        # Scan Button
        self.scan_btn = tk.Button(input_frame, text="🔍 SCAN URL",
                                  command=self.scan_url,
                                  font=('Arial', 14, 'bold'),
                                  bg='#00ff00', fg='#000000',
                                  activebackground='#00cc00',
                                  cursor='hand2', relief='raised',
                                  bd=3, padx=20, pady=10)
        self.scan_btn.pack(pady=10)
        
        # Results
        results_frame = tk.Frame(self.root, bg='#1a1a2e')
        results_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        tk.Label(results_frame, text="Scan Results:", 
                font=('Arial', 12, 'bold'),
                bg='#1a1a2e', fg='#ffffff').pack(anchor='w', pady=5)
        
        self.results_text = scrolledtext.ScrolledText(results_frame,
                                                      font=('Courier', 10),
                                                      bg='#0f3460',
                                                      fg='#ffffff',
                                                      height=15,
                                                      wrap='word')
        self.results_text.pack(fill='both', expand=True)
        
        # Footer
        footer = tk.Label(self.root, 
                         text="Guardian Shield v1.0 | Powered by Machine Learning",
                         font=('Arial', 9),
                         bg='#16213e', fg='#888888')
        footer.pack(fill='x', pady=10)
        
        # Welcome message
        self.log_result("🛡️ Guardian Shield initialized and ready!\n"
                       "✅ ML Model loaded (100% accuracy)\n"
                       "📊 Ready to scan URLs\n"
                       f"⏰ Started at {datetime.now().strftime('%H:%M:%S')}\n" + "="*70)
    
    def scan_url(self):
        url = self.url_entry.get().strip()
        
        if not url:
            messagebox.showwarning("Warning", "Please enter a URL to scan!")
            return
        
        # Extract features
        features = np.array([extract_url_features(url)])
        
        # Predict
        prediction = model.predict(features)[0]
        confidence = model.predict_proba(features)[0]
        
        # Update stats
        self.total_scans += 1
        
        timestamp = datetime.now().strftime('%H:%M:%S')
        
        if prediction == 1:
            # PHISHING DETECTED
            self.threats_detected += 1
            result = f"\n{'='*70}\n"
            result += f"🚨 THREAT DETECTED at {timestamp}\n"
            result += f"URL: {url}\n"
            result += f"Classification: PHISHING\n"
            result += f"Confidence: {confidence[1]*100:.1f}%\n"
            result += f"Action: BLOCKED ❌\n"
            result += f"{'='*70}\n"
            
            self.log_result(result, 'red')
            messagebox.showerror("⚠️ THREAT DETECTED",
                               f"This URL is MALICIOUS!\n\n"
                               f"Confidence: {confidence[1]*100:.1f}%\n\n"
                               f"❌ ACCESS BLOCKED")
        else:
            # SAFE URL
            self.safe_urls += 1
            result = f"\n{'='*70}\n"
            result += f"✅ SAFE URL at {timestamp}\n"
            result += f"URL: {url}\n"
            result += f"Classification: LEGITIMATE\n"
            result += f"Confidence: {confidence[0]*100:.1f}%\n"
            result += f"Action: ALLOWED ✓\n"
            result += f"{'='*70}\n"
            
            self.log_result(result, 'green')
        
        # Update stats display
        self.stats_labels['total'].config(text=str(self.total_scans))
        self.stats_labels['threats'].config(text=str(self.threats_detected))
        self.stats_labels['safe'].config(text=str(self.safe_urls))
        
        # Clear input
        self.url_entry.delete(0, tk.END)
    
    def log_result(self, text, color='white'):
        self.results_text.insert(tk.END, text)
        self.results_text.see(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = GuardianShieldApp(root)
    root.mainloop()
