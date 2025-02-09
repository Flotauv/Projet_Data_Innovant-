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

st.title('Politique nationales en faveur des mobilités douces ')
### Image des politiques nationales voulues pour la France 
st.image('Screens/politiques_nationales.jpeg',width=900)

st.write(" Au niveau national plusieurs actions ont été mises en place pour pousser l'utilisation des modes de transport qualifiés de mobilités douces. ")
st.write("Le sujet des mobilités douces notamment le vélo, n'est pas un cas propre à Grenoble, il est toujours intéressant de voir ce qu'il se passe ailleur pour pouvoir comparer, prendre exemple ou bien éviter certaines erreurs.")
st.write("Notre priorité sera de sortir certaines données relatives au vélo pour évaluer l'impact des politiques menées en faveur des mobilités douces.")


st.header('Ces villes européennes qui ont adopté le vélo comme mobilité douce')


##Création des colonnes et des titres liés

st.subheader('Stockholm et Copenhague : Deux villes qui ne lâchent pas la pédalle',divider=True)
col_stockholm_grande , col_stockholm_petite = st.columns([3,0.1])

st.subheader('Strasbourg : Une ville qui prend l\'aspiration',divider=True)
col_stras_grande , col_stras_petite = st.columns([1,1])


st.subheader("Bilan : Les infrastructures font chauffer les watts ",divider=True)
st.write("Ces villes considérées comme en avance sur le développement de la mobilité à vélo ont su prendre, dès le début des années 2000 voir 2010, des mesures qui favorisent l'essort du vélo en ville.")
st.write("Un élément clé de succès c'est le nombre de pistes cyclables et les kilomètres que celles-ci recouvrent qui est un atout majeur dans le développement du vélo en ville.")
st.write("Un réseau connecté , où les pistes sont larges, à l'écart des voitures et où l'on doit peu s'arrêter ou faire des détours justifie le nombre croissant d'utilisateurs à vélo.")
st.write("La voiture, ennemi juré des cyclistes qui est un frein au développement des infrastructures cyclables, doit voir son nombre d'utilisateurs quotidien baisser pour favoriser l'essort du vélo en ville.")
st.write("L'électrique devient un autre levier fort dans le développement des mobilités douces, il permet de toucher plus de personnes réticentes à l'utilisation du vélo.")

with col_stockholm_grande:

    
    st.write('2004 : Green Wave, projet qui permet aux cyclistes de ne pas s\'arrêter continuellement à chaque intersection ou feux rouges, le tout en fluidifiant le traffic des vélos et assurant une sécurité optimale')
    st.write('2015 : Walkable city qui veut encourager la marche , le vélo et les transports en communs auprès des habitants avec plus de 7000 m2 de pistes cyclables et une taxe de congestion du traffic automobile au centre ville.')
    st.write('2018-2023 : Stockholm eBikes, projet d\'installation de plus de 120 stations de location de vélos électriques réparties dans la ville avec plus de 5000 vélos électriques disponibles, c\'est le plus gros projet de vélos électriques en Europe du Nord')
    st.write('2014 - 2024  : 200 millions d\'euros dépensés par la ville de Copenhague dans les infrastructures cyclables pour plus de 400 km de pistes cyclables' )

    col1,col2 = st.columns(2)

    with col1:

        st.image('Screens/Gree_wave.jpg.webp',caption='Green Wave : marquage au sol pour les vélos',width=400)

    with col2:

        st.image('Screens/bike_vs_cars.jpg.webp',caption='Conséquences des politiques menées à Copenhague sur les modalités de déplacements',width=480)

with col_stras_grande:
    
    
    st.image('Screens/velostras.jpg',caption='Projet VéloStras',width=400)

with col_stras_petite:
    st.write(" ")
    st.write('2013 : VéloStras projet qui a pour but d\'équiper la ville d\'axes cyclable la traversant du Nord au Sud et de l\'Est à l\'Ouest')
    st.write('2019 : Plan Action pour les Mobilités Actives (PAMA) qui veut consolider la place que possède la ville dans le classement des métropoles utilisant les mobilités douces , pour péréniser l\'utilisation du vélo en ville ')
    st.write('2021 : Le "Plan vélo" qui a pour but de faire rejoindre les communes de deuxième couronne  au centre ville de Strasbourg')
    st.write('2025 : L\'arrivée de plus de 5000 vélos disponibles en location libre ainsi que plus de 1200 vélos à assistance électrique')

    

    









## Définition de la page de garde

def main():
    st.header('Introduction') #Bien faire attention que le nom soit le même que le fichier
    st.title('Dashboard mobilité')



if __name__ == '__main()__':
    main()

