import streamlit as st
import pandas as pd

st.title("📊 Application RAMA")

data = pd.DataFrame({
    "Tâche": ["Surveiller", "Installer", "Planifier"],
    "Statut": ["En cours", "À faire", "Terminé"]
})

st.dataframe(data)
