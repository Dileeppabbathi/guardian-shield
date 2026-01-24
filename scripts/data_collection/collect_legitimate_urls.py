import csv
from datetime import datetime

def collect_legitimate_urls():
    print("Collecting legitimate URLs...")
    
    legitimate_urls = [
        "https://www.bbc.com", "https://www.cnn.com", "https://www.nytimes.com",
        "https://www.apple.com", "https://www.microsoft.com", "https://www.google.com",
        "https://www.amazon.com", "https://www.netflix.com", "https://www.github.com",
        "https://www.facebook.com", "https://www.twitter.com", "https://www.instagram.com",
        "https://www.wikipedia.org", "https://www.mit.edu", "https://www.stanford.edu",
        "https://www.ebay.com", "https://www.walmart.com", "https://www.paypal.com",
    ]
    
    filename = f'../../datasets/legitimate_urls/legitimate_{datetime.now().strftime("%Y%m%d")}.csv'
    
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['url', 'source', 'date', 'label'])
        for url in legitimate_urls:
            writer.writerow([url, 'Manual', datetime.now().strftime("%Y-%m-%d"), 'legitimate'])
    
    print(f"Collected {len(legitimate_urls)} legitimate URLs")
    print(f"Saved to: {filename}")

if __name__ == "__main__":
    collect_legitimate_urls()
