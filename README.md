# Initial Balance Breakout Strategy (Alpaca-Compatible)

This project implements a time-based breakout strategy using 5-minute intraday bars, built with full compatibility in mind for Alpaca’s API. The core logic identifies when price breaks above or below the **Initial Balance** range (9:30–10:30 AM ET) and flags the first valid breakout of the session.

> This project is being developed as part of my application to Alpaca. The logic is fully portable to Alpaca’s bar format, and integration is already underway. The breakout engine is modular, scalable, and easily integrated into a live Alpaca account for further development or execution.

---

## 🚀 Features

- Calculates the Initial Balance (IB) from 5-minute bars
- Detects and timestamps the first breakout (above or below the IB)
- Uses `yfinance` for prototyping due to paper API data limitations
- Includes working connection test to Alpaca's live API

---

## 📁 Project Structure

alpaca/ ├── ib_breakout_yahoo.py # Working breakout prototype using yfinance ├── check_balance.py # Connects to Alpaca API and prints account status ├── check_feed.py # Tests market data feed functionality ├── config.yaml # Placeholder for API keys (used with check_balance.py) ├── requirements.txt # All dependencies for this project └── README.md # Project overview and usage instructions


---

## 📦 Installation

Install required Python packages with:

```bash
pip install -r requirements.txt