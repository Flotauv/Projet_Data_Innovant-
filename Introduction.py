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
st.title('Ces villes qui ont adopté le vélo comme mobilité douce')

st.write('Il peut être intéressant de voir ce que certaines villes ont mis en place concernant leur ')
##Création de colonnes
#col1,col2= st.columns(2)
col_stockholm_grande , col_stockholm_petite = st.columns([3,0.1])
col_stras_grande , col_stras_petite = st.columns([3,0.1])


#col3,col4 = st.columns([3,0.1])




with col_stockholm_grande:
    st.subheader('Stockholm et Copenhague : Deux villes qui ne lâchent pas la pédalle',divider=True)
    st.write('2004 : Green Wave, projet qui permet aux cyclistes de ne pas s\'arrêter continuellement à chaque intersection ou feux rouges, le tout en fluidifiant le traffic des vélos et assurant une sécurité optimale')
    st.write('2015 : Walkable city qui veut encourager la marche , le vélo et les transports en communs auprès des habitants avec plus de 7000 m2 de pistes cyclables et une taxe de congestion du traffic automobile au centre ville.')
    st.write('2018-2023 : Stockholm eBikes, projet d\'installation de plus de 120 stations de location de vélos électriques réparties dans la ville avec plus de 5000 vélos électriques disponibles, c\'est le plus gros projet de vélos électriques en Europe du Nord')
    st.write('2014 - 2024  : 200 millions d\'euros dépensés par la ville de Copenhague dans les infrastructures cyclables pour plus de 400 km de pistes cyclables' )

    col1,col2 = st.columns(2)
    with col1:
        st.image('Screens/Gree_wave.jpg.webp',caption='Green Wave : marquage au sol pour les vélos',width=300)
    with col2:
        st.image('Screens/bike_vs_cars.jpg.webp',caption='Conséquences des politiques menées à Copenhague sur les modalités de déplacements',width=400)
with col_stras_grande:
    st.subheader('Strasbourg : Une ville qui prend l\'aspiration',divider=True)
    st.write('2013 : VéloStras projet qui a pour but d\'équiper la ville d\'axes cyclable la traversant du Nord au Sud et de l\'Est à l\'Ouest')
    st.write('2019 : Plan Action pour les Mobilités Actives (PAMA) qui veut consolider la place que possède la ville dans le classement des métropoles utilisant les mobilités douces , pour péréniser l\'utilisation du vélo en ville ')
    st.write('2021 : Le "Plan vélo" qui a pour but de faire rejoindre les communes de deuxième couronne  au centre ville de Strasbourg')
    st.write('2025 : L\'arrivée de plus de 5000 vélos disponibles en location libre ainsi que plus de 1200 vélos à assistance électrique')
    col1,col2 = st.columns(2)
    with col1:
        st.image('Screens/velostras.jpg',caption='Projet VéloStras')
#with col_stras_petite:
    #st.image('Screens/velostras.jpg')
#ith col3:
    #st.subheader('Grenoble : Une vile qui mouille le maillot ',divider=True)







## Définition de la page de garde

def main():
    st.header('Introduction') #Bien faire attention que le nom soit le même que le fichier
    st.title('Dashboard mobilité')



if __name__ == '__main()__':
    main()

