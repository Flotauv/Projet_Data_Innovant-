import streamlit as st 
st.set_page_config(page_title='Politiques autour du vélo à Grenoble',layout='centered')
## Titre
st.title("Politiques autour du vélo à Grenoble")

st.write("Cette page présente les mesures phare qui ont pu être prises pour favoriser la politique nationale à propos du vélo dans l'agglomération Grenobloise")
##Création colonnes
col_image_principale , col_image_second = st.columns([3,0.1])

with col_image_principale:
    st.image('Screens/politiques_grenoble.jpeg')

