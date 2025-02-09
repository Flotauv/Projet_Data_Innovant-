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


st.header("Quelles sont les modes de transport utilisés par les usagers de l'INP (étudiants et personnels) ?")
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel(file_path)

# Vérifier si les colonnes nécessaires existent
required_columns = [
    "Proportion Occurrences (%) 2020",
    "Proportion Occurrences (%) 2021",
    "Proportion Occurrences (%) 2023",
    "Proportion Occurrences (%) 2024"
]

if all(col in df.columns for col in required_columns):

    # Titre de l'application
    st.title("Histogramme des Modes de Transport (2020 - 2024)")

    # Définir les années et leurs couleurs associées
    years = ["2020", "2021", "2023", "2024"]
    colors = plt.cm.get_cmap("tab10", len(df))  # Utilisation d'une colormap pour assigner des couleurs uniques

    # Création du graphique
    fig, ax = plt.subplots(figsize=(10, 6))

    # Position des barres
    bar_width = 0.2
    x = np.arange(len(df))  # Indices des modes de transport

    # Boucle sur les années pour tracer les histogrammes avec des couleurs différentes
    for i, year in enumerate(years):
        ax.bar(
            x + i * bar_width,
            df[f"Proportion Occurrences (%) {year}"],
            width=bar_width,
            label=f"Année {year}",
            color=colors(i)  # Attribuer une couleur différente à chaque transport
        )

    # Labels et légendes
    ax.set_xticks(x + bar_width * (len(years) - 1) / 2)
    ax.set_xticklabels(df["Mode de Transport"], rotation=45, ha="right")
    ax.set_ylabel("Proportion (%)")
    ax.set_title("Proportion d'Occurrences par Mode de Transport (2020 - 2024)")
    ax.legend()

    # Afficher le graphique dans Streamlit
    st.pyplot(fig)

else:
    st.error("Les colonnes des proportions pour les années 2020, 2021, 2023 et 2024 sont introuvables dans le fichier.")

# Message de fin
st.write("📊 Données basées sur les années 2020, 2021, 2023 et 2024")


st.header("La distance parcourue influence-t-elle le choix du mode de transport ? Que représente chaque moyen de transport dans le kilométrage total ?")

st.write("Ajoutez ici une étude temporelle détaillée sur l'INP. Vous pouvez inclure des graphiques ou des analyses basées sur les données temporelles.")
