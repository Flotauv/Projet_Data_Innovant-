import streamlit as st
import pandas as pd
import plotly.express as plx
import folium
import datetime

from streamlit_folium import st_folium
from geopy.distance import geodesic
from shapely.geometry import shape
from shapely.geometry import LineString
import json

st.set_page_config(layout="wide")




## Les autres packages dont on va avoir besoin mais qui posent problème

#json
#folium
#streamlit_folium
#geopy
#shapely


#st.title("Dashboard récapitulatif environnement vélo Grenoble")
#st.write("La première version de notre dashboard avec les tenants et les aboutissants de \
         #ce que nous voulons montrer")


# Création des colonnes pour pouvoir mettre les graphiques
col1, col2 = st.columns(2)



with col1:

    def fct_transform_tmja_to_axes_routier(file):
        df_tmja = pd.read_csv(file, sep=';')
        df_tmja['dateReferentiel'] = pd.to_datetime(df_tmja['dateReferentiel'])
        df_tmja['Annee'] = df_tmja['dateReferentiel'].dt.year
        df_tmja = df_tmja[df_tmja['depPrD'] == 38]
        df_tmja = df_tmja.dropna()  # Il y en a très peu

        df_tmja['longueur'] = df_tmja['longueur'].str.replace(',', '.')
        df_tmja['ratio_PL'] = df_tmja['ratio_PL'].str.replace(',', '.')
        df_tmja['ratio_PL'] = df_tmja['ratio_PL'].astype(float)
        df_tmja['ratio_PL'] = df_tmja['ratio_PL']/100
        df_tmja['Nb_poids_lourds'] = round(
            df_tmja['TMJA'] * df_tmja['ratio_PL'])
        df_axes_routier = df_tmja.groupby(['route', 'Annee'])[['longueur', 'TMJA', 'Nb_poids_lourds']].sum(
        ).reset_index().sort_values(by='TMJA', ascending=False)

        df_axes_routier['ratio_PL'] = round(
            (df_axes_routier['Nb_poids_lourds']/df_axes_routier['TMJA'])*100)
        # df_axes_routier = df_axes_routier.drop(columns=['Unnamed: 0'])
        df_axes_routier = df_axes_routier[(df_axes_routier['route'] != 'N0007') & (
            df_axes_routier['route'] != 'A0007N')]
        df_axes_routier = df_axes_routier.rename(
            columns={'TMJA': 'Taux Moyen Journalier Annualisé (en Millions)'})
        df_axes_routier = df_axes_routier.rename(
            columns={'route': 'Axe routier'})

        df_axes_routier['Axe routier'] = df_axes_routier['Axe routier'].replace(
            'A0041', 'A41')
        df_axes_routier['Axe routier'] = df_axes_routier['Axe routier'].replace(
            'A0043', 'A43')
        df_axes_routier['Axe routier'] = df_axes_routier['Axe routier'].replace(
            'A0007', 'A7')
        df_axes_routier['Axe routier'] = df_axes_routier['Axe routier'].replace(
            'A0048', 'A48')
        df_axes_routier['Axe routier'] = df_axes_routier['Axe routier'].replace(
            'A0049', 'A49')
        df_axes_routier['Axe routier'] = df_axes_routier['Axe routier'].replace(
            'N0085', 'Nationale 85')
        df_axes_routier['Axe routier'] = df_axes_routier['Axe routier'].replace(
            'N0087', 'Nationale 87')
        df_axes_routier['Axe routier'] = df_axes_routier['Axe routier'].replace(
            'A0051N', 'A51')

        return df_axes_routier

    fig = plx.bar(fct_transform_tmja_to_axes_routier('BaseDeDonnées/Grenoble/tmj_axes_routier.csv'),

                  x='Axe routier',
                  y='Taux Moyen Journalier Annualisé (en Millions)',
                  text='Taux Moyen Journalier Annualisé (en Millions)', )

    st.header(
        'Indicateur 1 : Traffic routier de l\'agglomération Grenobloise', divider='gray')
    fig.update_traces(textposition="outside")
    st.write('Traffic routier lié à l\'année  {}'.format(fct_transform_tmja_to_axes_routier(
        'BaseDeDonnées/Grenoble/tmj_axes_routier.csv')['Annee'][0]))
    st.plotly_chart(fig, use_container_width=True)



with col1: 
    st.header('Nombre de parkings à vélo dans l\'agglomération Grenobloise')


    def fct_comptage_park_velo(file):
        df_sta = pd.read_csv(file)
        df_sta = df_sta[df_sta['commune_local']=='Grenoble']
        df_sta= df_sta.drop(columns=['id_osm','gratuit','type_accroche'])
        df_sta = df_sta.dropna()
        df_sta['date_maj'] = pd.to_datetime(df_sta['date_maj'])
        df_sta['annee'] = df_sta['date_maj'].dt.year

        return (len(df_sta),df_sta['annee'][0])

    st.metric(label = 'Nombre de parkings à vélo dans l\'agglomération Grenobloise',
     value = fct_comptage_park_velo('BaseDeDonnées/Grenoble/stationnement_velo.csv')[0],
     border=True)

#col3, col4 = st.columns([1, 1])
with col2:
    st.header('Cartographie du réseau cyclable et des parkings à vélo',divider='gray')
    def reverse_coordonnees(liste):
        return [(coordonnees[1],coordonnees[0]) for coordonnees in liste ]
    def fct_map_reseau_cyclable(file):


        df_piste = pd.read_csv(file)
        # Création des colonnes 'latitude' et 'longitude'
        df_piste['lat'] = [element[1] for element in df_piste['geo_point_2d'].str.split(',')]
        df_piste['long'] = [element[0] for element in df_piste['geo_point_2d'].str.split(',')]
        df_piste['lat'] = df_piste['lat'].astype(object)
        df_piste['long'] = df_piste['long'].astype(object)
        df_piste['geo_shape'] = df_piste['geo_shape'].apply(lambda x: LineString(eval(x)['coordinates']))
        df_piste['coordonnees'] = df_piste['geo_shape'].apply(lambda x: list(x.coords)).to_list()

        df_piste['coordonnees'] = df_piste['coordonnees'].apply(lambda x: reverse_coordonnees(x))

        # Création de la map
        map_piste_cyclable = folium.Map(location=[45.188529, 5.724524],zoom_start=14,titles='Map Piste Cyclable')
        for cords in df_piste['coordonnees']:
            folium.PolyLine(cords, color='blue').add_to(map_piste_cyclable)

        return map_piste_cyclable


    def fct_arceaux_velo(file):
        df_sta = pd.read_csv(file)
        df_sta = df_sta[df_sta['commune_local']=='Grenoble']
        df_sta= df_sta.drop(columns=['id_osm','gratuit','type_accroche'])
        df_sta = df_sta.dropna()
        df_sta['date_maj'] = pd.to_datetime(df_sta['date_maj'])
        df_sta['annee'] = df_sta['date_maj'].dt.year
        carte = fct_map_reseau_cyclable('BaseDeDonnées/Grenoble/pistes_cyclables.xls')
        df_sta['ratio_color'] =df_sta['capacite']/df_sta['capacite'].max()

        for index, row in df_sta.iterrows():
            folium.CircleMarker([row['lat'],row['lon']],
            radius=5,popup=f"capacité :{row['capacite']}",
            color='red',
            fill=True).add_to(carte)
        return carte
    #with st.expander('Cartographie du réseau cyclable avec parkings '):
    st_folium(fct_arceaux_velo('BaseDeDonnées/Grenoble/stationnement_velo.csv'))