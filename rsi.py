import streamlit as st

def app():
	st.title("Relative Strength Index (RSI)")
	st.markdown("---")
	markdown="""
Technical analysts use the relative strength index (RSI) to determine whether a stock or other asset is overbought or oversold.

The RSI measures the magnitude of recent price changes and is used to determine whether a stock or other asset has reached an overbought or oversold condition. The RSI provides technical traders with signals about bullish and bearish price momentum, and it is often plotted beneath the graph of an asset’s price. An asset is usually considered overbought when the RSI is above 70% and oversold below 30%.
	"""
	st.markdown(markdown)


if __name__=="__main__":
	app()
