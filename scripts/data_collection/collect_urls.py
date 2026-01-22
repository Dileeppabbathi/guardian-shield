"""
Simple URL Data Collector for Guardian Shield
Collects phishing URLs from public sources
"""

import requests
import csv
from datetime import datetime

def collect_phishing_urls():
    """Collect URLs from OpenPhish"""
    print("Collecting phishing URLs from OpenPhish...")
    
    try:
        url = "https://openphish.com/feed.txt"
        response = requests.get(url, timeout=30)
        
        if response.status_code == 200:
            urls = response.text.strip().split('\n')
            
            # Save to CSV
            filename = f'../../datasets/phishing_urls/openphish_{datetime.now().strftime("%Y%m%d")}.csv'
            
            with open(filename, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['url', 'source', 'date', 'label'])
                
                for url in urls[:1000]:
                    writer.writerow([url, 'OpenPhish', datetime.now().strftime("%Y-%m-%d"), 'phishing'])
            
            print(f"Collected {len(urls[:1000])} URLs")
            print(f"Saved to: {filename}")
        else:
            print(f"Error: HTTP {response.status_code}")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    collect_phishing_urls()
