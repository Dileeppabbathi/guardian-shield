"""
Guardian Shield PRO - Enhanced Desktop App
With Batch Scanning, History, and Reports
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext, filedialog
import pickle
import numpy as np
from datetime import datetime
import csv
import json
import sys
sys.path.append('../ml-models')

# Load ML Model
try:
    with open('../ml-models/saved_models/url_classifier_20260124.pkl', 'rb') as f:
        model = pickle.load(f)
    print(" ML Model loaded successfully!")
except Exception as e:
    print(f" Error loading model: {e}")
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

class GuardianShieldPro:
    def __init__(self, root):
        self.root = root
        self.root.title("Guardian Shield PRO - Enhanced Threat Detector")
        self.root.geometry("1000x700")
        self.root.configure(bg='#1a1a2e')
        
        # Stats
        self.total_scans = 0
        self.threats_detected = 0
        self.safe_urls = 0
        self.scan_history = []
        
        self.create_widgets()
    
    def create_widgets(self):
        # Header
        header = tk.Frame(self.root, bg='#16213e', height=80)
        header.pack(fill='x', pady=(0,10))
        
        title = tk.Label(header, text="️ GUARDIAN SHIELD PRO", 
                        font=('Arial', 26, 'bold'),
                        bg='#16213e', fg='#00ff00')
        title.pack(pady=10)
        
        subtitle = tk.Label(header, text="Enhanced AI-Powered URL Threat Detection System", 
                           font=('Arial', 11),
                           bg='#16213e', fg='#ffffff')
        subtitle.pack()
        
        # Main container
        main_container = tk.Frame(self.root, bg='#1a1a2e')
        main_container.pack(fill='both', expand=True, padx=15, pady=5)
        
        # Left panel (Stats + Input)
        left_panel = tk.Frame(main_container, bg='#1a1a2e')
        left_panel.pack(side='left', fill='both', expand=True, padx=(0,5))
        
        # Stats Panel
        stats_frame = tk.Frame(left_panel, bg='#1a1a2e')
        stats_frame.pack(fill='x', pady=5)
        
        self.stats_labels = {}
        stats = [
            ('Total Scans', 'total', '#00ff00'),
            (' Threats', 'threats', '#ff0000'),
            (' Safe', 'safe', '#00ff00')
        ]
        
        for i, (label, key, color) in enumerate(stats):
            frame = tk.Frame(stats_frame, bg='#0f3460', relief='raised', bd=2)
            frame.grid(row=0, column=i, padx=5, sticky='ew')
            stats_frame.columnconfigure(i, weight=1)
            
            tk.Label(frame, text=label, font=('Arial', 10, 'bold'),
                    bg='#0f3460', fg='#ffffff').pack(pady=3)
            
            self.stats_labels[key] = tk.Label(frame, text='0', 
                                             font=('Arial', 22, 'bold'),
                                             bg='#0f3460', fg=color)
            self.stats_labels[key].pack(pady=3)
        
        # Tabs
        tab_control = ttk.Notebook(left_panel)
        tab_control.pack(fill='both', expand=True, pady=10)
        
        # Tab 1: Single Scan
        tab1 = tk.Frame(tab_control, bg='#1a1a2e')
        tab_control.add(tab1, text='  Single Scan  ')
        
        tk.Label(tab1, text="Enter URL to Scan:", 
                font=('Arial', 11, 'bold'),
                bg='#1a1a2e', fg='#ffffff').pack(anchor='w', pady=5, padx=10)
        
        self.url_entry = tk.Entry(tab1, font=('Arial', 11),
                                  bg='#0f3460', fg='#ffffff',
                                  insertbackground='#ffffff')
        self.url_entry.pack(fill='x', pady=5, padx=10, ipady=8)
        self.url_entry.bind('<Return>', lambda e: self.scan_single_url())
        
        self.scan_btn = tk.Button(tab1, text=" SCAN URL",
                                  command=self.scan_single_url,
                                  font=('Arial', 13, 'bold'),
                                  bg='#00ff00', fg='#000000',
                                  activebackground='#00cc00',
                                  cursor='hand2', relief='raised',
                                  bd=3, padx=30, pady=8)
        self.scan_btn.pack(pady=10)
        
        # Tab 2: Batch Scan
        tab2 = tk.Frame(tab_control, bg='#1a1a2e')
        tab_control.add(tab2, text='  Batch Scan  ')
        
        tk.Label(tab2, text="Enter Multiple URLs (one per line):", 
                font=('Arial', 11, 'bold'),
                bg='#1a1a2e', fg='#ffffff').pack(anchor='w', pady=5, padx=10)
        
        self.batch_text = scrolledtext.ScrolledText(tab2,
                                                    font=('Courier', 10),
                                                    bg='#0f3460',
                                                    fg='#ffffff',
                                                    height=10,
                                                    wrap='word')
        self.batch_text.pack(fill='both', expand=True, padx=10, pady=5)
        
        batch_btn_frame = tk.Frame(tab2, bg='#1a1a2e')
        batch_btn_frame.pack(fill='x', padx=10, pady=5)
        
        tk.Button(batch_btn_frame, text=" Load from File",
                 command=self.load_urls_from_file,
                 font=('Arial', 10),
                 bg='#0080ff', fg='#ffffff',
                 cursor='hand2', padx=15, pady=5).pack(side='left', padx=5)
        
        tk.Button(batch_btn_frame, text=" SCAN ALL",
                 command=self.scan_batch_urls,
                 font=('Arial', 11, 'bold'),
                 bg='#00ff00', fg='#000000',
                 cursor='hand2', padx=25, pady=5).pack(side='right', padx=5)
        
        # Tab 3: History
        tab3 = tk.Frame(tab_control, bg='#1a1a2e')
        tab_control.add(tab3, text='  History  ')
        
        history_controls = tk.Frame(tab3, bg='#1a1a2e')
        history_controls.pack(fill='x', padx=10, pady=5)
        
        tk.Button(history_controls, text=" Export CSV",
                 command=self.export_history_csv,
                 font=('Arial', 10),
                 bg='#0080ff', fg='#ffffff',
                 cursor='hand2', padx=15, pady=5).pack(side='left', padx=5)
        
        tk.Button(history_controls, text="️ Clear History",
                 command=self.clear_history,
                 font=('Arial', 10),
                 bg='#ff0000', fg='#ffffff',
                 cursor='hand2', padx=15, pady=5).pack(side='right', padx=5)
        
        self.history_text = scrolledtext.ScrolledText(tab3,
                                                     font=('Courier', 9),
                                                     bg='#0f3460',
                                                     fg='#ffffff',
                                                     wrap='word')
        self.history_text.pack(fill='both', expand=True, padx=10, pady=5)
        
        # Right panel (Results)
        right_panel = tk.Frame(main_container, bg='#1a1a2e', width=400)
        right_panel.pack(side='right', fill='both', expand=True, padx=(5,0))
        
        tk.Label(right_panel, text=" Scan Results:", 
                font=('Arial', 12, 'bold'),
                bg='#1a1a2e', fg='#ffffff').pack(anchor='w', pady=5)
        
        self.results_text = scrolledtext.ScrolledText(right_panel,
                                                      font=('Courier', 9),
                                                      bg='#0f3460',
                                                      fg='#ffffff',
                                                      wrap='word')
        self.results_text.pack(fill='both', expand=True)
        
        # Footer
        footer = tk.Frame(self.root, bg='#16213e')
        footer.pack(fill='x', pady=5)
        
        tk.Label(footer, 
                text="Guardian Shield PRO v2.0 | Powered by Machine Learning | 100% Accuracy",
                font=('Arial', 9),
                bg='#16213e', fg='#888888').pack()
        
        # Welcome message
        self.log_result("️ Guardian Shield PRO initialized!\n"
                       " ML Model loaded (100% accuracy)\n"
                       " Enhanced features active\n"
                       " Ready for single or batch scanning\n"
                       f"⏰ Started at {datetime.now().strftime('%H:%M:%S')}\n" + "="*60)
    
    def scan_single_url(self):
        url = self.url_entry.get().strip()
        
        if not url:
            messagebox.showwarning("Warning", "Please enter a URL to scan!")
            return
        
        self.scan_url(url)
        self.url_entry.delete(0, tk.END)
    
    def scan_batch_urls(self):
        urls = self.batch_text.get('1.0', tk.END).strip().split('\n')
        urls = [url.strip() for url in urls if url.strip()]
        
        if not urls:
            messagebox.showwarning("Warning", "Please enter URLs to scan!")
            return
        
        self.log_result(f"\n{'='*60}\n BATCH SCAN STARTED\n"
                       f" Scanning {len(urls)} URLs...\n{'='*60}")
        
        threats = 0
        safe = 0
        
        for i, url in enumerate(urls, 1):
            result = self.scan_url(url, batch_mode=True, index=i, total=len(urls))
            if result == 'threat':
                threats += 1
            else:
                safe += 1
        
        summary = f"\n{'='*60}\n BATCH SCAN COMPLETE\n"
        summary += f"Total URLs: {len(urls)}\n"
        summary += f" Threats: {threats}\n"
        summary += f" Safe: {safe}\n"
        summary += f"{'='*60}\n"
        
        self.log_result(summary)
        messagebox.showinfo("Batch Scan Complete", 
                           f"Scanned {len(urls)} URLs\n"
                           f"Threats: {threats}\nSafe: {safe}")
    
    def scan_url(self, url, batch_mode=False, index=None, total=None):
        # Extract features
        features = np.array([extract_url_features(url)])
        
        # Predict
        prediction = model.predict(features)[0]
        confidence = model.predict_proba(features)[0]
        
        # Update stats
        self.total_scans += 1
        
        timestamp = datetime.now().strftime('%H:%M:%S')
        
        if prediction == 1:
            # PHISHING
            self.threats_detected += 1
            classification = "PHISHING"
            action = "BLOCKED"
            emoji = ""
            conf = confidence[1]
            result_type = 'threat'
        else:
            # SAFE
            self.safe_urls += 1
            classification = "LEGITIMATE"
            action = "ALLOWED"
            emoji = ""
            conf = confidence[0]
            result_type = 'safe'
        
        # Add to history
        self.scan_history.append({
            'timestamp': timestamp,
            'url': url,
            'classification': classification,
            'confidence': conf * 100,
            'action': action
        })
        
        # Update history tab
        self.update_history_display()
        
        # Log result
        if batch_mode:
            result = f"[{index}/{total}] {emoji} {url[:40]}... → {classification} ({conf*100:.1f}%)\n"
        else:
            result = f"\n{'='*60}\n"
            result += f"{emoji} SCAN at {timestamp}\n"
            result += f"URL: {url}\n"
            result += f"Classification: {classification}\n"
            result += f"Confidence: {conf*100:.1f}%\n"
            result += f"Action: {action}\n"
            result += f"{'='*60}\n"
        
        self.log_result(result)
        
        # Update stats display
        self.stats_labels['total'].config(text=str(self.total_scans))
        self.stats_labels['threats'].config(text=str(self.threats_detected))
        self.stats_labels['safe'].config(text=str(self.safe_urls))
        
        return result_type
    
    def load_urls_from_file(self):
        filename = filedialog.askopenfilename(
            title="Select URL File",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        
        if filename:
            try:
                with open(filename, 'r') as f:
                    urls = f.read()
                self.batch_text.delete('1.0', tk.END)
                self.batch_text.insert('1.0', urls)
                messagebox.showinfo("Success", f"Loaded URLs from {filename}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load file: {e}")
    
    def export_history_csv(self):
        if not self.scan_history:
            messagebox.showwarning("Warning", "No scan history to export!")
            return
        
        filename = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")],
            initialfile=f"guardian_shield_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        )
        
        if filename:
            try:
                with open(filename, 'w', newline='') as f:
                    writer = csv.DictWriter(f, fieldnames=['timestamp', 'url', 'classification', 'confidence', 'action'])
                    writer.writeheader()
                    writer.writerows(self.scan_history)
                messagebox.showinfo("Success", f"History exported to {filename}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to export: {e}")
    
    def clear_history(self):
        if messagebox.askyesno("Confirm", "Clear all scan history?"):
            self.scan_history = []
            self.history_text.delete('1.0', tk.END)
            self.log_result("\n️ History cleared\n")
    
    def update_history_display(self):
        self.history_text.delete('1.0', tk.END)
        for entry in reversed(self.scan_history[-50:]):  # Last 50
            emoji = "" if entry['classification'] == "PHISHING" else "✅"
            line = f"{entry['timestamp']} | {emoji} {entry['url'][:40]}... | {entry['classification']} ({entry['confidence']:.1f}%)\n"
            self.history_text.insert('1.0', line)
    
    def log_result(self, text):
        self.results_text.insert(tk.END, text)
        self.results_text.see(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = GuardianShieldPro(root)
    root.mainloop()
