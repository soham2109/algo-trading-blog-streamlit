from datetime import date, timedelta

import pandas as pd
import numpy as np
from scipy import signal
from pandas_datareader import data
from pandas_datareader.nasdaq_trader import get_nasdaq_symbols
from pandas_datareader.yahoo.headers import DEFAULT_HEADERS
import requests_cache
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

import streamlit as st
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

def filter(values, percentage):
	previous = values[0]
	mask = [True]
	for value in values[1:]:
		relative_difference = np.abs(value - previous)/previous
		if relative_difference > percentage:
			previous = value
			mask.append(True)
		else:
			mask.append(False)
	return mask


def get_data(stock=None, start_date=None, end_date=None):
	expire_after = timedelta(days=3)
	session = requests_cache.CachedSession(cache_name='cache',
										   backend='sqlite',
										   expire_after=expire_after)
	session.headers = DEFAULT_HEADERS
	df = data.DataReader(
		stock, 'yahoo',
		start=start_date,
		end=end_date,
		#data_source='yahoo'
		session=session
	)
	return df


def plot(df_peaks_valleys, filtered, data_x, data_y, label):
	# Instantiate axes.
	(fig, ax) = plt.subplots(1,1, figsize=(10,5), \
							 constrained_layout=True)
	# Plot zigzag trendline.
	ax.plot(df_peaks_valleys['date'].values,
			df_peaks_valleys['zigzag_y'].values,
			color='red', label="Extrema", lw=2)
	# Plot zigzag trendline.
	ax.plot(filtered['date'].values,
			filtered['zigzag_y'].values,
			color='blue', label="ZigZag", lw=2)
	# Plot original line.
	ax.plot(data_x, data_y,
			linestyle='dashed',
			color='black',
			label="Original Line", linewidth=2)
	ax.set_title("Stock: {}".format(label))
	plt.legend(loc="best")
	return fig


def track_valleys(stock):
	today = '{}'.format(date.today())
	cont = 0

	series = get_data(stock=stock, start_date='2018-1-1', end_date=today)
	series.insert(loc=0, column='Date', value=series.index)
	series = series.reset_index(drop=True)
	data_x = series.index.values
	data_y = series['Close'].values
	peak_indexes = signal.argrelextrema(data_y, np.greater)
	peak_indexes = peak_indexes[0]

	# Find valleys(min).
	valley_indexes = signal.argrelextrema(data_y, np.less)
	valley_indexes = valley_indexes[0]

	# Merge peaks and valleys data points using pandas.
	df_peaks = pd.DataFrame({'date': data_x[peak_indexes],
							 'zigzag_y': data_y[peak_indexes]})
	df_valleys = pd.DataFrame({'date': data_x[valley_indexes],
							   'zigzag_y': data_y[valley_indexes]})
	df_peaks_valleys = pd.concat([df_peaks, df_valleys],
								  axis=0, ignore_index=True, sort=True)

	# Sort peak and valley datapoints by date.
	df_peaks_valleys = df_peaks_valleys.sort_values(by=['date'])
	p = 0.1 # 20%
	filter_mask = filter(df_peaks_valleys.zigzag_y, p)
	filtered = df_peaks_valleys[filter_mask]

	return (df_peaks_valleys, filtered, data_x, data_y)



def app():
	max_width(80)
	st.title("ZIG ZAG")
	st.markdown("---")
	markdown="""
The Zig Zag indicator is a valuable tool for visualizing past price trends and can make using drawing tools easier by providing a visual representation of those trends. As a result, it connects local peaks and troughs. Prices are tracked using this tool in order to identify price trends. Rather than relying on random price fluctuations, it tries to identify trend changes. If the price movement between the swing high and swing low is greater than the specified percentage — **often 5 percent** — then zig-zag lines will appear on the chart. The indicator makes it easier to spot trends in all time frames by filtering out minor price movements.

It is important to note that the Zig Zag indicator does not predict future trends; however, it can be used to identify potential support and resistance zones between plotted swing high and swing low levels. Zig Zag lines can also reveal reversal patterns, such as double bottoms and head and shoulders tops, when viewed from different angles. When the Zig Zag line changes direction, traders can use popular technical indicators such as the *relative strength index* (**RSI**) and the stochastics oscillator to determine whether a security's price is overbought or oversold. The RSI and the stochastics oscillator are two popular technical indicators.
	"""
	st.markdown(markdown)
	stocks = st.selectbox(label="Select stock:",
						  options=['Netflix', 'Microsoft', 'Google', 'Apple', 'Tesla', 'Ball Corp.']
						  )
	stock_name = stock_key_dict[stocks]
	(df_peaks_valleys, filtered, data_x, data_y) = track_valleys(stock_name)
	st.pyplot(plot(df_peaks_valleys, filtered, \
					data_x, data_y, label=stocks))



if __name__=="__main__":
	app()
