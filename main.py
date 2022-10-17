import streamlit as st
# import pandas as pd
# import requests as re
# import json
# import matplotlib.pyplot as plt


header = st.container()
data_set = st.container()
features = st.container()
modelTraining = st.container()

st.set_page_config(page_title="App détection billet")

st.title("Application de détection des faux billets")

with header: 
	st.title('application web détection')
