import pandas as pd 
import streamlit as st 
import osmnx as ox 
import geopandas as gpd
from shapely.wkt import loads
from shapely.geometry import Point
import folium

# Configurer la page Streamlit
st.set_page_config(
    page_title="Visualisation d'infrastructures cyclistes sur le territoire Grenoblois",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon=":shark:",
    menu_items={
        'About' : 'https://www.presse-citron.net/crypto/comparatif/binance-vs-coinbase/'
    }
)
st.title("Visualisation d'infrastructures cyclistes sur le territoire Grenoblois")

## Définition des fonctions utiles à la page : 

# Fonction pour charger les contours des communes
@st.cache_data
def load_communes():
    communes_cibles = [
        "Grenoble",
        "Saint-Martin-le-Vinoux",
        "Fontaine",
        "Echirolles",
        "Saint-Martin-d’Hères",
        "Le Pont-de-Claix",
        "Eybens",
        "Poisat",
        "Seyssinet-Pariset",
        "Meylan",
        "La Tronche",
        "Saint-Egrève"
    ]
    communes_selectionnees = gpd.GeoDataFrame()
    for commune in communes_cibles:
        try:
            commune_gdf = ox.geocode_to_gdf(commune + ", France")
            commune_gdf = commune_gdf.to_crs(epsg=4326)  # CRS compatible avec Folium
            communes_selectionnees = pd.concat([communes_selectionnees, commune_gdf], ignore_index=True)
        except Exception as e:
            st.error(f"Erreur lors du traitement de {commune}: {e}")
    return gpd.GeoDataFrame(communes_selectionnees, crs="EPSG:4326")

# Fonction pour charger les comptages vélo
@st.cache_data
def load_comptages():
    df = pd.read_csv("comptages.csv")  # Remplacez par le chemin correct
    # Calculer les rayons des cercles proportionnels
    facteur_echelle = 0.002
    df['rayon'] = facteur_echelle * df['tmj_2022'] ** 0.5
    df['geometry'] = df['geo_point_2d'].apply(
        lambda x: Point(map(float, x.split(',')[::-1]))  # Inverser les coordonnées
    )
    gdf = gpd.GeoDataFrame(df, geometry='geometry', crs="EPSG:4326")
    return gdf

# Fonction pour charger les pistes cyclables
@st.cache_data
def load_pistes():
    df = pd.read_csv("Pistes.csv")  # Remplacez par le chemin correct
    df['geometry'] = df['geometry'].apply(loads)  # Convertir WKT en géométries Shapely
    gdf = gpd.GeoDataFrame(df, geometry='geometry', crs="EPSG:3857")  # Définir le CRS actuel
    gdf = gdf.to_crs(epsg=4326)  # Reprojeter en latitude/longitude
    return gdf



## Création des colonnes pour afficher nos graphiques
col1,col2 = st.columns([3,1])


with col1:
    # Ajouter les boutons pour afficher/masquer les couches
    show_pistes = st.checkbox("Afficher les pistes cyclables", value=True)
    show_comptages = st.checkbox("Afficher les nombres de trajets moyen journalier en vélo", value=True)
    show_arceaux = st.checkbox("Afficher les arceaux pour vélo", value=True)
