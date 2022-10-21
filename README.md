# README Projet 10

## 0. Scénario du projet
*Vous êtes consultant Data Analyst dans une entreprise spécialisée dans la data. Votre entreprise a décroché une prestation en régie au sein de l’Organisation nationale de lutte contre le faux-monnayage (ONCFM).
Cette institution a pour objectif de mettre en place des méthodes d’identification des contrefaçons des billets en euros.*

*Nous aimerions pouvoir mettre en concurrence deux méthodes de prédiction : la régression logistique classique et le K-means, duquel seront utilisés les centroïdes pour réaliser la prédiction.*

## 1. Description générale du projet

Le dossier que vous venez d’ouvrir contient les livrables répondant aux attentes du projet 10 de la formation de Data Analyst : Détectez les faux billets avec R ou Python.

Le travail est composé de deux notebooks fonctionnant "en série" :
- Projet 10.1 : traitements.ipynb
- Projet 10.2 : application.ipynb

## 2. Configuration du développeur

Version de Python utilisée : 3.7.13

Environnement de développement : Google Colaboratory

Version de l’OS : Windows 10

## 3. Installation du programme
Le premier notebook “10.1 : traitements” nécessite l’installation préalable des fichiers CSV fournis dans le projet :
- billet.csv
- billets_production.csv

Cependant, j'ai décidé d'héberger ces fichiers sur ma page github afin de faciliter leur importation. 

Vous pouvez retrouver ma page [GitHub ici](https://github.com/thibautcr/projet-10.git).

Par la suite, le second notebook “10.2 : applications” nécessite l’importation de certains fichiers contenus dans le premier notebook. Ces fichiers, au format pickle, sont notre estimateur et notre scaler de notre régression logistique permettant tous deux la classification des billets. Une commande d'exportation est située à la fin du notebook "traitements".

Ces fichiers, au format pkl, sont également hébergés sur ma page GitHub et ne nécessitent donc aucune importation. Cet hébergement permet, à mon sens, de rendre l'application plus facile à prendre en main pour les utilisateurs, notamment non-programmeurs.


## 4. Fonctionnalités

Mon approche sur le premier notebook se décompose en 5 parties :
1. Analyses exploratoires des données (uni-variées, bi-variées, et multi-variées)
2. Utilisation de la régression linéaire pour prédire les données manquantes
3. Clustering avec k-means
4. Classification avec la régression logistique
5. Exportation de notre algorithme et création de notre beta d'application.

La méthodologie employée est développée en markdown de chaque début de partie et des commentaires expliquent mon cheminement afin d'arriver à mes résultats.

Le second notebook a, quant à lui, pour unique objectif de prédire l'authenticité des billets qu'on lui importe, à partir d'un algorithme de régression logistique déjà entrainé et optimisé.

Je souhaiterai précisé qu'**une application Streamlit est en cours de développement**. Cependant, pour des **contraintes techniques et temporelles**, je n'ai pas encore trouver le moyen fonctionnel d'importer mes fichiers pickle dans l'application et je ne peux poursuivre ces travaux.
J'espère **résoudre ce problème technique afin de présenter l'application** directement sur la plateforme Streamlit que je trouve plus intuitive et ergonomique qu'un jupyter notebook. Vous pouvez retrouver [l'application ici]([https://github.com/thibautcr/projet-10.git](https://thibautcr-p10-streamlit-app-76hsts.streamlitapp.com))

Merci pour votre lecture!

Thibaut Cressent
