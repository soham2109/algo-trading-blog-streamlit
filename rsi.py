from datetime import date

import streamlit as st
import yfinance
import pandas as pd
import pandas_datareader as dr
import talib
import matplotlib.pyplot as plt

np.random.seed(0)

stock_key_dict={"Netflix": "NFLX",
				"Microsoft": "MSFT",
				"Google": "GOOG",
				"Apple": "AAPL",
				"Tesla": "TSLA",
				"Ball Corp.": "BLL"}
plt.style.use("bmh")

def get_data(stock):
	today = '{}'.format(date.today())
	data = yfinance.download(stock,
							 '2018-1-1',
							 end=today)
	rsi = talib.RSI(data["Close"])
	return rsi, data





def app():
	st.title("Relative Strength Index (RSI)")
	st.markdown("---")
	markdown="""
Technical analysts use the relative strength index (RSI) to determine whether a stock or other asset is overbought or oversold.

The RSI measures the magnitude of recent price changes and is used to determine whether a stock or other asset has reached an overbought or oversold condition. The RSI provides technical traders with signals about bullish and bearish price momentum, and it is often plotted beneath the graph of an asset’s price. An asset is usually considered overbought when the RSI is above 70% and oversold below 30%.
	"""
	st.markdown(markdown)
	stocks = st.selectbox(label="Select stock:",
						  options=['Netflix', 'Microsoft', 'Google', 'Apple', 'Tesla', 'Ball Corp.']
						  )
	stock_name = stock_key_dict[stocks]


if __name__=="__main__":
	app()
