
import streamlit as st 
import pandas as pd 
import plotly.express as plx

st.set_page_config(layout="wide")
st.title("Dashboard récapitulatif environnement vélo Grenoble")
st.write("La première version de notre dashboard avec les tenants et les aboutissants de \
         ce que nous voulons montrer")

@st.cache_data
def read_csv_file(path):
    df=pd.read_csv(path,sep=';')
    return df







#df_axes_routier = df_axes_routier.rename(columns={'route':'Route'})
#st.subheader('Dataframes')
#with st.expander('Preview'):
    #st.dataframe(fct_transform_tmja_to_axes_routier())

## Figure 

col1_l1,col2_l1 = st.columns(2)
col1_l2,col2_l2 = st.columns(2) # Création des colonnes pour pouvoir mettre les graphiques 

with col1_l1:

    def fct_transform_tmja_to_axes_routier(file):
        df_tmja = pd.read_csv(file,sep=';')
        df_tmja['dateReferentiel'] = pd.to_datetime(df_tmja['dateReferentiel'])
        df_tmja['Annee'] = df_tmja['dateReferentiel'].dt.year
        df_tmja = df_tmja[df_tmja['depPrD']==38]
        df_tmja = df_tmja.dropna() # Il y en a très peu

        df_tmja['longueur']=df_tmja['longueur'].str.replace(',','.')
        df_tmja['ratio_PL']=df_tmja['ratio_PL'].str.replace(',','.')
        df_tmja['ratio_PL']=df_tmja['ratio_PL'].astype(float)
        df_tmja['ratio_PL']=df_tmja['ratio_PL']/100
        df_tmja['Nb_poids_lourds'] = round(df_tmja['TMJA']* df_tmja['ratio_PL'])
        df_axes_routier = df_tmja.groupby(['route','Annee'])[['longueur','TMJA','Nb_poids_lourds']].sum().reset_index().sort_values(by='TMJA',ascending=False)

        df_axes_routier['ratio_PL']=round((df_axes_routier['Nb_poids_lourds']/df_axes_routier['TMJA'])*100)
        #df_axes_routier = df_axes_routier.drop(columns=['Unnamed: 0'])
        df_axes_routier = df_axes_routier[(df_axes_routier['route']!='N0007')&(df_axes_routier['route']!='A0007N')]
        df_axes_routier = df_axes_routier.rename(columns={'TMJA':'Taux Moyen Journalier Annualisé (en Millions)'})
        df_axes_routier = df_axes_routier.rename(columns={'route':'Axe routier'})

        df_axes_routier['Axe routier']=df_axes_routier['Axe routier'].replace('A0041','A41')
        df_axes_routier['Axe routier']=df_axes_routier['Axe routier'].replace('A0043','A43')
        df_axes_routier['Axe routier']=df_axes_routier['Axe routier'].replace('A0007','A7')
        df_axes_routier['Axe routier']=df_axes_routier['Axe routier'].replace('A0048','A48')
        df_axes_routier['Axe routier']=df_axes_routier['Axe routier'].replace('A0049','A49')
        df_axes_routier['Axe routier']=df_axes_routier['Axe routier'].replace('N0085','Nationale 85')
        df_axes_routier['Axe routier']=df_axes_routier['Axe routier'].replace('N0087','Nationale 87')
        df_axes_routier['Axe routier']=df_axes_routier['Axe routier'].replace('A0051N','A51')


        return df_axes_routier

    fig = plx.bar(fct_transform_tmja_to_axes_routier('BaseDeDonnées/Grenoble/tmj_axes_routier.csv'),
                  
                x='Axe routier',
                y='Taux Moyen Journalier Annualisé (en Millions)',
                text='Taux Moyen Journalier Annualisé (en Millions)', )


    st.header('Indicateur 1 : Traffic routier de l\'agglomération Grenobloise',divider='gray')
    fig.update_traces(textposition = "outside")
    st.write('Traffic routier lié à l\'année  {}'.format(fct_transform_tmja_to_axes_routier('BaseDeDonnées/Grenoble/tmj_axes_routier.csv')['Annee'][0]))
    st.plotly_chart(fig,use_container_width=True)


with col2_l1:
    st.header('Nombre d\'accidents dans l\'agglomération Grenobloise',divider='gray')
    st.write('Indicateur permettant d\'avoir le nombre d\'accidents au sein de l\'agglomération Grenobloise')

    ## Définition de la fonction 

    def fct_accidents(file_caracteristique,file_vehicules):
        df_accidents = pd.read_csv(file_caracteristique,sep=';')
        df_vehicules = pd.read_csv(file_vehicules, sep=';')

        if 'Accident_Id' in df_accidents.columns:
            df_accidents = df_accidents.rename(columns={'Accident_Id':'Num_Acc'})

        df_vehicules['Num_Acc']= df_vehicules['Num_Acc'].astype(str)

        if df_accidents['an'][0]+int(df_vehicules.iloc[0]['Num_Acc'][:4]) != df_accidents['an'][0]*2:
            print('Les fichiers comparés sont de la mauvaise année, l\'un l\'année {} et l\'autre l\'année {}'.format(int(df_vehicules['Num_Acc'][0].str[:4]),df_accidents['ann'][0]))
        df_vehicules['Num_Acc'] = df_vehicules['Num_Acc'].astype(int)
        df_accidents = df_accidents[df_accidents['dep']=='38']
        df_vehicules = df_vehicules[df_vehicules['catv']==1]
        df_accidents_grenoble = pd.merge(df_accidents,df_vehicules, how='inner',on='Num_Acc')
        df_accidents_grenoble =df_accidents_grenoble[df_accidents_grenoble['catv']==1]

        return len(df_accidents_grenoble)
    

    st.metric(label="Nombre total d'\'accidents'", value=fct_accidents('BaseDeDonnées/Accidents_france/carcteristiques-2022.csv','BaseDeDonnées/Accidents_france/vehicules-2022.csv'), delta=120, delta_color="inverse")
# Afficher la carte dans Streamlit
#folium_static(map)