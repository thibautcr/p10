import streamlit as st
import pandas as pd
import pickle

st.title("Application de détection")

st.sidebar.title('Drop a file section')

st.sidebar.subheader("1. Upload le fichier CSV")
file = st.sidebar.file_uploader("Deposez votre fichier au format .csv")
df = pd.read_csv(file, sep=",", decimal=".").reset_index()
st.sidebar.write("[Exemple du format de table](https://share.streamlit.io/mesmith027/streamlit_webapps/main/MC_pi/streamlit_app.py)")


st.sidebar.subheader("2. Upload des fichiers pickle")
estimator = st.sidebar.file_uploader("estimator")
scaler = st.sidebar.file_uploader("scaler")

# df = pd.read_csv(file, sep=",", decimal=".").reset_index()
# st.dataframe(df)

estimator = pickle.load(open('estimator.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))