import streamlit as st 
import pandas as pd
import os
st.set_page_config(page_title='Politiques autour du vélo à Grenoble',layout='centered')
## Titre
st.title("Politiques autour du vélo à Grenoble")

st.write("Cette page présente les mesures phare qui ont pu être prises pour favoriser la politique nationale à propos du vélo dans l'agglomération Grenobloise")

## Création des fonctions 

### Affichage du traffic routier

#### Chemin du dossier 

repertory_traffic = 'BaseDeDonnées/Traffic_routier/'

#### Fonction qui retourne les axes routiers de Grenoble et leur taux moyens journaliers sur l'année
@st.cache_data()
def fct_transform_tmja_to_axes_routier(file):

    df_tmja = pd.read_csv(file, sep=None,engine='python')  
    ##Conversion en date pour extraire l'année
    df_tmja.columns = df_tmja.columns.str.lower()
    df_tmja.columns = df_tmja.columns.str.replace(r'_','',regex=True)
    df_tmja['datereferentiel'] = pd.to_datetime(df_tmja['datereferentiel'])
    df_tmja['annee'] = df_tmja['datereferentiel'].dt.year
    
    ##Filtre sur les routes du département de l'Isère
    df_tmja = df_tmja[df_tmja['depprd'] == 38]
    df_tmja = df_tmja.dropna()  # Il y en a très peu
    
    df_tmja['longueur'] = df_tmja['longueur'].str.replace(',', '.')
    df_tmja['ratiopl'] = df_tmja['ratiopl'].str.replace(',', '.')
    df_tmja['ratiopl'] = df_tmja['ratiopl'].astype(float)
    
    df_tmja['ratiopl'] = df_tmja['ratiopl']/100
    df_tmja['nb_poids_lourds'] = round(df_tmja['tmja'] * df_tmja['ratiopl'])
    ## Création de la base de donnée avec les routes 
    df_axes_routier = df_tmja.groupby(['route', 'annee'])[[ 'tmja', 'nb_poids_lourds']].mean().reset_index().sort_values(by='tmja', ascending=False)
    
    df_axes_routier['ratiopl'] = round((df_axes_routier['nb_poids_lourds']/df_axes_routier['tmja'])*100)
    df_axes_routier['tmja']=round(df_axes_routier['tmja'])
    df_axes_routier['annee']=df_axes_routier['annee'].astype(str)
    df_axes_routier = df_axes_routier[(df_axes_routier['route'] != 'N0007') & (df_axes_routier['route'] != 'A0007N')]
    df_axes_routier = df_axes_routier.rename(columns={'tmja': 'Taux Moyen Journalier Annualisé (en Millions)'})
    
    df_axes_routier = df_axes_routier.rename(columns={'route': 'Axe routier'})

    df_axes_routier['Axe routier'] = df_axes_routier['Axe routier'].replace('A0041', 'A41')
    df_axes_routier['Axe routier'] = df_axes_routier['Axe routier'].replace('A0043', 'A43')
    df_axes_routier['Axe routier'] = df_axes_routier['Axe routier'].replace('A0007', 'A7')
    df_axes_routier['Axe routier'] = df_axes_routier['Axe routier'].replace('A0048', 'A48')
    df_axes_routier['Axe routier'] = df_axes_routier['Axe routier'].replace('A0049', 'A49')
    df_axes_routier['Axe routier'] = df_axes_routier['Axe routier'].replace('N0085', 'Nationale 85')
    df_axes_routier['Axe routier'] = df_axes_routier['Axe routier'].replace('N0087', 'Nationale 87')
    df_axes_routier['Axe routier'] = df_axes_routier['Axe routier'].replace('A0051N', 'A51')
    
    return df_axes_routier

#### Fonction de concatenation 
@st.cache_data()
def fct_concat():
    L=[]
    for file_2 in os.listdir('BaseDeDonnées/Traffic_routier'):
        if file_2!='.DS_Store':
            L.append(file_2)
    df = fct_transform_tmja_to_axes_routier(repertory_traffic+str(L[0]))
    for i in range(1,len(L)):
    #df_0 = fct_transform_tmja_to_axes_routier(repertory_traffic+str(L[0]))
    #df=fct_transform_tmja_to_axes_routier(repertory_traffic+str(L[i]))
        df = pd.concat([df,fct_transform_tmja_to_axes_routier(repertory_traffic+str(L[i]))])

    return df



## Accidents

##Création colonnes
col_image_principale , col_image_second = st.columns([3,0.1])
col_traffic_principale, col_traffic_second = st.columns([3,0.1])

with col_image_principale:
    st.image('Screens/politiques_grenoble.jpeg')
    st.write('Plusieurs mesures phares qui englobent un large périmètre')
with col_traffic_principale:
    st.subheader('Évolution du traffic autour de Grenoble',divider=True)
    st.bar_chart(data=fct_concat(),
                  x='Axe routier',
                  y='Taux Moyen Journalier Annualisé (en Millions)',
                  color='annee',
                  x_label='Axes routiers',
                  y_label='Tmja (en milliers)')
    
    

