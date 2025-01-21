
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


#upload_file = st.file_uploader("Choose a file")
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
    #df_axes_routier = pd.read_csv('Axes_routiers.csv') 
    df_axes_routier = df_axes_routier.drop(columns=['Unnamed: 0'])
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





#df_axes_routier = df_axes_routier.rename(columns={'route':'Route'})
#st.subheader('Dataframes')
#with st.expander('Preview'):
    #st.dataframe(fct_transform_tmja_to_axes_routier())


## Figure 

st.columns(4) # Création des colonnes pour pouvoir mettre les graphiques 
fig = plx.bar(fct_transform_tmja_to_axes_routier('Axes_routier.csv'),
              x='Axe routier',
              y='Taux Moyen Journalier Annualisé (en Millions)',
              text='Taux Moyen Journalier Annualisé (en Millions)', )


st.header('Indicateur 1 : Traffic routier de l\'agglomération Grenobloise',divider='gray')

st.write('Traffic routier lié à l\'année 2019')
st.plotly_chart(fig,use_container_width=True)

