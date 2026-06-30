import yfinance as yf
import matplotlib.pyplot as plt

df = yf.download("AAPL", period="1y")
df.columns = df.columns.get_level_values(0)

# print(df.head())
# print(df.tail())

df['roll_7'] = df['Close'].rolling(7).mean()
df['roll_30'] = df['Close'].rolling(30).mean()
# print(df[['Close','roll_7','roll_30']].head(35))

plt.figure(figsize=(12,6))
plt.plot(df.index, df['Close'], label='Close', alpha=0.5)
plt.plot(df.index, df['roll_7'], label='7-day MA')
plt.plot(df.index, df.index, df['roll_30'], label='30-day MA')
plt.legend()
plt.show()

print(df.columns)
print(df.columns.tolist())
print(df.index)