import yfinance as yf
import matplotlib.pyplot as plt
from helper import StockData, StockPlotter, RollingMeanPlotter, CrossoverPlotter

tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "NVDA", "TSLA"]

fig, axes = plt.subplots(2, 3, figsize=(15, 8))
axes = axes.flatten()

for i, ticker in enumerate(tickers):
    data = StockData(ticker)
    data.fetch(period='1y')
    CrossoverPlotter(data).plot(axes[i])

plt.tight_layout()
plt.savefig("signals.png", dpi=150)
plt.show()