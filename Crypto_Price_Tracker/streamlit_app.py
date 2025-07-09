import streamlit as st
import requests
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
import time
theme = st.selectbox("🌗 Choose Theme", ["Light", "Dark"])

if theme == "Dark":
    st.markdown(
        """
        <style>
            body { background-color: #1e1e1e; color: white; }
            .stApp { background-color: #1e1e1e; }
        </style>
        """,
        unsafe_allow_html=True
    )

# -------------------- Auto-Refresh --------------------
st.markdown(
    """
    <meta http-equiv="refresh" content="60">
    """,
    unsafe_allow_html=True
)

# -------------------- Email Sender --------------------
def send_email(to_email, crypto, price):
    try:
        from_email = st.secrets["email"]["address"]
        app_password = st.secrets["email"]["app_password"]


        subject = f"{crypto.upper()} Price Alert 📈"
        body = f"Hey! {crypto.upper()} has hit ₹{price} at {datetime.now().strftime('%I:%M %p')}"

        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = from_email
        msg['To'] = to_email

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, app_password)
        server.send_message(msg)
        server.quit()

        return True
    except Exception as e:
        print("❌ Email failed:", e)
        return False

# -------------------- Price Fetcher --------------------
def get_prices(crypto_ids, currency='usd'):
    url = 'https://api.coingecko.com/api/v3/simple/price'
    params = {
        'ids': ','.join(crypto_ids),
        'vs_currencies': currency
    }

    try:
        response = requests.get(url, params=params)
        return response.json()
    except:
        return {}

# -------------------- Session States for Chart --------------------
if "coin_history" not in st.session_state:
    st.session_state.coin_history = {}  # {coin: [prices]}
if "time_labels" not in st.session_state:
    st.session_state.time_labels = []


# -------------------- Streamlit UI --------------------
st.set_page_config(page_title="💸 Crypto Tracker", layout="centered")
st.title("📈 Real-Time Crypto Price Tracker")
st.markdown("Track your favorite coins with love 💙")

# Dropdowns
crypto_list = ['bitcoin', 'ethereum', 'dogecoin', 'shiba-inu', 'cardano']
currency_list = ['usd', 'inr', 'eur']

selected_currency = st.selectbox("Choose Currency", currency_list)
selected_cryptos = st.multiselect("Choose Cryptocurrencies", crypto_list, default=crypto_list[:3])

# -------------------- Fetch Prices --------------------
price_data = get_prices(selected_cryptos, selected_currency)

if price_data:
    # Display price table
    table = []
    for crypto in selected_cryptos:
        price = price_data.get(crypto, {}).get(selected_currency, "N/A")
        table.append({
            'Crypto': crypto.capitalize(),
            f'Price ({selected_currency.upper()})': price
        })

    df = pd.DataFrame(table)
    st.table(df)
    csv = df.to_csv(index=False).encode('utf-8')

    st.download_button(
        label="📥 Download Price Data as CSV",
        data=csv,
        file_name='crypto_prices.csv',
        mime='text/csv',
    )

    # Update chart data for all coins
    timestamp = datetime.now().strftime('%H:%M:%S')
    st.session_state.time_labels.append(timestamp)

    for coin in selected_cryptos:
        price = price_data.get(coin, {}).get(selected_currency, None)
        if price is not None:
            if coin not in st.session_state.coin_history:
                st.session_state.coin_history[coin] = []
            st.session_state.coin_history[coin].append(price)

else:
    st.warning("⚠️ Failed to fetch prices 😢")

# -------------------- Line Chart --------------------
st.subheader("📊 Live Multi-Crypto Trend")

if st.session_state.time_labels:
    df_chart = pd.DataFrame(index=st.session_state.time_labels)
    for coin, prices in st.session_state.coin_history.items():
        df_chart[coin.upper()] = prices
    st.line_chart(df_chart)

# -------------------- Price Alert Section --------------------
st.subheader("🔔 Set Price Alerts")
alert_crypto = st.selectbox("Select crypto for alert", selected_cryptos)
alert_price = st.number_input(f"Alert me when {alert_crypto.upper()} goes above:", min_value=0.0)
email_input = st.text_input("Enter your email for alert")

# Alert check
if price_data and alert_crypto in price_data:
    live_price = price_data[alert_crypto][selected_currency]

    if live_price >= alert_price and email_input:
        if send_email(email_input, alert_crypto, live_price):
            st.success(f"📬 Alert sent! {alert_crypto.upper()} is ₹{live_price}")
            with open("alert_log.txt", "a", encoding="utf-8") as log:
                log.write(f"{datetime.now()} | Alert sent for {alert_crypto.upper()} at ₹{live_price} to {email_input}\n")
        else:
            st.error("❌ Failed to send email.")
