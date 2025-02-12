import streamlit as st 
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from collections import Counter
### Configuration de la page 
st.set_page_config(page_title = "Étude de cas temporelle sur l'INP",layout="wide")
# Titres 
st.title("Étude de cas temporelle sur l'INP")
st.write("Cette page présente une analyse des données de l'INP, groupe d'écoles de l'Université Grenoble Alpes.")
    
st.write("Les visualisations s'appuient sur une enquête intitulée **_'Challenge mobilité'_**  sur cinq années 2020 (149 répondants), 2021 (735), 2022 (247), 2023 (412), 2024 (424)")
st.write("Cette enquête compare les trajets de personnes faisant partie de  l'INP se rendant sur leur lieu de travail/étude via différents modes de transport")





st.header("Comment les modes de transport sont utilisés ?")





df_merged = pd.read_excel("BaseDeDonnées/df_merged.xlsx")


st.subheader("Quels sont les modes de transport favoris ? ",divider=True)

###Quelles sont les modes de transport les plus utilisés

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Définition des années et des colonnes concernées
years = ["2020", "2021", "2022", "2023", "2024"]
year_columns = [f"Proportion Occurrences (%) {year}" for year in years]

# Génération d'une palette de bleu dégradé
cmap = cm.Blues  # Colormap bleu
year_colors = [cmap(0.2 + i * 0.15) for i in range(len(years))]  # Nuances progressives

# Création du graphique avec nuances de bleu
fig, ax = plt.subplots(figsize=(14, 7))

# Position des barres avec espacement plus large entre les groupes
bar_width = 0.15
spacing = 0.3  # Espace entre les groupes de barres
x = np.arange(len(df_merged)) * (bar_width * len(years) + spacing)  # Ajustement des positions

# Boucle sur les années pour tracer les histogrammes avec nuances de bleu
for i, (year, color) in enumerate(zip(years, year_colors)):
    ax.bar(
        x + i * bar_width,
        df_merged[year_columns[i]],
        width=bar_width,
        label=f"Année {year}",
        color=color  # Utilisation des nuances de bleu
    )

# Configuration des axes et légendes
ax.set_xticks(x + bar_width * (len(years) - 1) / 2)
ax.set_xticklabels(df_merged["Mode de Transport"], rotation=45, ha="right")
ax.set_ylabel("Proportion d'utilisation %")
ax.set_title("Proportion d'utilisation par Mode de Transport (2020 - 2024)")
ax.legend()

# Affichage de la visualisation
st.pyplot(fig)




st.subheader("Les trajets sont-ils décarbonés ? ",divider=True)



###Part de chaque mode de transport sur les trajets de la ville

# Définition des années et des colonnes concernées
years = ["2020", "2021", "2022", "2023", "2024"]
year_columns = [f"Proportion Distance Totale (%) {year}" for year in years]

# Génération d'une palette de rouge dégradé
cmap = cm.Reds  # Colormap rouge
year_colors = [cmap(0.2 + i * 0.15) for i in range(len(years))]  # Nuances progressives

# Création du graphique avec nuances de rouge
fig, ax = plt.subplots(figsize=(14, 7))

# Position des barres avec espacement plus large entre les groupes
bar_width = 0.15
spacing = 0.3  # Espace entre les groupes de barres
x = np.arange(len(df_merged)) * (bar_width * len(years) + spacing)  # Ajustement des positions

# Boucle sur les années pour tracer les histogrammes avec nuances de rouge
for i, (year, color) in enumerate(zip(years, year_colors)):
    ax.bar(
        x + i * bar_width,
        df_merged[year_columns[i]],
        width=bar_width,
        label=f"Année {year}",
        color=color  # Utilisation des nuances de rouge
    )
# Configuration des axes et légendes
ax.set_xticks(x + bar_width * (len(years) - 1) / 2)
ax.set_xticklabels(df_merged["Mode de Transport"], rotation=45, ha="right")
ax.set_ylabel("Part des modes de transport dans les distances cumulées")
ax.set_title("Importance de chaque mode de transport dans les distances réalisées (2020 - 2024)")
ax.legend()

# Affichage de la visualisation
st.pyplot(fig)




st.subheader("Part représentative des modes de déplacement par années ",divider=True)

###Distance moyenne parcourue sur chaque mode de transport

# Définition des années et des colonnes concernées
years = ["2020", "2021", "2022", "2023", "2024"]
year_columns = [f"Distance Moyenne (km) {year}" for year in years]

# Génération d'une palette de vert dégradé
cmap = cm.Greens  # Colormap vert
year_colors = [cmap(0.2 + i * 0.15) for i in range(len(years))]  # Nuances progressives

