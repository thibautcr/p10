import streamlit as st
import pandas as pd
import requests as re
import json
import matplotlib.pyplot as plt


header = st.container()
data_set = st.container()
features = st.container()
modelTraining = st.container()

# st.set_page_config(page_title="App détection billet")

# st.title("Application de détection des faux billets")

with header: 
	st.title('Détection de faux billets')
	
st.markdown("""<style>.streamlit-expanderHeader{font-size: 17px;}</style>
<div style="text-align: justify;">Cette application Streamlit, développée dans le cadre du projet 10 de la formation Data Analyst v2 d'OpenClassrooms, utilise un modèle d'apprentissage supervisé de classification (Régression logistique) servant d'API afin de détecter les billets frauduleux en fonction de leurs dimensions.</div>""", unsafe_allow_html=True)
st.write("""explication structure dataset""")

st.header("Drop file section)
file = st.file_uploader("Dans un premier temps, vous devez déposer votre fichier au format .csv")

option = st.radio("Quel type de billet souhaitez-vous visualiser ?", ("Tous les billets", "Uniquement les faux"), 1)



if st.button("Analyses"):
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
    else:
        values = file.to_dict()
        res = re.post(f"https://app-detection-billet.herokuapp.com/multipredict",json=values)
        json_str = json.dumps(res.json())
        resp = json.loads(json_str)
        
        #Traitement de la réponse
        data = pd.DataFrame(resp["0"].values(), index=resp["0"].keys(), columns=["Proba"])
        data["Prediction"] = data["Proba"]>=0.62

        #Création d'un pie chart
        l = data["Prediction"].value_counts().index.tolist() #Transformation des index en liste 
        l = list(map(lambda x: str(x).replace("False", 'Faux billets').replace("True", 'Vrais billets'), l)) #Remplacement des booléens par Vrai/Faux
        def generateur(): #Création d'un générateur pour l'argument autopct de Matplotlib
            for i in range(2):
                yield l[i]
                
        gen = generateur() #initialisation du générateur
        fig, ax = plt.subplots()
        ax.pie(data["Prediction"].value_counts(), autopct= lambda p: f'{p:.2f}%\n {p*data.shape[0]/100:.0f} {next(gen)}', labels=l) #On utilise next(gen) pour itérer sur le générateur et ainsi le nombre de billet est labellisé avec Vrais/Faux
        
        data.index.name = "Id"
        down = pd.DataFrame(data.loc[data["Prediction"] == False].index).to_csv(header=False, index=False).encode('utf-8')
        down2 = data.to_csv().encode('utf-8')
        
        
        
        #Divison en 2 parties:
        col1, col2  = st.columns(2)
        
        col1.pyplot(fig)
        
        
        if option == "Uniquement les faux":
            if len(data.loc[data["Prediction"]==False]) > 5:
                col2.expander("Liste des identifiants des faux billets:").write(data.loc[data["Prediction"]==False])
            else:
                col2.write(data.loc[data["Prediction"]==False])
            col2.download_button(label = "Télécharger l'id des faux billets", data= down, file_name='Faux_billets.csv', help="fichier csv encodé en *utf-8*")
            
        elif option == "Tous les billets":
            if len(data) >5:
                col2.expander("Liste des identifiants des billets:").write(data)
            else:
                col2.write(data)
            col2.download_button(label = "Télécharger", data= down2, file_name='Billets.csv', help="fichier csv encodé en *utf-8*")

