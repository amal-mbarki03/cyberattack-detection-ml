import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Sample dataset
data = {
    'duration': [10, 20, 5, 30, 25],
    'packets': [100, 200, 50, 300, 250],
    'label': [0, 1, 0, 1, 1]
}

df = pd.DataFrame(data)

X = df[['duration', 'packets']]
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train, y_train)

print("Model trained successfully")
