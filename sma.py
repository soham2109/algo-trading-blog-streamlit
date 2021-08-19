import streamlit as st

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


if __name__=="__main__":
	app()
