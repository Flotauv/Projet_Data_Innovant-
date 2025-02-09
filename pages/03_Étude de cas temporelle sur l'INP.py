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
st.markdown("**_Les visualisations utilisent les données du Challenge mobilité sur cinq années : 2020 (149 répondants), 2021 (735), 2022 (), 2023 (412), 2024 (424)_**")


st.header("Quelles sont les modes de transport utilisés par les usagers de l'INP (étudiants et personnels) ?")
st.header("La distance parcourue influence-t-elle le choix du mode de transport ? Que représente chaque moyen de transport dans le kilométrage total ?")

st.write("Ajoutez ici une étude temporelle détaillée sur l'INP. Vous pouvez inclure des graphiques ou des analyses basées sur les données temporelles.")
