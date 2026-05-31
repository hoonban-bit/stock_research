import os

REPORTS_DIR = 'reports'

def generate_report(ticker):
    """
    Analyzes extracted data and generates a final markdown report for the ticker.
    Placeholder for future implementation.
    """
    os.makedirs(REPORTS_DIR, exist_ok=True)
    report_path = os.path.join(REPORTS_DIR, f"{ticker}_report.md")

    content = f"# Stock Analysis Report: {ticker}\n\n## Overview\n\n## Financials (10-K)\n\n## Strategic Insights (Presentations)\n\n## Conclusion\n"

    with open(report_path, 'w') as f:
        f.write(content)

    print(f"Generated report at {report_path}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python analyze_report.py <TICKER>")
        sys.exit(1)

    ticker = sys.argv[1].upper()
    generate_report(ticker)
