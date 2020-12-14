import yfinance as yf
import pandas as pd
import requests
import json
from yahoofinancials import YahooFinancials
import os
import matplotlib.pyplot as plt
import seaborn
import yahoo_fin.stock_info as si

# Obtain general ticker data
# msft = yf.Ticker("MSFT")
#
# # get stock info
# # print(msft.info)
#
# # get historical market data
# hist = msft.history(period="10y")
#
# hist['Close'].plot(figsize=(16,9))

# Export data to csv
# data_df = yf.download("AAPL", start="2010-01-01", end="2020-12-12")
#
# outputFile = 'aapl.csv'
#
# if os.path.exists(outputFile):
#     os.remove(outputFile)
#
# data_df.to_csv(outputFile)

# Obtain financial fundamentals
# aapl = yf.Ticker("AAPL")
# aapl.history(period="1y")
#
# print(aapl.actions)

#Download stock prices
# tesla_df = yf.download('TSLA', start='2019-01-01', end='2019-12-31', progress=False)
# tesla_df.head()
# tesla_df.to_csv("tesla_stock.csv")

# Variaty of functions
# ticker = yf.Ticker('TSLA')
# tesla_df = ticker.history(period="max")
# # tesla_df['Close'].plot(title="TSLA's stock price")
# ticker.info

# yahoo_financials = YahooFinancials('TSLA')
#
# # data = yahoo_financials.get_historical_price_data(start_date='2000-01-01', end_date='2019-12-31', time_interval='weekly')
# # data = yahoo_financials.get_summary_data()
# # data = yahoo_financials.get_key_statistics_data()
# # data = yahoo_financials.get_stock_data()
# # data = yahoo_financials.get_stock_quote_type_data()
# # data = yahoo_financials.get_financial_stmts(frequency='annual', statement_type='income')
# data = yahoo_financials.get_operating_income()
#
# print(data)

# tsla_df = pd.DataFrame(data['TSLA']['prices'])
# tsla_df = tsla_df.drop('date', axis=1).set_index('formatted_date')
# tsla_df.head()
#
# print(tsla_df)

# r = requests.get("https://financialmodelingprep.com/api/v3/financials/income-statement/AAPL?period=quarter")
# r = r.json()
# print(r)

# Youtube tutorial on scraping financial stock data
# test = si.get_cash_flow('TSLA', yearly=False)
# test = si.get_balance_sheet('msft')
# test = si.get_income_statement('msft')
# test = si.get_financials('nflx')
#
#
# print(test.keys())

# Medium: using alpha_vantage
