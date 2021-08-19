import streamlit as st

def app():
	st.title("ZIG ZAG")
	st.markdown("---")
	markdown="""
The Zig Zag indicator is a valuable tool for visualizing past price trends and can make using drawing tools easier by providing a visual representation of those trends. As a result, it connects local peaks and troughs. Prices are tracked using this tool in order to identify price trends.

Rather than relying on random price fluctuations, it tries to identify trend changes. If the price movement between the swing high and swing low is greater than the specified percentage — **often 5 percent** — then zig-zag lines will appear on the chart. The indicator makes it easier to spot trends in all time frames by filtering out minor price movements.

It is important to note that the Zig Zag indicator does not predict future trends; however, it can be used to identify potential support and resistance zones between plotted swing high and swing low levels.

Zig Zag lines can also reveal reversal patterns, such as double bottoms and head and shoulders tops, when viewed from different angles. When the Zig Zag line changes direction, traders can use popular technical indicators such as the *relative strength index* (**RSI**) and the stochastics oscillator to determine whether a security's price is overbought or oversold. The RSI and the stochastics oscillator are two popular technical indicators.
	"""
	st.markdown(markdown)


if __name__=="__main__":
	app()
