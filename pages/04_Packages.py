import os
import streamlit as st 

## Packages et version à mettre dans le fichier texte (à supprimer après)
result = os.popen('pip list').read()
st.code(result, language=None)
print(os.name)