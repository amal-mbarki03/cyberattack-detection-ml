import streamlit as st
import pandas as pd
import pickle

st.title("Cyberattack Detection ML")

uploaded_file = st.file_uploader("Choisir un fichier CSV")
if uploaded_file:
    data = pd.read_csv(uploaded_file)
    model = pickle.load(open("model.pkl", "rb"))
    predictions = model.predict(data)
    st.write("Prédictions :")
    st.write(predictions)