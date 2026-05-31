# Stock Research Tracker

This repository is designed to help organize and streamline stock research.

## Features & Workflow

1. **Save Interesting Tickers**: Track tickers you find interesting (due to low value, momentum, compelling story, etc.) in `tickers.csv`.
2. **Organize Raw Data**: Save source documents such as 10-K filings, earnings transcripts, and investor presentations in ticker-specific folders under `data/`.
3. **Extract Data**: Use automated scripts in `src/` to pull key data from the saved documents.
4. **Analyze and Report**: Synthesize the extracted information into reports saved in `reports/`.

## Directory Structure

```
.
├── data/                  # Raw data (10-Ks, presentations) organized by ticker
├── reports/               # Final generated analysis reports
├── src/                   # Python scripts for tracking, extracting, and analyzing data
│   ├── manage_tickers.py
│   ├── extract_data.py
│   └── analyze_report.py
└── tickers.csv            # Master list of tracked tickers
```

## Getting Started

To add a new ticker to your tracking list:
```bash
python src/manage_tickers.py AAPL "Strong momentum and services growth"
```
This will append AAPL to `tickers.csv` and create `data/AAPL/` where you can drop their 10-K and presentations.

Extract data:
```bash
python src/extract_data.py AAPL
```

Generate a report:
```bash
python src/analyze_report.py AAPL
```
