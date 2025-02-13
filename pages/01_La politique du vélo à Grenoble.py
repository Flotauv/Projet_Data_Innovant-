import streamlit as st 
import pandas as pd
import os
import re 
import altair as alt
st.set_page_config(page_title='Politiques autour du vélo à Grenoble',layout='wide')
## Titre
st.title("Politiques autour du vélo à Grenoble")

st.write("Cette page présente les mesures phare qui ont pu être prises pour favoriser la politique nationale à propos du vélo dans l'agglomération Grenobloise")

## Création des fonctions 

### Affichage du traffic routier

#### Chemin du dossier 
#source : https://www.data.gouv.fr/fr/datasets/trafic-moyen-journalier-annuel-sur-le-reseau-routier-national/'
repertory_traffic = 'BaseDeDonnées/Traffic_routier/'

#### Fonction qui retourne les axes routiers de Grenoble et leur taux moyens journaliers sur l'année
@st.cache_data()
def fct_transform_tmja_to_axes_routier(file):

    df = pd.read_csv(file, sep=None,engine='python')  
    ##Conversion en date pour extraire l'année
    df.columns = df.columns.str.lower()
    df.columns = df.columns.str.replace(r'_','',regex=True)
    df['datereferentiel'] = pd.to_datetime(df['datereferentiel'])
    df['annee'] = df['datereferentiel'].dt.year
    
    ##Filtre sur les routes du département de l'Isère
    df = df[df['depprd'] == 38]
    df = df.dropna()  # Il y en a très peu
    
    df['longueur'] = df['longueur'].str.replace(',', '.')
    df['ratiopl'] = df['ratiopl'].str.replace(',', '.')
    df['ratiopl'] = df['ratiopl'].astype(float)
    
    df['ratiopl'] = df['ratiopl']/100
    df['nb_poids_lourds'] = round(df['tmja'] * df['ratiopl'])
    
    ##axe routier
    df = df.rename(columns={'route': 'Axe routier'})
    df['Axe routier'] = df['Axe routier'].replace('A0041', 'A41')
    df['Axe routier'] = df['Axe routier'].replace('A0048', 'A48')
    df['Axe routier'] = df['Axe routier'].replace('A00480', 'A48')
    df['Axe routier'] = df['Axe routier'].replace('N0087', 'Nationale 87')
    df['Axe routier'] = df['Axe routier'].replace('A0051N', 'A51')
    df['Axe routier'] = df['Axe routier'].replace('A0051', 'A51')

    
    liste_axes_ref=['A41','A48','A51','A480','Nationale 87']
    
    df = df[df['Axe routier'].isin(liste_axes_ref)]
    ## Création de la base de donnée avec les routes 
    df_axes_routier = df.groupby(['Axe routier', 'annee'])[[ 'tmja', 'nb_poids_lourds']].mean().reset_index().sort_values(by='tmja', ascending=False)
    
    df_axes_routier['ratiopl'] = round((df_axes_routier['nb_poids_lourds']/df_axes_routier['tmja'])*100)
    df_axes_routier['tmja']=round(df_axes_routier['tmja'])
    df_axes_routier['annee']=df_axes_routier['annee'].astype(str)
    df_axes_routier = df_axes_routier[(df_axes_routier['Axe routier'] != 'N0007') & (df_axes_routier['Axe routier'] != 'A0007N')]
    #df_axes_routier = df_axes_routier.rename(columns={'tmja': 'Taux Moyen Journalier Annualisé (en millier)'})
    
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
#source : https://www.data.gouv.fr/fr/datasets/bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-routiere-annees-de-2005-a-2023/
### Répertoires où se situent les fichiers dans le repository
repertory_caract = 'BaseDeDonnées/Accidents_france/Caractéristiques/'
repertory_vehicule = 'BaseDeDonnées/Accidents_france/Véhicules/'

files_vehi = [file for file in os.listdir(repertory_vehicule) if file!='.DS_Store']
files_caract = [file for file in os.listdir(repertory_caract) if file!='.DS_Store']

### Fct qui retourne la date du fichier caractéristique
@st.cache_data()
def fct_file_carac(file):
    df_accident = pd.read_csv(file,sep=None,engine='python',encoding='ISO-8859-1')
    if 'Accident_Id' in df_accident.columns:
        df_accident = df_accident.rename(columns={'Accident_Id': 'Num_Acc'})
    df_accident['Num_Acc'] = df_accident['Num_Acc'].astype(str)

    annee = df_accident.iloc[0]['Num_Acc'][:4]
    
    return int(annee)

