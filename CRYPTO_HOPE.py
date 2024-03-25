#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


data=pd.read_csv("crypto_data.csv")


# In[3]:


import streamlit as st
import pandas as pd
import plotly.express as px

# Sidebar
st.sidebar.header('Select Crypto Currency')
selected_crypto = st.sidebar.selectbox('Crypto type', data['Name'].unique())

# Filtering data
data_selected = data[data['Name'] == selected_crypto]

# Main
st.header(f'{selected_crypto} from 2018 to 2023')
fig = px.line(data_selected, x='Date', y=['Open', 'High', 'Low', 'Close'], title=f'{selected_crypto} OHLC Prices')
fig.update_xaxes(rangeslider_visible=True)
st.plotly_chart(fig)

st.header(f'{selected_crypto} Volume')
fig2 = px.line(data_selected, x='Date', y='Volume', title=f'{selected_crypto} Volume')
fig2.update_xaxes(rangeslider_visible=True)
st.plotly_chart(fig2)

st.header(f'{selected_crypto} RSI and SMA')
fig3 = px.line(data_selected, x='Date', y=['RSI', 'SMA'], title=f'{selected_crypto} RSI and SMA')
fig3.update_xaxes(rangeslider_visible=True)
st.plotly_chart(fig3)

st.header(f'{selected_crypto} MACD')
fig4 = px.line(data_selected, x='Date', y='MACD', title=f'{selected_crypto} MACD')
fig4.update_xaxes(rangeslider_visible=True)
st.plotly_chart(fig4)

st.header(f'{selected_crypto} Bollinger Bands')
fig5 = px.line(data_selected, x='Date', y=['bb_bbm', 'bb_bbh', 'bb_bbl'], title=f'{selected_crypto} Bollinger Bands')
fig5.update_xaxes(rangeslider_visible=True)
st.plotly_chart(fig5)

st.header(f'{selected_crypto} Daily Returns')
fig6 = px.line(data_selected, x='Date', y='Daily Returns', title=f'{selected_crypto} Daily Returns')
fig6.update_xaxes(rangeslider_visible=True)
st.plotly_chart(fig6)

