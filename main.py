import yfinance as yf
import matplotlib.pyplot as plt

df = yf.download("AAPL", period="1y")
# flatten the multi-level columns
df.columns = df.columns.get_level_values(0)

# print(df.head())
# print(df.tail())

df['roll_7'] = df['Close'].rolling(7).mean()
df['roll_30'] = df['Close'].rolling(30).mean()
# print(df[['Close','roll_7','roll_30']].head(35))

# detects crossovers between the 7-day and 30-day moving averages
df['signal'] = df['roll_7'] > df['roll_30']
df['crossover'] = df['signal'].astype(int).diff().abs()
crossover_points = df[df['crossover'] == 1]

# prints the number of crossovers and the first few crossover points
print(f"Found {len(crossover_points)} crossovers")
print(crossover_points[['Close', 'roll_7', 'roll_30']].head())

# plots the closing price, moving averages, and crossover points
plt.figure(figsize=(12,6))
plt.plot(df.index, df['Close'], label='Close', alpha=0.5)
plt.plot(df.index, df['roll_7'], label='7-day MA')
plt.plot(df.index, df['roll_30'], label='30-day MA')
plt.scatter(crossover_points.index, crossover_points['roll_30'], color='red', zorder=5, s=50, label='Crossover')
plt.legend()
plt.show()