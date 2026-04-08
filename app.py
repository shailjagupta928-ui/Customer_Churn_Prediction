import streamlit as st
import pickle
import pandas as pd

model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
features = pickle.load(open("features.pkl", "rb"))

st.title(" Customer Churn Prediction📊")
st.markdown("### 🔍 Check if a customer will leave or stay")

st.markdown("## 🧾 Customer Details")

col1, col2 = st.columns(2)

with col1:
    tenure = st.slider("📅 Tenure (months)", 0, 72, 12)
    monthly = st.number_input("💰 Monthly Charges")

with col2:
    total = st.number_input("🧾 Total Charges")

st.sidebar.title("📌 About")
st.sidebar.info("ML model to predict churn")
st.sidebar.markdown("Made by Shailja⚡✨")

if st.button("🚀 Predict Now"):
    input_dict = {
        "tenure": tenure,
        "MonthlyCharges": monthly,
        "TotalCharges": total
    }

    input_df = pd.DataFrame([input_dict])

    for col in features:
        if col not in input_df.columns:
            input_df[col] = 0

    input_df = input_df[features]

    input_scaled = scaler.transform(input_df)
    prediction = model.predict(input_scaled)

    if prediction[0] == 1:
        st.error("❌ Customer will churn")
        st.image("https://cdn-icons-png.flaticon.com/512/1828/1828843.png", width=100)
    else:
        st.success("✅ Customer will stay")
        st.image("https://cdn-icons-png.flaticon.com/512/845/845646.png", width=100)
