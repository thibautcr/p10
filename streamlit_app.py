import streamlit as st

st.title("Application de détection")

st.siderbar.title('Drop a file section')

st.sidebar.header("1. Upload le fichier CSV")
df = st.sidebar.file_uploader("Dans un premier temps, vous devez déposer votre fichier au format .csv")

st.sidebar.header("2. Upload des fichiers pickle")
estimator = st.sidebar.file_uploader("estimator")
scaler = st.sidebar.file_uploader("scaler")
