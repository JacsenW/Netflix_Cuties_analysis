import yfinance as yf
import pandas as pd

#Define the stock symbol and time range for Netflix
netflix = yf.Ticker("NFLX")

#Download daily stock data for Netflix in 2020
stock_data = netflix.history(start="2020-01-01", end="2020-12-31")

#preview the data 
print(stock_data.head())

# Save the stock data to a CSV file
stock_data.to_csv("netflix_stock_data_2020.csv")
print("Stock data saved to netflix_stock_data_2020.csv")