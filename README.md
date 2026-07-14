# 🎭 Phishing-detector-app

This project is a machine-learning power web app that detects whether  a URL is **phishing** or **legitimate**. It is built using Python and deployed with [Streamlit.]( https://streamlit.io/)
<br>
🔗 **Live App:** [Try it here](https://phishing-detector-app-hlxvj4rqueq5nqgfu5qzj8.streamlit.app/)
<br>
📁 **Project Type:** End-to-end Machine Learning + Web Deployment
<br>
🧠 **Tech Stack:** Pandas Scikit-learn NumPy Streamlit Python


## 📌 Features

- Paste any URL and get a predictions instantly
- Automatic Feature extraction from the URL
- Lightweight, fast, and easy to use
- Deployed online for public use

## 🚀 How it works
 
 1. The app extracts feature from tthe input URL (like HTTPS usage, URL length  , special symbols etc.)
 2. A trained ML model classifies the URL s **phishing** or **legitimate**
 3. The result is shown instantly on the screen

##  🧠 Machine learning details

- **Model used:** RandomForestClassifier
- **Accuracy:** *98.2%* on test data
- **Feature Engineering:**
 Custom features from raw URLs such as:
  - Presence of `https`
  - Length of URL
  - Count of special characters like `@`, `-`, `.`
  - Use of IP addresses or suspicious keywords (e.g. `login`, `secure`, etc.)


## 🛠 How to run locally

```bash
# Clone the repository
git clone https://github.com/namal-xx/Phishing-detector-app.git 
cd Phishing-detector-app

# Install dependencies
pip install -r requiremenets.txt

# Run the app
streamlit run phishing_detector_app.py
 

  
