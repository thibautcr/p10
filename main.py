import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt


header = st.container()
data_set = st.container()
features = st.container()
modelTraining = st.container()

# st.set_page_config(page_title="App détection billet")

# st.title("Application de détection des faux billets")

with header: 
	st.title('Détection de faux billets')

# 1. Read me	
st.header("Read me")
st.markdown("""<style>.streamlit-expanderHeader{font-size: 17px;}</style>
<div style="text-align: justify;">Cette application Streamlit, développée dans le cadre du projet 10 de la formation Data Analyst v2 d'OpenClassrooms, utilise un modèle d'apprentissage supervisé de classification (Régression logistique) servant d'API afin de détecter les billets frauduleux en fonction de leurs dimensions.</div>""", unsafe_allow_html=True)
st.write("""explication structure dataset""")
st.write("""Le notebook du modèle, les scripts FastAPI, Streamlit et Dockerfiles sont disponibles sur [GitHub](https://).""")

# 2. Dépot de fichier
st.header("Drop a file section")
file = st.file_uploader("Dans un premier temps, vous devez déposer votre fichier au format .csv")

option = st.radio("Quel type de billet souhaitez-vous visualiser ?", ("Tous les billets", "Uniquement les faux"), 1)

# 3. Analyse du fichier

url_estimator = "https://github.com/thibautcr/p10/blob/06e4a1a72aa488f7c1b9aa407c5b8393946025e2/estimator.pkl?raw=true"
url_scaler =  "https://github.com/thibautcr/p10/blob/06e4a1a72aa488f7c1b9aa407c5b8393946025e2/scaler.pkl?raw=true"

estimator = pd.read_pickle(url_estimator) 
scaler = pd.read_pickle(url_scaler) 

st.header("Analyse des billets")
st.write("""En cliquant sur le bouton "Execute" ci-dessous, notre algorithme de prédiction viendra analyser les billets contenu dans le fichier :
1. d'une part, en respectant les parametres optimaux que nous lui calculé
2. d'autre part, en réutilisant les valeurs observées dans son entrainement préalable sur les 1200 billets du jeu d'entrainement""")
if st.button("Execute"):
    try:
        file = pd.read_csv(file, sep=",", decimal=".")
        if file.shape[1] != 7:
            raise Exception("Le fichier n'a pas le nombre de colonnes attendues, vérifiez l'encodage (utf8; sep = ',' ; dec = '.') ou les colonnes fournies.")
        elif not (file.columns == ['diagonal', 'height_left', 'height_right', 'margin_low', 'margin_up','length', 'id']).all():
            raise Exception('Les colonnes entrées ne correspondent pas au schéma ci-dessus, vérifiez le nom des colonnes')
        elif file[["id"]].duplicated().any():
            raise Exception('Attention il y a des doublons dans la colonne "id".')
        file.rename(columns={"id":"ide"}, inplace=True)
    except UnicodeDecodeError:
        st.write('Vérifiez que votre fichier est un fichier *csv* encodé en utf-8 avec comme séparateur décimal un "." et comme séparateur de valeurs une ",".')
    except ValueError:
        st.write("Veuillez sélectionner un fichier existant.")
	
	
# 4. Entrainement du modèle
st.header("""Entrainement du modèle""")
st.write("""méthodologie utlisée : pistes explorées, entrainement, optimisation, ..., résultats ,""")


st.markdown("""Thibaut Cressent""")
