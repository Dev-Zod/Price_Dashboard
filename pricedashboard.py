#package installations
pip install -i https://pypi.anaconda.org/ranaroussi/simple finance
import pandas as pd
import streamlit as st
import yfinance as yf



st.write("""
# Stock Price Web Application

 
Shown are the stock closing **price** and ***volume*** of Amazon!

**Period**: May 2012 - May 2022
         
""")

ticker_symbol = 'AMZN'

#get ticker data by creating a ticker object

ticker_data = yf.Ticker(ticker_symbol)

#get amazon historical stock data for a specified time period as a dataframe

tickerDF = ticker_data.history(period="1mo",
                               interval="1d",start='2012-5-31', end= '2022-5-31')

#columns: Open, High, Low Close, Volume, Dividends and Stock Splits

st.write("""
         ## Stock Closing Price in USD
         """    )
st.line_chart(tickerDF.Close)

st.write("""
         ## Stock Volume in USD
         """    )
st.line_chart(tickerDF.Volume)

