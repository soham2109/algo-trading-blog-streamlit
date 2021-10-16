from datetime import date

import streamlit as st
import yfinance
import pandas as pd
import numpy as np
import pandas_datareader as dr
# import talib
import matplotlib.pyplot as plt

np.random.seed(0)

stock_key_dict={"Netflix": "NFLX",
				"Microsoft": "MSFT",
				"Google": "GOOG",
				"Apple": "AAPL",
				"Tesla": "TSLA",
				"Ball Corp.": "BLL"}
plt.style.use("bmh")


def max_width(prcnt_width:int = 75):
    max_width_str = f"max-width: {prcnt_width}%;"
    st.markdown(f"""
                <style>
                .reportview-container .main .block-container{{{max_width_str}}}
                </style>
                """,
                unsafe_allow_html=True,
    )

def calculate_rsi(data, periods = 14, ema=True):
	close_delta = data.diff()
	# Make two series: one for lower closes and one for higher closes
	up = close_delta.clip(lower=0)
	down = -1 * close_delta.clip(upper=0)

	if ema == True:
		# Use exponential moving average
		ma_up = up.ewm(com = periods - 1, adjust=True, min_periods = periods).mean()
		ma_down = down.ewm(com = periods - 1, adjust=True, min_periods = periods).mean()
	else:
		# Use simple moving average
		ma_up = up.rolling(window = periods, adjust=False).mean()
		ma_down = down.rolling(window = periods, adjust=False).mean()

	rsi = ma_up / ma_down
	rsi = 100 - (100/(1 + rsi))
	return rsi


def get_data(stock):
	today = '{}'.format(date.today())
	data = yfinance.download(stock,
							 '2018-1-1',
							 end=today)
	# rsi = talib.RSI(data["Close"])
	rsi = calculate_rsi(data["Close"])
	return rsi, data





def app():
	max_width(80)
	st.title("Relative Strength Index (RSI)")
	st.markdown("---")
	markdown="""
Technical analysts use the relative strength index (RSI) to determine whether a stock or other asset is overbought or oversold. The RSI measures the magnitude of recent price changes and is used to determine whether a stock or other asset has reached an overbought or oversold condition. The RSI provides technical traders with signals about bullish and bearish price momentum, and it is often plotted beneath the graph of an asset’s price. An asset is usually considered overbought when the RSI is above 70% and oversold below 30%.


The RSI is computed with a two-part calculation that starts with the following formula:

$RSI_{\\text{step one}} = 100 - [\\frac{100}{1+\\frac{Average Gain}{Average Loss}}]$

Here, we use only positive values for the case of Average Loss. Assume the market closed higher seven out of the last fourteen days, averaging 1%. The subsequent seven days closed lower by an average of 0.8%. The first portion of the RSI calculation is as follows:
$55.55 = 100 - [\\frac{100}{1 + \\frac{1\%/14}{0.8\%/14}}]$

The second portion of the RSI formula can be calculated after 14 periods of data are available. The second step in the algorithm smoothes out the output.

$RSI_{\\text{step two}} = 100 - [\\frac{100}{1+\\frac{(Previous Average Gain)\\times13) + Current Gain}{(Previous Average Loss)\\times13) + Current Loss}}]$

	"""
	st.markdown(markdown)
	stocks = st.selectbox(label="Select stock:",
						  options=['Netflix', 'Microsoft', 'Google', 'Apple', 'Tesla', 'Ball Corp.']
						  )
	stock_name = stock_key_dict[stocks]
	rsi, data = get_data(stock_name)

if __name__=="__main__":
	app()
