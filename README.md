# Initial Balance Breakout Strategy (Alpaca-Compatible)

This project implements a time-based breakout strategy using 5-minute intraday bars, built with full compatibility in mind for Alpaca’s API. The core logic identifies when price breaks above or below the **Initial Balance** range (9:30–10:30 AM ET) and flags the first valid breakout of the session.

> This project is being developed as part of my application to Alpaca. The logic is fully portable to Alpaca’s bar format, and integration is already underway. The breakout engine is modular, scalable, and easily integrated into a live Alpaca account for further development or execution.

 ⚠️ **Note:** All trading logic and integration was built using Alpaca’s **Paper API** and simulated live structure.  
> Due to current regional restrictions (**Canada**), live account functionality could not be **enabled**.

---

## 🚀 Features

- Calculates the Initial Balance (IB) from 5-minute bars
- Detects and timestamps the first breakout (above or below the IB)
- Uses `yfinance` for prototyping due to paper API data limitations
- Includes working connection test to Alpaca's live API

---

## 📁 Project Structure

```
alpaca/
├── ib_breakout_yahoo.py       # Working breakout prototype using yfinance
├── alpaca_check_balance.py    # Connects to Alpaca API and prints account status
├── check_feed.py              # Tests market data feed functionality
├── config_sample.yaml         # Safe example config file for API keys
├── requirements.txt           # All dependencies for this project
└── README.md                  # Project overview and usage instructions
```

---

## 🔐 API Credentials Setup

To run this project:

1. Copy the file named `config_sample.yaml`
2. Rename it to `config.yaml`
3. Paste in your actual Alpaca API Key ID and Secret Key

This file is used by scripts like `alpaca_check_balance.py` and should not be committed to version control.

---

## 📦 Installation

Install required Python packages with:

```bash
pip install -r requirements.txt