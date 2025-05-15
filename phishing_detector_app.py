import streamlit as st
import joblib
import pandas as pd
import re
from urllib.parse import urlparse
data =  pd.read_csv("Phishing_Legitimate_full.csv")

# Load model and scaler
model = joblib.load("phishing_model.pkl")
scaler = joblib.load("scaler.pkl")
expected_columns = joblib.load("columns.pkl")

# Feature extraction function
def extract_features(url):
    features = {}
    parsed_url = urlparse(url) 

    features["URL_Lenght"] = len(url)
    features["Have_At_Symbol"] = 1 if "@" in url else 0
    features["Double_slash_redirecting"] = 1 if url.count("//") > 1 else 0 
    features["Prefix_Suffix"] = 1 if "-" in parsed_url.netloc else 0
    features["Subdomain"]  = 1 if url.count(".") > 2 else 0
    features["HTTPS_Token"] = 1 if "https" in parsed_url.netloc else 0

    # Fill in 0 for remaining expected features (if any)
    for col in expected_columns:
        if col not in features and col not in ["CLASS_LABEL", "Id"]:
            features[col] = 0

    return features
 

# Streamlit app interface
st.title("🔒Phishing Website Detector")

st.markdown("### ✨ Welcome to the Phishing Dectector App")
st.markdown("**Paste a URL to detect if it's phishing.** ")

url = st.text_input("Enter the URL. ")

if st.button("Check"):
    if url:
        extracted = extract_features(url)

        # Convert to DataFrame
        input_df = pd.DataFrame([extracted])

        # Reindex to ensure same order and fill missing with 0
        input_df = input_df.reindex(columns=expected_columns, fill_value=0)

        # Scale the input data using preloaded scaler
        scaled_input = scaler.transform(input_df)

        # Predict using preloaded model
        prediction = model.predict(scaled_input)

       # Show the predicted results
    if prediction == 1:
        st.markdown("### 🚨 Warning! This website is a **Phishing** website! 🚨 ")
    else:
            st.markdown("### ✅ This website is **Safe**! ✅")
else:
    st.warning("Please enter a URL.")
