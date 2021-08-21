import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st


stock_key_dict={"Netflix": "NFLX",
				"Microsoft": "MSFT",
				"Google": "GOOG",
				"Apple": "AAPL",
				"Tesla": "TSLA",
				"Ball Corp.": "BLL"}


plt.style.use("bmh")


@st.cache()
def get_data(stock):
	nflx_ticker = yf.Ticker(stock)
	nflx= yf.download(stock)
	SMA20 = nflx['Close'].rolling(window = 20).mean()
	SMA50 = nflx['Close'].rolling(window = 50).mean()
	return nflx, SMA20, SMA50


def get_points_above(sma_low, sma_high):
	points_above = {}
	for pair in zip(sma_low, sma_high):
		if pair[0] >= pair[1]:
			date = sma_low[sma_low == pair[0]].index[0]
			points_above[date] = pair[0]

	points_above = pd.Series(points_above, name='Price_Points')
	points_above.index.name = 'Date'

	return points_above


def get_crossovers(nflx, SMA20 , SMA50):
	crossovers = pd.DataFrame()
	crossovers['Dates'] = SMA20['Date']
	crossovers['Price'] = [i for i in nflx['Close']]
	crossovers['SMA20'] = SMA20['Close']
	crossovers['SMA50'] = SMA50['Close']
	crossovers['position'] = crossovers['SMA20'] >= crossovers['SMA50']
	crossovers['pre-position'] = crossovers['position'].shift(1)
	crossovers['Crossover'] = np.where(crossovers['position'] == crossovers['pre-position'], 0, 1)
	crossovers['Crossover'][0] = 0
	# crossovers.set_index('Dates')

	crossovers = crossovers.loc[crossovers['Crossover'] == 1]
	crossovers = crossovers.reset_index()
	crossovers = crossovers.drop(['position', 'pre-position', 'Crossover','index'], axis=1)
	# crossovers.set_index('Dates')

	return crossovers


def return_plot(nflx, SMA20, SMA50, crossovers, label):
	fig, ax = plt.subplots(1,1, constrained_layout=True, figsize=(10,5))
	ax.plot(nflx['Close'][-600:], label=label, lw=2)

	#print(nflx.columns)


	#ax.set_facecolor("#f1f1f1")
	ax.plot(SMA20[-600:], label='SMA20',lw=2)
	ax.plot(SMA50[-600:], label='SMA50', lw=2)
	ax.plot(crossovers.loc[crossovers.Signal == 'Buy']['Dates'][-5:],
		  crossovers['SMA20'][crossovers.Signal == 'Buy'][-5:],
		  '^', markersize=15, color='g', label='Buy',)
	ax.plot(crossovers.loc[crossovers.Signal == 'Sell']['Dates'][-4:],
		  crossovers['SMA20'][crossovers.Signal == 'Sell'][-4:],
		  'v', markersize=15, color='r', label='Sell')
	ax.legend(loc='upper left', fontsize=15)
	ax.set_xlabel("TIME")
	ax.set_ylabel("PRICE")
	ax.set_title("Stock Price for {}".format(label))

	ax.set_xlim(xmin=nflx[-600:].index.min(),
				xmax=nflx[-600:].index.max())

	return fig






def app():
	st.title("Simple Moving Average (SMA)")
	st.markdown("---")
	markdown="""
A simple moving average (SMA) is calculated by adding all the data for a specific period and dividing the total by the number of days. They are considered to be particularly useful in upward or downward trending markets.

When asset prices cross over their moving averages, it may generate a trading signal for technical traders. A general rule of thumb among traders is that if a stock price is above its 200-days moving average, the trend is bullish (i.e., the price rises). So they are often looking for stocks whose price is above the 200-periods SMA.

A straightforward example of an Algo trading system would :

**BUY** an instrument if its 20-day moving average cross above its 50-day moving average and

**SELLS** the instrument when the 20-day moving average cross below the 50-day moving average
	"""
	st.markdown(markdown)
	stock_name_ = st.selectbox(label="Select the stock name: ",
							  options=("Netflix","Microsoft","Google","Apple", "Tesla","Ball Corp."))
	stock_name = stock_key_dict[stock_name_]

	nflx, SMA20, SMA50 = get_data(stock_name)
	points_above_SMA50 = get_points_above(SMA20, SMA50)

	SMA20_reset = SMA20.reset_index()
	SMA50_reset = SMA50.reset_index()

	crossovers = get_crossovers(nflx, SMA20_reset, SMA50_reset)
	crossovers['Signal'] = ""
	crossovers['Binary_Signal'] = 1


	for i in range(len(crossovers['SMA20'])):
		if crossovers['SMA20'][i] > crossovers['SMA50'][i]:
			crossovers['Binary_Signal'][i] = 1
			crossovers['Signal'][i] = 'Buy'
		else:
			crossovers['Signal'][i] = 'Sell'

	st.subheader("{} Stock Data".format(stock_name_))
	st.dataframe(nflx.tail(10))

#	st.subheader("Defining Crossovers after SMA calculations")
#	st.dataframe(crossovers.tail(10))

#	st.subheader("Let's visualize the data obtained.")
	st.pyplot(return_plot(nflx, SMA20, SMA50, crossovers, label=stock_name_))


if __name__=="__main__":
	app()
