import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score
from data_processing import load_data, clean_data, split_features_labels

# Charger et préparer les données
df = load_data("data.csv")
df = clean_data(df)
X, y = split_features_labels(df)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entraîner le modèle
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Évaluer
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("F1 Score:", f1_score(y_test, y_pred, average='weighted'))

# Sauvegarder le modèle
pickle.dump(model, open("model.pkl", "wb"))