import streamlit as st
import pandas as pd
import pandas_ta as ta
import yfinance as yf
import numpy as np
from telegram import Bot

# Telegram bot details
telegram_token = "7866169725:AAE2cqgvu82sUsDhB2GRH8JDecaIDue9nYg"
chat_id = "8142807256"
bot = Bot(token=telegram_token)

# Sample function to fetch data and generate signals
def fetch_data():
    df = yf.download("EURUSD=X", period="5d", interval="1m")
    return df

def signal_generator(df):
    # Example indicator logic
    df['RSI'] = ta.rsi(df['Close'], length=14)
    if df['RSI'].iloc[-1] > 70:
        return "Sell"
    elif df['RSI'].iloc[-1] < 30:
        return "Buy"
    else:
        return "Hold"

def send_signal_to_telegram(signal):
    bot.send_message(chat_id=chat_id, text=f"New Signal: {signal}")

# Main Streamlit app
def main():
    st.title("Quotex Signal Bot")
    st.write("This is a simple Quotex signal bot based on technical indicators.")
    
    df = fetch_data()
    signal = signal_generator(df)
    st.write(f"Latest Signal: {signal}")

    send_signal_to_telegram(signal)

if __name__ == "__main__":
    main()
