def extract_10k_data(ticker):
    """
    Extracts relevant financial data from 10-K documents for a given ticker.
    Placeholder for future implementation.
    """
    print(f"Extracting 10-K data for {ticker}...")
    pass

def extract_presentation_data(ticker):
    """
    Extracts insights from investor presentations for a given ticker.
    Placeholder for future implementation.
    """
    print(f"Extracting presentation data for {ticker}...")
    pass

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python extract_data.py <TICKER>")
        sys.exit(1)

    ticker = sys.argv[1].upper()
    extract_10k_data(ticker)
    extract_presentation_data(ticker)
