import csv
import os
from datetime import datetime

WATCHLISTS_DIR = 'watchlists'
DATA_DIR = 'data'

def add_ticker(watchlist_name, ticker, reason):
    """
    Adds a ticker to the tracking list and creates its data directory.
    """
    # Ensure watchlists directory exists
    os.makedirs(WATCHLISTS_DIR, exist_ok=True)

    # Create directory for the ticker
    ticker_dir = os.path.join(DATA_DIR, ticker.upper())
    os.makedirs(ticker_dir, exist_ok=True)

    # Add to CSV
    date_added = datetime.now().strftime("%Y-%m-%d")

    csv_file = os.path.join(WATCHLISTS_DIR, f"{watchlist_name}.csv")
    file_exists = os.path.isfile(csv_file)

    with open(csv_file, mode='a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Ticker", "Reason", "Date Added"])
        writer.writerow([ticker.upper(), reason, date_added])

    print(f"Added ticker {ticker.upper()} to {csv_file} and created directory {ticker_dir}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 4:
        print("Usage: python manage_tickers.py <WATCHLIST_NAME> <TICKER> <REASON>")
        sys.exit(1)

    add_ticker(sys.argv[1], sys.argv[2], sys.argv[3])