# Création du graphique avec nuances de vert
fig, ax = plt.subplots(figsize=(14, 7))

# Position des barres avec espacement plus large entre les groupes
bar_width = 0.15
spacing = 0.3  # Espace entre les groupes de barres
x = np.arange(len(df_merged)) * (bar_width * len(years) + spacing)  # Ajustement des positions

# Boucle sur les années pour tracer les histogrammes avec nuances de vert
for i, (year, color) in enumerate(zip(years, year_colors)):
    ax.bar(
        x + i * bar_width,
        df_merged[year_columns[i]],
        width=bar_width,
        label=f"Année {year}",
        color=color  # Utilisation des nuances de vert
    )
# Configuration des axes et légendes
ax.set_xticks(x + bar_width * (len(years) - 1) / 2)
ax.set_xticklabels(df_merged["Mode de Transport"], rotation=45, ha="right")
ax.set_ylabel("Distance Moyenne (km)")
ax.set_title("Distance Moyenne par Mode de Transport (2020 - 2024)")
ax.legend()




# Affichage de la visualisation
st.pyplot(fig)








st.header("Quel impact a le challenge mobilité sur les déplacements ?")





# Chargement des données
df_impact_challenge = pd.read_excel('BaseDeDonnées/ImpactChallenge.xlsx')

# Création de deux colonnes
col1, col2 = st.columns([1, 1])  # 1/3 pour le texte, 2/3 pour le graphique




# Partie droite : affichage du graphique
with col1:
    # Création du graphique avec Matplotlib
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(df_impact_challenge.columns, df_impact_challenge.iloc[0], marker='o', linestyle='-', color='b')

    # Ajout des labels et du titre
    ax.set_xlabel("Année")
    ax.set_ylabel("Évolution en %")
    ax.set_title("Impact du Challenge Mobilité sur les choix de modes de transport verts")

    # Affichage de la grille
    ax.grid(True)

    # Affichage du graphique dans Streamlit
    st.pyplot(fig)

# Partie gauche : texte explicatif
with col2:
    st.write("             ")
    st.write("Ce graphique illustre l'évolution des choix de modes de transport verts dans le cadre du Challenge Mobilité")
    st.write("L'objectif est de mesurer l'impact de cette initiative sur les comportements de déplacement au fil des années.")
    st.write("L'impact du Challenge Mobilité semble être mitigé. On n'observe pas d'adoption massive des transports verts durant le challenge.")
    st.markdown("**Cela indique sûrement que les campagnes de sensibilisation s'adressent souvent à un public déjà conquis.**")








st.header("Les matrices des choix de transport en fonction du type de distance")


df_2020 = pd.read_excel('BaseDeDonnées/INP2020Matrice.xlsx')
df_2021 = pd.read_excel('BaseDeDonnées/INP2021Matrice.xlsx')
df_2022 = pd.read_excel('BaseDeDonnées/INP2022Matrice.xlsx')
df_2023 = pd.read_excel('BaseDeDonnées/INP2023Matrice.xlsx')
df_2024 = pd.read_excel('BaseDeDonnées/INP2024Matrice.xlsx')



# Dictionnaire des DataFrames par année
data = {
    '2020': df_2020,
    '2021': df_2021,
    '2022': df_2022,
    '2023': df_2023,
    '2024': df_2024
}

# Titre de l'application
st.title("Visualisation des occurrences des modes de transport par type de trajet")

# Sélecteur d'année
selected_year = st.selectbox("Sélectionnez une année", list(data.keys()))

# Récupérer le DataFrame correspondant à l'année sélectionnée
dfanalyse = data[selected_year]

# Traitement des données
colonnes_gardees = dfanalyse.drop(columns=['Distance totale du trajet', 'Type de trajet'])
occurrences_transport = dfanalyse.groupby('Type de trajet').apply(lambda group: (group[colonnes_gardees.columns] > 0).sum())

# Création de la heatmap
fig, ax = plt.subplots(figsize=(12, 8))
sns.heatmap(occurrences_transport, annot=True, fmt="d", cmap="YlGnBu", cbar=True, ax=ax)
ax.set_title(f"Occurrences des modes de transport par type de trajet en {selected_year}", fontsize=16)
ax.set_ylabel("Type de trajet", fontsize=12)
ax.set_xlabel("Modes de transport", fontsize=12)
plt.xticks(rotation=45, ha="right")
plt.tight_layout()


# Affichage de la heatmap dans Streamlit
st.pyplot(fig)









st.header("Les raisons qui poussent aux choix des transports utilisés")




df_choix = pd.read_excel("BaseDeDonnées/choix.xlsx")



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

