
import streamlit as st 
import pandas as pd 
import plotly.express as plx


st.title("Dashboard récapitulatif environnement vélo Grenoble")
st.write("La première version de notre dashboard avec les tenants et les aboutissants de \
         ce que nous voulons montrer")

@st.cache_data
def read_csv_file(path):
    df=pd.read_csv(path,sep=';')
    return df


#upload_file = st.file_uploader("Choose a file")

df_axes_routier = pd.read_csv('Axes_routiers.csv')
'On arrange un peu le dataframes' 
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





#df_axes_routier = df_axes_routier.rename(columns={'route':'Route'})
st.dataframe(df_axes_routier)


## Figure 

st.columns(4) # Création des colonnes pour pouvoir mettre les graphiques 
fig = plx.bar(df_axes_routier,
              x='Axe routier',
              y='Taux Moyen Journalier Annualisé (en Millions)',
              text='Taux Moyen Journalier Annualisé (en Millions)', )


st.header('Traffic routier de l\'agglomération Grenobloise',divider='gray')
st.write('Traffic routier lié à l\'année 2019')
st.plotly_chart(fig,use_container_width=True)

