📊 Customer Churn Prediction using Machine Learning
<img width="1523" height="594" alt="Screenshot (18)" src="https://github.com/user-attachments/assets/038fe45a-b7c5-41ab-b0c4-e6dd23362ec9" />




---
LIVE DEMO - https://churnpredictionanalysis-8mojyugbcgndz5szdqzb6a.streamlit.app/
           
 App Screenshot
<img width="1738" height="790" alt="Screenshot (29)" src="https://github.com/user-attachments/assets/69efb812-a06a-4216-914d-7c282299bba0" />
<img width="1735" height="680" alt="Screenshot (30)" src="https://github.com/user-attachments/assets/236364c6-8a1f-4ef4-85dd-97977bed01e0" />




## 📌 Project Overview
Customer churn is a major challenge for businesses. In this project, we analyze customer data and build a predictive model to identify customers who are at risk of leaving.It is built using Logistic Regression, Random Forest, and XGBoost with a fully automated sklearn Pipeline and deployed using Streamlit.


🧠 Problem Statement

Telecom companies lose revenue when customers leave (churn).
The goal is to predict churn early so companies can take preventive actions.


⚙️ Tech Stack
The project covers the full ML lifecycle:
- Data Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Model Building & Evaluation
- Deployment using Streamlit

---

## 🎯 Objective
To build a model that accurately predicts customer churn and provides insights that can help businesses reduce customer loss.

---

## 🛠️ Tech Stack
- Python  
- Pandas, NumPy  
- Scikit-learn  
- Matplotlib, Seaborn  
- Streamlit
- XGBOOST
  
-Joblib (model saving) 

📈 Model Performance
Model	Accuracy	Precision	Recall	F1 Score
Logistic Regression	0.787	0.620	0.516	0.563
Random Forest	0.786	0.628	0.478	0.543
XGBoost	0.774	0.589	0.497	0.539

 📊 Features
- Cleaned and preprocessed dataset  
- Performed detailed EDA to find churn patterns  
- Built multiple ML classification models  
- Selected best model based on performance metrics  
- Deployed interactive web app using Streamlit

 ⚙️ Pipeline Features
Automatic handling of categorical variables (OneHotEncoding)
Feature scaling (StandardScaler)
No manual preprocessing required during prediction
Prevents feature mismatch errors

🧠 Key Insights
Accuracy alone is not reliable due to possible class imbalance
F1-score provides a better measure of model performance
Logistic Regression gave more balanced predictions
Random Forest had higher precision but lower recall
XGBoost can be improved with hyperparameter tuning

📌 Future Improvements
Hyperparameter tuning for XGBoost
Handling class imbalance (SMOTE, undersampling)
Deploy model using Streamlit
Add real-time prediction system

🎯 Conclusion

This project demonstrates how Machine Learning can effectively predict customer churn. By identifying at-risk customers early, businesses can take targeted actions to improve retention and reduce losses.

