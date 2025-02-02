import streamlit as st
import pandas as pd
import os 


##Configuration de la page 
st.set_page_config(
    page_title='Introduction',
    layout='wide',
    initial_sidebar_state='expanded'
    )
##Création du titre
st.title('Introduction  : Ces villes qui ont adopté le vélo comme mobilité douce')

##Création de colonnes
col1,col2= st.columns(2)
col3,col4 = st.columns([3,0.1])




with col1:
    st.subheader('Stockholm : Une ville qui ne lâche pas les pédalles',divider=True)

with col2:
    st.subheader('Strasbourg : Une ville qui prend l\'aspiration',divider=True)

with col3:
    st.subheader('Grenoble : Une vile qui mouille le maillot ',divider=True)







## Définition de la page de garde 
def main():
    st.header('HOME PAGE')
    st.title('Dashboard mobilité')



if __name__ == '__main()__':
    main()

