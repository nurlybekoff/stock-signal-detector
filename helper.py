
import yfinance as yf
import matplotlib.pyplot as plt

class StockData:

    def __init__(self, ticker):
        self.ticker = ticker
        self.df = None
        self.crossover_points = None

    def fetch(self, period):
        # download stock data using yfinance
        df = yf.download(self.ticker, period=period)
        # flatten the multi-level columns
        df.columns = df.columns.get_level_values(0)

        # computea rolling means
        df['roll_7'] = df['Close'].rolling(7).mean()
        df['roll_30'] = df['Close'].rolling(30).mean()

        # detects crossovers between the 7-day and 30-day moving averages
        df['signal'] = df['roll_7'] > df['roll_30']
        df['crossover'] = df['signal'].astype(int).diff().abs()

        self.df = df
        self.crossover_points = df[df['crossover'] == 1]


class StockPlotter:
    
    def __init__(self, stock_data):
        self.stock_data = stock_data

    def plot(self, ax):
        # draw just the Close price
        df = self.stock_data.df
        ax.plot(df.index, df['Close'], label='Close', alpha=0.5)
        ax.legend(fontsize=8)
        ax.set_title(f"{self.stock_data.ticker} Stock Price")
        pass

class RollingMeanPlotter(StockPlotter):
    
    def plot(self, ax):
        super().plot(ax)
        # draw just the Close price
        df = self.stock_data.df
        ax.plot(df.index, df['roll_7'], label='7-day MA')
        ax.plot(df.index, df['roll_30'], label='30-day MA')
        ax.legend(fontsize=8)
        pass

class CrossoverPlotter(RollingMeanPlotter):
    
    def plot(self, ax):
        super().plot(ax)
        # draw just the Close price
        crossover = self.stock_data.crossover_points
        ax.scatter(crossover.index, crossover['roll_30'], color='red', zorder=5, s=50, label='Crossover')
        ax.legend(fontsize=8)
        pass