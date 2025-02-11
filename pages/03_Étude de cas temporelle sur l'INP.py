import streamlit as st 

# Titres 
st.title("Etude de cas temporelle sur l'INP et l'UGA")
st.write(
    """
Cette page présente une analyse des données de l'INP, groupe d'écoles de l'Université Grenoble Alpes. Les visualisations s'appuient sur une enquête intitulée "Challenge mobilité".
Cette enquête compare le trajet quotidien d'un usager de l'INP, réalisé tout au long de l'année, en termes de modes de transport utilisés et de kilomètres parcourus sur chaque mode,
avec le trajet effectué lors d'une journée dédiée au challenge, où l'usager doit tenter d'utiliser des modes de transport écologiques.
    """
)
st.write("""Nous compléterons nos visualisations avec celles issues de l'ensemble de l'Université Grenoble Alpes (plus de 57 000 étudiants),
ainsi que celles provenant de Copenhague, cette dernière étant considérée comme un modèle en matière de mobilité durable.""")

st.markdown("**_Les visualisations utilisent les données du Challenge mobilité sur cinq années : 2020 (149 répondants), 2021 (735), 2022 (), 2023 (412), 2024 (424)_**")


st.header("Quelles sont les modes de transport utilisés par les usagers de l'INP (étudiants et personnels) ? (en finition)")
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Charger les données
df_merged = pd.read_excel("BaseDeDonnées/df_merged.xlsx")

# Définition des années et des colonnes concernées
years = ["2020", "2021", "2023", "2024"]
year_columns = [f"Proportion Occurrences (%) {year}" for year in years]

# Définir des couleurs bien distinctes pour chaque année
year_colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"]  # Bleu, Orange, Vert, Rouge

# Interface utilisateur Streamlit
st.title("📊 Histogramme des Modes de Transport (2020 - 2024)")
st.write("Affichage des proportions d'occurrences (%) des modes de transport sur 4 années.")

# Création du graphique avec de nouvelles couleurs
fig, ax = plt.subplots(figsize=(14, 7))

# Position des barres
bar_width = 0.2
x = np.arange(len(df_merged))  # Indices des modes de transport

# Boucle sur les années pour tracer les histogrammes avec des couleurs bien distinctes
for i, (year, color) in enumerate(zip(years, year_colors)):
    ax.bar(
        x + i * bar_width,
        df_merged[year_columns[i]],
        width=bar_width,
        label=f"Année {year}",
        color=color  # Utilisation des nouvelles couleurs distinctes
    )

# Configuration des axes et légendes
ax.set_xticks(x + bar_width * (len(years) - 1) / 2)
ax.set_xticklabels(df_merged["Mode de Transport"], rotation=45, ha="right")
ax.set_ylabel("Proportion Occurrences (%)")
ax.set_title("Proportion d'Occurrences par Mode de Transport (2020 - 2024)")
ax.legend()

# Afficher le graphique dans Streamlit
st.pyplot(fig)

st.header("Quel impact a le challenge mobilité sur les déplacements ? (en cours)")



st.header("La distance parcourue influence-t-elle le choix du mode de transport ? Que représente chaque moyen de transport dans le kilométrage total ? (en finition)")


# Définition des années et des colonnes concernées pour la Distance Totale
years = ["2020", "2021", "2023", "2024"]
distance_columns = [f"Proportion Distance Totale (%) {year}" for year in years]

# Définir des couleurs bien distinctes pour chaque année
year_colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"]  # Bleu, Orange, Vert, Rouge

# Interface utilisateur Streamlit
st.title("📊 Histogramme des Distances Totales par Mode de Transport (2020 - 2024)")
st.write("Affichage des proportions de distance totale (%) parcourues par mode de transport sur 4 années.")

# Création du graphique avec de nouvelles couleurs
fig, ax = plt.subplots(figsize=(14, 7))

# Position des barres
bar_width = 0.2
x = np.arange(len(df_merged))  # Indices des modes de transport

# Boucle sur les années pour tracer les histogrammes avec des couleurs bien distinctes
for i, (year, color) in enumerate(zip(years, year_colors)):
    ax.bar(
        x + i * bar_width,
        df_merged[distance_columns[i]],
        width=bar_width,
        label=f"Année {year}",
        color=color  # Utilisation des nouvelles couleurs distinctes
    )

# Configuration des axes et légendes
ax.set_xticks(x + bar_width * (len(years) - 1) / 2)
ax.set_xticklabels(df_merged["Mode de Transport"], rotation=45, ha="right")
ax.set_ylabel("Proportion Distance Totale (%)")
ax.set_title("Proportion de la Distance Totale par Mode de Transport (2020 - 2024)")
ax.legend()

# Afficher le graphique dans Streamlit
st.pyplot(fig)

st.header("Les matrices des choix de transport en fonction du type de distance (en cours)")

st.header("Que nous révèles les données de l'UGA ? (en cours)")

st.header("Comparaison avec Copenhague (en cours, dépend du temps restant)")



st.header("Les raisons qui poussent aux choix des transports utilisés (en cours)")


st.write("Ajoutez ici une étude temporelle détaillée sur l'INP. Vous pouvez inclure des graphiques ou des analyses basées sur les données temporelles.")
