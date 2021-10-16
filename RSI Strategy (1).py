#!/usr/bin/env python
# coding: utf-8

# In[1]:


import yfinance
import pandas as pd
import talib
import matplotlib.pyplot as plt
import pandas_datareader as dr
get_ipython().run_line_magic('matplotlib', 'inline')
data = yfinance.download('NFLX','2016-1-1','2020-1-1')


# In[2]:


rsi = talib.RSI(data["Close"])
fig = plt.figure()
fig.set_size_inches((25, 18))
ax_rsi = fig.add_axes((0, 0.24, 1, 0.2))
ax_rsi.plot(data.index, [70] * len(data.index), label="overbought")
ax_rsi.plot(data.index, [30] * len(data.index), label="oversold")
ax_rsi.plot(data.index, rsi, label="rsi")
ax_rsi.plot(data["Close"])
ax_rsi.legend()

section = None
sections = []
for i in range(len(rsi)): 
    if rsi[i] < 30:
        section = 'oversold'
    elif rsi[i] > 70:
        section = 'overbought'
    else:
        section = None
    sections.append(section)


# In[ ]:




