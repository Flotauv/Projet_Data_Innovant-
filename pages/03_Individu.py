import streamlit as st 
import pandas as pd 
st.title('Indicateurs liés au cycliste')

colonne_1,colonne_2 = st.columns(2)

with colonne_1:
    st.subheader('Nombre d\'accidents dans l\'agglomération Grenobloise',
              divider='gray')
    
    # Définition de la fonction
    def fct_accidents(file_caracteristique, file_vehicules):
        df_accidents = pd.read_csv(file_caracteristique, sep=';')
        df_vehicules = pd.read_csv(file_vehicules, sep=';')
        # Condition pour avoir les clefs primaires du même nom
        if 'Accident_Id' in df_accidents.columns:
            df_accidents = df_accidents.rename(
                columns={'Accident_Id': 'Num_Acc'})
        # Condition pour avoir des fichiers de même année
        df_vehicules['Num_Acc'] = df_vehicules['Num_Acc'].astype(str)
        if df_accidents['an'][0]+int(df_vehicules.iloc[0]['Num_Acc'][:4]) != df_accidents['an'][0]*2:
            print('Les fichiers comparés sont de la mauvaise année, l\'un l\'année {} et l\'autre l\'année {}'.format(
                int(df_vehicules['Num_Acc'][0].str[:4]), df_accidents['ann'][0]))

        df_vehicules['Num_Acc'] = df_vehicules['Num_Acc'].astype(int)
        df_accidents = df_accidents[df_accidents['dep'] == '38']
        df_vehicules = df_vehicules[df_vehicules['catv'] == 1]
        df_accidents_grenoble = pd.merge(
            df_accidents, df_vehicules, how='inner', on='Num_Acc')
        df_accidents_grenoble = df_accidents_grenoble[df_accidents_grenoble['catv'] == 1]

        annee = df_accidents.iloc[0]['an']
        return len(df_accidents_grenoble), annee

    st.metric(label="Nombre total d'\'accidents durant l\'année {}".format(fct_accidents('BaseDeDonnées/Accidents_france/carcteristiques-2022.csv', 'BaseDeDonnées/Accidents_france/vehicules-2022.csv')[1]),
              value=fct_accidents('BaseDeDonnées/Accidents_france/carcteristiques-2022.csv',
                                  'BaseDeDonnées/Accidents_france/vehicules-2022.csv')[0],
              delta=3, delta_color="inverse",border=True)