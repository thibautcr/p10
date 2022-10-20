import streamlit as st

st.title("Application de détection")

st.sidebar.title('Drop a file section')
st.sidebar.write('Dans un premier temps, vous devez déposer les fichiers nécessaires')
st.sidebar.header("1. Upload le fichier CSV")
st.sidebar.write("Exemple du format fichier")
# st.markdown("[![Exemple du format fichier](http://www.google.com.au/images/nav_logo7.png)](http://google.com.au/)")
df = st.sidebar.file_uploader("Deposez votre fichier au format .csv")
st.markdown('''
    <a href="https://docs.streamlit.io">
        <img src="https://media.tenor.com/images/ac3316998c5a2958f0ee8dfe577d5281/tenor.gif" />
    </a>''',
    unsafe_allow_html=True
)

st.sidebar.header("2. Upload des fichiers pickle")
estimator = st.sidebar.file_uploader("estimator")
scaler = st.sidebar.file_uploader("scaler")
