import streamlit as st

def app():
	st.title("Introduction to Algo-Trading")
	st.markdown("---")
	markdown = """
Algorithmic trading is a method of executing orders that uses automated pre-programmed trading instructions that take variables such as time, price, and volume into account.

Algorithmic trading strategies use a rule-based system to select trading instruments, identify trading opportunities, manage risk, and optimize position size and capital use. In most cases, systems are automated, so the algorithm also executes entries and exits. The terms algorithmic trading, systematic trading, electronic trading, black-box trading, mechanical trading, and quantitative trading are sometimes used interchangeably.

**HFT**, also known as *high-frequency trading*, is frequently associated with algorithmic trading. Indeed, high-frequency trading (HFT) is based on lightning-fast algorithms that take advantage of price differences between exchanges.
	"""
	st.markdown(markdown)


if __name__=="__main__":
	app()
