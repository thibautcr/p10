import streamlit as st
import pandas as pd
import pickle
import sklearn

st.title("Application de détection")

# SIDEBAR
st.sidebar.title('Drop a file section')

st.sidebar.header("1. Upload le fichier CSV")
file = st.sidebar.file_uploader("Deposez votre fichier au format .csv")
st.sidebar.write("[Exemple du format de table](https://share.streamlit.io/mesmith027/streamlit_webapps/main/MC_pi/streamlit_app.py)")

st.sidebar.header("2. Upload des fichiers pickle")
estimator = st.sidebar.file_uploader("estimator")
scaler = st.sidebar.file_uploader("scaler")


# MAIN
if file != None:
	df = pd.read_csv(file, sep=",", decimal=".").reset_index()
	df_index = df.id
	if scaler != None:
		data_test = scaler.transform(df.loc[:,df.columns != "id"])
		st.write(data_test)