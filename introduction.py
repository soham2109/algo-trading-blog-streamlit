import streamlit as st

def max_width(prcnt_width:int = 75):
    max_width_str = f"max-width: {prcnt_width}%;"
    st.markdown(f"""
                <style>
                .reportview-container .main .block-container{{{max_width_str}}}
                </style>
                """,
                unsafe_allow_html=True,
    )


def app():
	max_width(80)
	st.title("Introduction to Algo-Trading")
	st.markdown("---")
	st.header("Introduction to Stock Market")
	st.markdown("---")
	markdown = """
Stock Market has been in news ever since its inception, it was considered to be a rich man's game and only few with connections to Stock market would dare to enter the market and trading in it was cumbersome. But nowadays, it's a household name and trading was never so open to all. Nowadays opening a demat account is almost as easy as opening an Instagram account and we have been hearing for some time that the market is trending at an All Time High. Every family whatsapp group gets a message that IF would have invested X amount of money in 10 years ,today you would have been a millionaire, these are the fear of missing out (FOMO) moments, that lead to many people enter in stock market with any prior knowledge and if they lose their amount, blame the market. It is not that hard to shield your primary invested capital if you have basic knowledge of Stock Market.

### So what is Stock Market Investment?


Stock market investment is a long-term process that can aid in financial management. Investing in the stock market might be intimidating, particularly when you are first getting started, as it may appear to be excessively complicated or hazardous. A thorough understanding can assist you in getting started.

Stock market is the place where shares and other company securities are traded extensively, and they play a critical role in the success of commerce and the overall health of an economy. Traders can take exposure to stock markets in the world's global financial centres, which regulate markets and run indices on which they can gain capital growth based on the risk taking abilities .For those who really understand the stock markets, more chances to profitable trading can be identified and the trends and directions of underlying movement in a particular market can be more easily highlighted. Those who understand more closely what they do on stock markets therefore have a better opportunity to identify viable businesses.


### Trading


Everyone has heard of the term "**trading**". The majority of us have traded in our daily lives, even if we are unaware of it. Everything you buy in a store is essentially a trade of money for the goods you desire.

It is the same principle when we talk about trading in financial markets. Consider someone who trades stocks. They are, in fact, purchasing shares (or a small portion of a company). If the value of those shares rises, they profit by reselling them at a higher price. This is a form of trading. You buy something at one price and sell it at a higher price, hopefully making a profit, and vice versa. But one may think  why would the value of the stock rise? The answer is simple: value changes due to supply and demand – the higher the demand for something, the higher the price people are willing to pay for it. So for these matching of Supply and demand at a  certain price and placing a trade accurately for maximum profit is impossible for human capabilities So we take help of computer code to place a trade when our certain requirements are met. Algorithmic trading accounts for around 60-73% of the overall United States equity trading.


### Algorithmic Trading


**Algorithmic trading** is a method of executing orders that uses automated pre-programmed trading instructions that take variables such as time, price, and volume into account. Algorithmic trading strategies use a rule-based system to select trading instruments, identify trading opportunities, manage risk, and optimize position size and capital use. In most cases, systems are automated, so the algorithm also executes entries and exits. The terms algorithmic trading, systematic trading, electronic trading, black-box trading, mechanical trading, and quantitative trading are sometimes used interchangeably. HFT, also known as high-frequency trading, is frequently associated with algorithmic trading. Indeed, high-frequency trading (HFT) is based on lightning-fast algorithms that take advantage of price differences between exchanges.
	"""
	st.markdown(markdown)


if __name__=="__main__":
	app()
