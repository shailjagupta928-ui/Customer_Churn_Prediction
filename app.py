import streamlit as st
import pandas as pd
import joblib

# =========================
# 🎯 LOAD PIPELINE MODEL
# =========================
model = joblib.load("xgb_pipeline_new.pkl")  # change name if needed

cols = joblib.load("cols.pkl")  # load columns used in training 

# =========================
# 🏷️ APP TITLE
# =========================
st.title("📊💼 Customer Churn Prediction App")
st.write("Fill customer details below to predict churn 🔮")

# =========================
# 🧾 USER INPUTS
# =========================
gender = st.selectbox("👤 Gender", ["Male", "Female"])
senior = st.selectbox("🧓 Senior Citizen", [0, 1])
partner = st.selectbox("❤️ Partner", ["Yes", "No"])
dependents = st.selectbox("👶 Dependents", ["Yes", "No"])
tenure = st.slider("📅 Tenure (months)", 0, 72, 12)
phone = st.selectbox("☎️ Phone Service", ["Yes", "No"])
internet = st.selectbox("🌐 Internet Service", ["DSL", "Fiber optic", "No"])
contract = st.selectbox("📜 Contract", ["Month-to-month", "One year", "Two year"])
monthly = st.slider("💰 Monthly Charges", 0.0, 150.0, 50.0)
total = st.slider("💳 Total Charges", 0.0, 10000.0, float(tenure * monthly))

# =========================
# 📦 CREATE INPUT DATAFRAME
# =========================
import pandas as pd

input_dict = ({
    "gender": gender,
    "SeniorCitizen": senior,
    "Partner": partner,
    "Dependents": dependents,
    "tenure": tenure,
    "PhoneService": phone,
    "MultipleLines": "No",
    "InternetService": internet,
    "OnlineSecurity": "No",
    "OnlineBackup": "No",
    "DeviceProtection": "No",
    "TechSupport": "No",
    "StreamingTV": "No",
    "StreamingMovies": "No",
    "Contract": contract,
    "PaperlessBilling": "Yes",
    "PaymentMethod": "Electronic check",
    "MonthlyCharges": monthly,
    "TotalCharges": total
})

input_df = pd.DataFrame([input_dict])



input_df = input_df.reindex(columns=cols, fill_value=0)

# =========================
# 🚀 PREDICTION
# =========================
if st.button("🔮 Predict Churn"):
    
    prediction = model.predict(input_df)[0]
    
    prob = model.predict_proba(input_df)[0][1]
    
    if prediction == 1:
        st.error(f"⚠️ Customer WILL CHURN ❌\nProbability: {prob:.2f}")
    else:
        st.success(f"✅ Customer will STAY 🎉\nProbability: {prob:.2f}")

# =========================
# 📋 SHOW INPUT
# =========================
st.subheader("📋 Input Data")
st.write(input_df)