### Fct qui retourne la date du fichier véhicule
@st.cache_data()
def fct_file_vehicule(file):
    df_vehicule = pd.read_csv(file,sep=None,engine='python')
    if 'Accident_Id' in df_vehicule.columns:
        df_vehicule = df_vehicule.rename(columns ={'Accident_Id':'Num_Acc'})
    df_vehicule['Num_Acc'] = df_vehicule['Num_Acc'].astype(str)
    annee = df_vehicule.iloc[0]['Num_Acc'][:4]
    return int(annee)

### Fct qui indique si les fichiers ont la même date 
@st.cache_data()
def fct_compatibilite(file_caract,file_vehicule):
    return fct_file_carac(file_caract)==fct_file_vehicule(file_vehicule)



@st.cache_data()
def fct_accidents(file_caracteristique, file_vehicules):
        df_accidents = pd.read_csv(file_caracteristique, sep=None,engine='python',encoding='ISO-8859-1')
        df_vehicules = pd.read_csv(file_vehicules, sep=None,engine='python')
        
        df_vehicules.columns = df_vehicules.columns.str.lower()
        df_accidents.columns = df_accidents.columns.str.lower()
        
        df_accidents.columns = df_accidents.columns.str.replace(r'_','',regex=True)
        df_vehicules.columns = df_vehicules.columns.str.replace(r'_','',regex=True)

        #df_accident = pd.re
        # Condition pour avoir les clefs primaires du même nom
        if 'accidentid' in df_accidents.columns:
            df_accidents = df_accidents.rename(columns={'accidentid': 'numacc'})
        # Condition pour avoir des fichiers de même année
        df_vehicules['numacc'] = df_vehicules['numacc'].astype(str)
        
        df_vehicules['numacc'] = df_vehicules['numacc'].astype(int)
        df_accidents = df_accidents[df_accidents['dep'] == '38']
        df_vehicules = df_vehicules[df_vehicules['catv'] == 1]
        df_accidents_grenoble = pd.merge(df_accidents, df_vehicules, how='inner', on='numacc')
        df_accidents_grenoble = df_accidents_grenoble[df_accidents_grenoble['catv'] == 1]

        df_accidents_grenoble = df_accidents_grenoble.rename(columns={'an':'Année'})
        df_accidents_grenoble['Année']= df_accidents_grenoble['Année'].astype(str)
        df = df_accidents_grenoble.groupby('Année')['numacc'].count().reset_index()
        df = df.rename(columns={'numacc':'Nombre accidents'})
        return df

### Fct de concaténation qui prend du temps notamment du aux boucles (À optimiser si possible )
@st.cache_data()
def fct_concat_acc():
    files_v = files_vehi
    files_c = files_caract
    df = pd.DataFrame()
    for file_carac in files_c:
        for file_vehi in files_v:
            if fct_compatibilite(repertory_caract+str(file_carac),repertory_vehicule+str(file_vehi))==True:
                df_accident = fct_accidents(repertory_caract+str(file_carac),repertory_vehicule+str(file_vehi))
                df = pd.concat([df,df_accident],ignore_index=False)
    return df
    


## Polution 
repertory_pollution = 'BaseDeDonnées/Pollution/Mesure_air/' #à changer certainement 

@st.cache_data()
def fct_pollution(file):
    df = pd.read_csv(file,sep=None,engine='python')
    
    ## Colonnes misent en minuscule
    df.columns = df.columns.str.lower()
    df['date_ech']= pd.to_datetime(df['date_ech'])
    df['annee']=df['date_ech'].dt.year
    
    ## Opérations sur les états 
    df['etat'] = df['etat'].astype(str)
    df['etat'] = df['etat'].replace('ALERTE SUR PERSISTANCE','ALERTE')
    df = df.rename(columns={'etat':'État de pollution'})
    df['com_court'].astype(str)
    df=df[df['lib_zone']=='Bassin Grenoblois']
    
    #Création premier dataframe groupé
    df = df.groupby(['annee','État de pollution'])['com_court'].count().reset_index()
    df = df.rename(columns = {'com_court':'Nombre_observations'})
    
    ## Création deuxième df 
    df_2 = df.groupby('annee')['Nombre_observations'].sum().reset_index()
    df_2 = df_2.rename(columns = {'Nombre_observations':'Nombre total observations'})
    
    ## Fusion des deux dataframes
    df = pd.merge(df,df_2,on='annee',how='left')
    
    ##Création de la colonne ratio
    df['Ratio'] = round(df['Nombre_observations']/df['Nombre total observations']*100)
    
    df = df.rename(columns = {'annee':'Années'})
    return df


@st.cache_data()
def fct_concat_pollution():
    df = pd.DataFrame()
    for file in os.listdir(repertory_pollution):
        if file !='.DS_Store':
            df_pollution = fct_pollution(repertory_pollution+str(file))
            df=pd.concat([df,df_pollution],ignore_index=True)
    df['Années']=df['Années'].astype(str)
    return df 

## Comptage 

