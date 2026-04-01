import pickle
import pandas as pd

# Charger les données
df_new = pd.read_csv("data.csv")

# ❗ supprimer la colonne label si elle existe
if "label" in df_new.columns:
    df_new = df_new.drop("label", axis=1)

# Charger le modèle
model = pickle.load(open("model.pkl", "rb"))

# Prédire
predictions = model.predict(df_new)

print("Prédictions :", predictions)