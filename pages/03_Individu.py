import streamlit as st
import pandas as pd
import os
st.title('Indicateurs liés au cycliste')

colonne_1, colonne_2 = st.columns(2)

## fct qui indique l'année du fichier caractéristique 
def fct_file_carac(file):
    df_accident = pd.read_csv(file,sep=';')
    if 'Accident_Id' in df_accident.columns:
        df_accident = df_accident.rename(columns={'Accident_Id': 'Num_Acc'})
    df_accident['Num_Acc'] = df_accident['Num_Acc'].astype(str)

    annee = df_accident.iloc[0]['Num_Acc'][:4]
    
    return int(annee)

## fct qui indique l'année du fichier véhicule 
def fct_file_vehicule(file):
    df_vehicule = pd.read_csv(file,sep=';')
    if 'Accident_Id' in df_vehicule.columns:
        df_vehicule = df_vehicule.rename(columns ={'Accident_Id':'Num_Acc'})
    df_vehicule['Num_Acc'] = df_vehicule['Num_Acc'].astype(str)
    annee = df_vehicule.iloc[0]['Num_Acc'][:4]
    return int(annee)




def fct_accidents(file_caracteristique, file_vehicules):
        df_accidents = pd.read_csv(file_caracteristique, sep=';')
        df_vehicules = pd.read_csv(file_vehicules, sep=';')
        # Condition pour avoir les clefs primaires du même nom
        if 'Accident_Id' in df_accidents.columns:
            df_accidents = df_accidents.rename(columns={'Accident_Id': 'Num_Acc'})
        # Condition pour avoir des fichiers de même année
        #df_vehicules['Num_Acc'] = df_vehicules['Num_Acc'].astype(str)
        df_vehicules['Num_Acc'] = df_vehicules['Num_Acc'].astype(int)
        df_accidents = df_accidents[df_accidents['dep'] == '38']
        df_vehicules = df_vehicules[df_vehicules['catv'] == 1]
        df_accidents_grenoble = pd.merge(
            df_accidents, df_vehicules, how='inner', on='Num_Acc')
        df_accidents_grenoble = df_accidents_grenoble[df_accidents_grenoble['catv'] == 1]

        df_vehicules['Num_Acc'] = df_vehicules['Num_Acc'].astype(str)
        annee = df_vehicules.iloc[0]['Num_Acc'][:4]
        return (len(df_accidents_grenoble), int(annee))

def fct_compatibilite(file_caract,file_vehicule):
    return fct_file_carac(file_caract)==fct_file_vehicule(file_vehicule)


repertory_caract = 'BaseDeDonnées/Accidents_france/Caractéristiques/'
repertory_vehicule = 'BaseDeDonnées/Accidents_france/Véhicules/'
L_accidents=[]
L_file_caract = []
L_file_vehicule = []
for file in os.listdir(repertory_caract):
    if file != '.DS_Store':
        L_file_caract.append(file)

for file in os.listdir(repertory_vehicule):
    if file != '.DS_Store':
        L_file_vehicule.append(file)
        
for file_caract in L_file_caract:
    for file_vehicule in L_file_vehicule:
        if fct_compatibilite(repertory_caract+str(file_caract),repertory_vehicule+str(file_vehicule))==True:
           L_accidents.append((fct_accidents(repertory_caract+str(file_caract),repertory_vehicule+str(file_vehicule))))

df_accidents = pd.DataFrame(L_accidents, columns = ['Nombre accidents','Année'])
#df_accidents['Année'] = df_accidents['Année'].replace(',','')



with colonne_1:
    st.subheader('Nombre d\'accidents dans l\'agglomération Grenobloise',divider='gray')

    st.bar_chart(df_accidents,x='Année',y='Nombre accidents',use_container_width=True)
    st.dataframe(df_accidents)
    


    st.metric(label="Nombre total d'\'accidents durant l\'année {}".format(fct_accidents('BaseDeDonnées/Accidents_france/Caractéristiques/carcteristiques-2022.csv', 'BaseDeDonnées/Accidents_france/Véhicules/vehicules-2022.csv')[1]),
              value=fct_accidents('BaseDeDonnées/Accidents_france/Caractéristiques/carcteristiques-2022.csv',
                                  'BaseDeDonnées/Accidents_france/Véhicules/vehicules-2022.csv')[0],
              delta=3, delta_color="inverse", border=True)
