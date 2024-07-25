import datetime
import time
from plyer import notification
import yfinance as yf

stock_tickers = ["TSLA", "AAPL", "GOOGL"]
while True:
    for stock_ticker in stock_tickers:
        stock = yf.Ticker(stock_ticker)
        data = stock.info

        notification.notify(
            title="{} DATA".format(stock_ticker),
            message="current price={cp}\n DayLow={dl}\n DayHigh={dh}".format(
                cp=data["currentPrice"],
                dl=data["regularMarketDayLow"],
                dh=data["regularMarketDayHigh"]
            ),
            app_icon="C:/Users/geeti/Downloads/notification_bell.ico",
            timeout=5
        )
        time.sleep(5)
    time.sleep(60 * 60 * 2)

