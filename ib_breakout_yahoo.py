
"""
Initial Balance Breakout Strategy (Yahoo Finance Prototype)

This script fetches 5-minute intraday OHLC data for a selected stock symbol
(using the yfinance library) for a given date range. It calculates the Initial
Balance (9:30–10:30 AM ET) and scans for the first breakout — a closing price
that occurs above or below the initial range — during the rest of the trading day.

This logic is built to be fully portable to Alpaca's live API and bar format.
"""




import pandas as pd

import pytz
import yfinance as yf
from datetime import datetime

# --- Step 1: Get the symbol from the user ---
symbol = input("Enter a stock symbol (e.g., SPY, TSLA, QQQ): ").upper()

# --- Step 2: Use a known trading day to avoid "no data" errors ---
# We're using Saturday as the "end" so we capture all of Friday
start_date = "2025-04-11"
end_date = "2025-04-12"

# --- Step 3: Fetch 5-minute OHLC bars from yfinance ---
# auto_adjust=False gives raw, unadjusted prices (important for intraday strategies)
print(f"\nFetching 5-minute OHLC bars for {symbol} on {start_date}...")

data = yf.download(
    tickers=symbol,
    start=start_date,
    end=end_date,
    interval="5m",
    progress=False,
    auto_adjust=False,
    group_by="ticker"  # ✅ Forces OHLC inside ticker
)

# Convert the index from UTC to Eastern Time
data.index = data.index.tz_convert('US/Eastern')

# Flatten to get just 'Open', 'High', etc.
if isinstance(data.columns, pd.MultiIndex):
    data = data[symbol]  # ✅ Just grab the nested block under 'SPY'




# --- Step 4: Trim to only OHLC and show preview ---
if data.empty:
    print("❌ No data returned. Double-check the symbol and ensure the market was open.")
else:
#    print("Columns in DataFrame:", data.columns)  # 🔍 See what's actually there
    ohlc = data[["Open", "High", "Low", "Close"]]
    print(f"✅ Fetched {len(ohlc)} OHLC bars.\n")
    print(ohlc.head(12))

# --- Step 5: Extract 9:30–10:30 for Initial Balance (IB) ---
ib_start = datetime.strptime("09:30", "%H:%M").time()
ib_end = datetime.strptime("10:30", "%H:%M").time()

# Filter the rows within the IB time range
ib_data = data.between_time(ib_start, ib_end)

if ib_data.empty:
    print("❌ No Initial Balance data found.")
else:
    ib_high = ib_data["High"].max()
    ib_low = ib_data["Low"].min()
#    ib_high = ib_data["High"].max().values[0]
#    ib_low = ib_data["Low"].min().values[0]

    print("\n🔍 Initial Balance (9:30–10:30 ET):")
    print(f"High : {ib_high:.2f}")
    print(f"Low  : {ib_low:.2f}")
    print(f"Range: {(ib_high - ib_low):.2f}")

# --- Step 6: Check for breakout close after 10:30 AM ---
print("\n📈 Scanning for breakouts after 10:30 AM...")

after_ib_data = ohlc.between_time("10:30", "16:00")

for timestamp, row in after_ib_data.iterrows():
    close = row["Close"]

    if close > ib_high:
        print(f"📍 Breakout ABOVE at {timestamp.strftime('%H:%M')} — Close: {close:.2f}")
        break
    elif close < ib_low:
        print(f"📍 Breakout BELOW at {timestamp.strftime('%H:%M')} — Close: {close:.2f}")
        break
else:
    print("🟨 No IB breakout occurred.")
