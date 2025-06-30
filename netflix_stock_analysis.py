import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

#Downloaad stock data for Netflix 2020
netflix = yf.Ticker("NFLX")
stock_data = netflix.history(start="2020-01-01", end="2020-12-31")
stock_data.reset_index(inplace=True)

#Plot Netlfix stock price
plt.figure(figsize=(14, 7))
plt.plot(stock_data['Date'], stock_data['Close'], label='Close Price', color='darkblue')
plt.axvline(pd.to_datetime('2020-08-18'),color='orange', linestyle='--', label='Trailer Released')
plt.axvline(pd.to_datetime('2020-09-09'), color='red', linestyle='--', label='Show Released')
plt.title('Netflix Stock Price in 2020')
plt.xlabel('Date')
plt.ylabel('Closing Price (USD)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

#Calculate price change before and after the film release
price_before = stock_data[stock_data['Date'] < '2020-09-08']['Close'].values[0]
price_after = stock_data[stock_data['Date'] > '2020-09-10']['Close'].values[0]
percent_change = ((price_after - price_before) / price_before) * 100

print(f"Price before release: ${price_before:.2f}")
print(f"Price after release: ${price_after:.2f}")
print(f"Percentage change around release: {percent_change:.2f}%")
