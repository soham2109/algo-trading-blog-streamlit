import introduction
import rsi
import zig_zag
import sma
import streamlit as st

PAGES = { "Introduction": introduction,
		  "Zig-Zag": zig_zag,
		  "RSI": rsi,
		  "SMA": sma,}


def app():
	st.sidebar.title("Algo Trading Blog")
	page_selected = st.sidebar.radio("Go to", list(PAGES))
	page = PAGES[page_selected]
	page.app()

if __name__ == "__main__":
	app()
