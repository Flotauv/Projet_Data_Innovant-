
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
df_axes_routier = df_axes_routier.drop(columns=['Unnamed: 0'])
st.dataframe(df_axes_routier)

