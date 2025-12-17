import streamlit as st
import requests

st.title("💳 Credit Card Fraud Detection")

st.write("Enter transaction details:")

inputs = []
for i in range(1, 29):
    val = st.number_input(f"V{i}", value=0.0)
    inputs.append(val)

amount = st.number_input("Transaction Amount", value=0.0)
inputs.append(amount)

if st.button("Predict Fraud"):
    data = {f"f{i}": inputs[i] for i in range(len(inputs))}

    response = requests.post("http://127.0.0.1:8000/predict", json=data)

    if response.status_code == 200:
        result = response.json()
        if result["fraud_prediction"] == 1:
            st.error(f"⚠️ Fraud Detected (Probability: {result['fraud_probability']})")
        else:
            st.success(f"✅ Transaction Safe (Probability: {result['fraud_probability']})")
