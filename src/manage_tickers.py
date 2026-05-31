import csv
import os
from datetime import datetime

TICKERS_FILE = 'tickers.csv'
DATA_DIR = 'data'

def add_ticker(ticker, reason):
    """
    Adds a ticker to the tracking list and creates its data directory.
    """
    # Create directory for the ticker
    ticker_dir = os.path.join(DATA_DIR, ticker.upper())
    os.makedirs(ticker_dir, exist_ok=True)

    # Add to CSV
    date_added = datetime.now().strftime("%Y-%m-%d")

    # Check if file exists, if not write header
    file_exists = os.path.isfile(TICKERS_FILE)

    with open(TICKERS_FILE, mode='a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Ticker", "Reason", "Date Added"])
        writer.writerow([ticker.upper(), reason, date_added])

    print(f"Added ticker {ticker.upper()} and created directory {ticker_dir}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: python manage_tickers.py <TICKER> <REASON>")
        sys.exit(1)

    add_ticker(sys.argv[1], sys.argv[2])
