import streamlit as st 


### Configuration de la page 
st.set_page_config(page_title = "Étude de cas temporelle sur l'INP",layout="wide")
# Titres 
st.title("Etude de cas temporelle sur l'INP")
st.write("Cette page présente une analyse des données de l'INP, groupe d'écoles de l'Université Grenoble Alpes.")
    
st.write("Les visualisations s'appuient sur une enquête intitulée 'Challenge mobilité' ")
st.write("Cette enquête compare les trajets de personnes faisant partie de  l'INP se rendant sur leur lieu de travail/étude via différents modes de transport")

st.markdown("**_Les visualisations utilisent les données du Challenge mobilité sur cinq années : 2020 (149 répondants), 2021 (735), 2022 (247), 2023 (412), 2024 (424)_**")


st.header("Quelles sont les modes de transport utilisés par les usagers de l'INP (étudiants et personnels) ? (en finition)")
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Charger les données
df_merged = pd.read_excel("BaseDeDonnées/df_merged.xlsx")
#df_occurence = pd.DataFrame()
colonnes_occ = df_merged.columns[df_merged.columns.str.startswith('Proportion Occurrences')]
colonnes_occ = colonnes_occ.to_list()
colonnes_occ.append('Mode de Transport')
df_occurence = df_merged[colonnes_occ]
df_occurence = df_occurence.melt(id_vars='Mode de Transport',value_name='Occurrence (%)',var_name='Annee')

df_occurence['Mode de Transport'] = df_occurence['Mode de Transport'].replace('Trotinette ou vélo électrique','Trotinette ou vélo')

df_occurence['Mode de Transport'] = df_occurence['Mode de Transport'].replace('Autre',np.nan)
df_occurence['Mode de Transport'] = df_occurence['Mode de Transport'].replace('Moto / Scooter',np.nan)
df_occurence['Mode de Transport'] = df_occurence['Mode de Transport'].replace('Voiture électrique',np.nan)
df_occurence['Mode de Transport'] = df_occurence['Mode de Transport'].replace('Voiture hybride rechargeable',np.nan)



df_occurence = df_occurence.dropna()
df_occurence = df_occurence.groupby(['Mode de Transport','Annee'])['Occurrence (%)'].sum().reset_index()

df_occurence['Annee'] = df_occurence['Annee'].str.replace('Proportion Occurrences (%)','')
#st.dataframe(df_occurence)
st.dataframe(df_occurence)

st.line_chart(data=df_occurence,x='Annee',y='Occurrence (%)',color='Mode de Transport',width=900,height=500)

## Affichage distances parcourues 
colonnes_dist = df_merged.columns[df_merged.columns.str.startswith('Proportion Distance')]
colonnes_dist = colonnes_dist.to_list()
colonnes_dist.append('Mode de Transport')
df_dist = df_merged[colonnes_dist]
df_dist = df_dist.melt(id_vars='Mode de Transport',value_name='Proportion Distance (%)',var_name='Annee')
df_dist['Mode de Transport'] = df_dist['Mode de Transport'].replace('Trotinette ou vélo électrique','Trotinette ou vélo')
df_dist['Mode de Transport'] = df_dist['Mode de Transport'].replace('Autre',np.nan)
df_dist['Mode de Transport'] = df_dist['Mode de Transport'].replace('Moto / Scooter',np.nan)
df_dist['Mode de Transport'] = df_dist['Mode de Transport'].replace('Voiture électrique',np.nan)
df_dist['Mode de Transport'] = df_dist['Mode de Transport'].replace('Voiture hybride rechargeable',np.nan)
df_dist = df_dist.dropna()
df_dist = df_dist.groupby(['Mode de Transport','Annee'])['Proportion Distance (%)'].sum().reset_index()
df_dist['Annee'] = df_dist['Annee'].str.replace('Proportion Distance Totale (%)','')
st.dataframe(df_dist)
st.line_chart(data=df_dist,x='Annee',y='Proportion Distance (%)',color='Mode de Transport',width=900,height=500)







# Définition des années et des colonnes concernées
years = ["2020", "2021", "2023", "2024"]
year_columns = [f"Proportion Occurrences (%) {year}" for year in years]

# Définir des couleurs bien distinctes pour chaque année
year_colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"]  # Bleu, Orange, Vert, Rouge

# Interface utilisateur Streamlit
st.subheader("📊 Histogramme des Modes de Transport (2020 - 2024)",divider=True)
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


st.header("Les raisons qui poussent aux choix des transports utilisés (en cours)")
df_choix = pd.read_excel("BaseDeDonnées/choix.xlsx")
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter

# Renommage de la colonne contenant les réponses
col_name = "33. Pourquoi avez-vous choisi ce mode de transport pour vous rendre sur votre lieu de travail ?_(3 réponses maximum)"
df_choix = df_choix.rename(columns={col_name: "Reasons"})

# Extraction et comptage des raisons
reasons_series = df_choix["Reasons"].dropna().str.split(';').explode()
reasons_counts = Counter(reasons_series)

# Conversion en DataFrame et triage par fréquence
df_choix = pd.DataFrame(reasons_counts.items(), columns=['Reason', 'Count']).sort_values(by='Count', ascending=False)

# Création de la figure
fig, ax = plt.subplots(figsize=(10, 6))

# Génération des couleurs et des hauteurs des barres
colors = plt.cm.Paired(np.linspace(0, 1, len(df_choix)))
bars = ax.barh(df_choix['Reason'], df_choix['Count'], color=colors)
# Ajout des labels et du titre 
ax.set_xlabel("Nombre de mentions")
ax.set_ylabel("Raisons du choix du mode de transport")
ax.set_title("Principales raisons du choix d'un mode de transport")

# Ajout des valeurs sur les barres
for bar in bars:
    ax.text(bar.get_width() + 5, bar.get_y() + bar.get_height()/2, 
            str(int(bar.get_width())), va='center')

# Inversion de l'axe Y pour afficher la raison la plus populaire en haut
plt.gca().invert_yaxis()

# Affichage de la visualisation
st.pyplot(fig)

