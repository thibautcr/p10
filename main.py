import streamlit as st
import pandas as pd
# import requests as re
# import json
# import matplotlib.pyplot as plt


header = st.container()
data_set = st.container()
features = st.container()
modelTraining = st.container()

# st.set_page_config(page_title="App détection billet")

# st.title("Application de détection des faux billets")

with header: 
	st.title('application web détection')
	
st.markdown("""<style>.streamlit-expanderHeader{font-size: 17px;}</style>
<div style="text-align: justify;">Cette application Streamlit, développée dans le cadre du projet 10 de la formation Data Analyst v2 d'OpenClassrooms, utilise un modèle d'apprentissage supervisé de classification (Régression logistique) servant d'API afin de détecter les billets frauduleux en fonction de leurs dimensions.</div>""", unsafe_allow_html=True)
st.write("""Vous pouvez:  
- Rentrer manuellement les dimensions d'un billet dans la bar sur le côté.  
- Charger un fichier *csv* qui devra être encodé en utf-8. Le fichier doit ressembler à cela et les colonnes doivent correspondre :""")

file = st.file_uploader("Dans un premier temps, vous devez déposer votre fichier au format .csv")

option = st.radio("Quel type de billet souhaitez-vous visualiser ?", ("Tous les billets", "Uniquement les faux"), 1)

