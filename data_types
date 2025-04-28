import streamlit as st

# Title for the app
st.title("Simple Blockchain Info")

# Numeric Data Types
block_number = 123456
transaction_fee = 0.0005

# Text Data Type
wallet_address = "0xABC123XYZ"

# List: Stores multiple transactions
transactions = [10, 50, 200, 5]

# Dictionary: Represents a transaction
transaction1 = {
    "sender": "Alice",
    "receiver": "Bob",
    "amount": 50
}

# Displaying the information using Streamlit
st.header("Block Information")
st.write("*Block Number:*", block_number)
st.write("*Transaction Fee:*", transaction_fee)

st.header("Wallet Information")
st.write("*Wallet Address:*", wallet_address)

st.header("Transactions List")
st.write("*Transaction Amounts:*", transactions)

st.header("Transaction Details")
st.json(transaction1)  # showing dictionary neatly as JSON
