import pandas as pd 
import streamlit as st 
import osmnx as ox 
import geopandas as gpd


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
col1,col2 = st.columns([3,1])


with col1:
    # Ajouter les boutons pour afficher/masquer les couches
    show_pistes = st.checkbox("Afficher les pistes cyclables", value=True)
    show_comptages = st.checkbox("Afficher les nombres de trajets moyen journalier en vélo", value=True)
    show_arceaux = st.checkbox("Afficher les arceaux pour vélo", value=True)
