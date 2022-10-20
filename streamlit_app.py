import streamlit as st

st.title("Application de détection")

st.sidebar.title('Drop a file section')

st.sidebar.header("1. Upload le fichier CSV")
df = st.sidebar.file_uploader("Deposez votre fichier au format .csv")
st.sidebar.write("[Exemple du format de table](https://share.streamlit.io/mesmith027/streamlit_webapps/main/MC_pi/streamlit_app.py)")


st.sidebar.header("2. Upload des fichiers pickle")
estimator = st.sidebar.file_uploader("estimator")
scaler = st.sidebar.file_uploader("scaler")


st.write("df")
st.dataframe(df)


df_git = pd.read_csv("billets_production.csv")
st.dataframe(df_git)