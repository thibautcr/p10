import streamlit as st
import pandas as pd
import cPickle
import sklearn

st.title("Application de détection")

# SIDEBAR
st.sidebar.title('Drop a file section')

st.sidebar.header("1. Upload le fichier CSV")
file = st.sidebar.file_uploader("Deposez votre fichier au format .csv")
st.sidebar.write("[Exemple du format de table](https://share.streamlit.io/mesmith027/streamlit_webapps/main/MC_pi/streamlit_app.py)")

# st.sidebar.header("2. Upload des fichiers pickle")
# estimator = st.sidebar.file_uploader("estimator")
# scaler = st.sidebar.file_uploader("scaler")
# if estimator is not None:
# 	estimator = pickle.loads(estimator.read())
# if scaler is not None:
# 	scaler = pickle.loads(scaler.read())



# MAIN


# estimator = open("estimator.pkl",'rb')
# estimator = pickle.loads(estimator.read())
# scaler = open("scaler.pkl",'rb')
# estimator = pickle.loads(estimator.read())
# st.dataframe(pd.read_csv("billets_production.csv"))
estimator = pickle.load(open('pickle/estimator.pkl','rb'))

# pickle_estimator = open("estimator.pkl", "rb")
# estimator = pickle.load(pickle_estimator)

# if file is not None:
# 	df = pd.read_csv(file, sep=",", decimal=".").reset_index()
# 	df_index = df.id
# 	st.write("Fichier chargé!")
# 	if scaler is not None:
# 		# data_test = scaler.transform(df.loc[:,df.columns != "id"])
# 		st.write("Model loaded")
# 		st.write(scaler)
# 		# st.write(data_test)