### piétons permanents
@st.cache_data()
def fct_comptage_pietons_permanents(file):
    df = pd.read_csv(file,sep=None,engine='python')
    df=df[df['nom_comm']=='Grenoble']
    colonnes = df.columns[df.columns.str.startswith('tmj_')]
    colonnes = colonnes.tolist()
    colonnes.append('id')
    colonnes.append('localisation')
    df= df[colonnes]
    #df = pd.concat([df_concat_1,df_concat_2],ignore_index=False)
    colonnes = df.columns[df.columns.str.startswith('tmj_')]
    df = df.groupby('localisation')[colonnes].mean().reset_index()
    df = df.rename(columns={'localisation':'Localisation'})

    df = df.melt(id_vars='Localisation',value_name='valeur',var_name='tmj')
    df['tmj'] = df['tmj'].str.replace('tmj_','')

    return df

### vélos permanents 
@st.cache_data()
def fct_comptage_velos_permanents(file):
    df = pd.read_csv(file,sep=None,engine='python')
    df=df[df['nom_comm']=='Grenoble']
    df=df.dropna()
    colonnes = df.columns[df.columns.str.startswith('tmj')]
    colonnes = colonnes.tolist()
    colonnes.append('id')
    colonnes.append('localisation')
    df= df[colonnes]
    #df = pd.concat([df_concat_1,df_concat_2],ignore_index=False)
    colonnes = df.columns[df.columns.str.startswith('tmj_')]
    df = df.groupby('localisation')[colonnes].mean().reset_index()
    df = df.rename(columns={'localisation':'Localisation'})
    df = df.melt(id_vars='Localisation',value_name='valeur',var_name='tmj')
    df['tmj'] = df['tmj'].str.replace('tmj_','')
    return df





##Création colonnes
col_image_principale , col_image_second = st.columns([3,0.1])
col_traffic_principale, col_traffic_second = st.columns([3,0.1])
col_accident_principale,col_accident_second = st.columns([3,0.1])
col_pollution_princiaple,col_pollution_second = st.columns([3,0.1])
#col_source_principale,col_source_second = st.columns([3,0.1])
col_comptage_pietons_permanent_principale , col_comptage_pietons_permanent_second = st.columns([3,0.1])
col_comptage_vélos_permanent_principale , col_comptage_vélos_permanent_second = st.columns([3,0.1])









with col_image_principale:
    st.image('Screens/politiques_grenoble.jpeg',use_container_width=True)
    st.write('Plusieurs mesures phares qui englobent un large périmètre')

    
with col_traffic_principale:
    st.subheader('Évolution du traffic autour de Grenoble',divider=True)
    st.line_chart(data=fct_concat(),
                  x='annee',
                  y='tmja',
                  color='Axe routier',
                  x_label='Années',
                  y_label="Taux Moyen Journalier (en millier) ",
                  width=900,
                  height=500
                  )

    
with col_accident_principale:
    st.subheader('Nombre d\'accidents dans la métropole Grenobloise impliquant un vélo',divider=True)
    st.line_chart(data=fct_concat_acc(),
                 x='Année',
                 y='Nombre accidents',
                 x_label='Années',
                 y_label="Nombre d'accidents",
                 width=900,
                 height=500)

with col_pollution_princiaple:
    st.subheader('Nombre de relevés et états de pollution de l\'agglomération Grenobloise',divider=True)
    chart = alt.Chart(fct_concat_pollution()).mark_bar().encode(
        x='Années',
        y='Nombre_observations',
        color=alt.Color('État de pollution',scale=alt.Scale(
            domain=['PAS DE DEPASSEMENT','ALERTE'],
            range=['green','red'])
            )
    ).properties(width = 900 ,height = 500 )
    st.altair_chart(chart)

    
    
with col_comptage_pietons_permanent_principale:
    st.subheader(body='Comptage du nombre de piétons par jours annualisé suivant différentes zones géographiques de Grenoble',divider=True)
    st.bar_chart(data=fct_comptage_pietons_permanents('BaseDeDonnées/Comptage_mode_deplacement/comptages_pietons_permanents.csv'),
                  x='tmj',
                  y='valeur',
                  color='Localisation',
                  x_label='Années',
                  y_label='Taux moyen journalier (en millier)',
                  stack=False,
                  width=900,
                  height=500)
    
with col_comptage_vélos_permanent_principale:
    st.subheader(body='Évolution du nombre de vélos par jours annualisé suivant différentes zones au sein de Grenoble',divider=True)
    st.bar_chart(data=fct_comptage_velos_permanents('BaseDeDonnées/Comptage_mode_deplacement/comptages_velos_permanents.csv'),
                 x='tmj',
                 y='valeur',
                 x_label='Années',
                 y_label='Taux moyen journalier (en millier)',
                 color='Localisation',
                 stack=False,
                 width=900,
                 height=500)
    