import streamlit as st 


st.title("Visualisation d'infrastructures cyclistes sur le territoire Grenoblois")


col1,col2 = st.columns([3,1])


with col1:
    # Ajouter les boutons pour afficher/masquer les couches
    show_pistes = st.checkbox("Afficher les pistes cyclables", value=True)
    show_comptages = st.checkbox("Afficher les nombres de trajets moyen journalier en vélo", value=True)
    show_arceaux = st.checkbox("Afficher les arceaux pour vélo", value=True)
