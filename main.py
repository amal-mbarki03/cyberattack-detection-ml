import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Sample dataset
data = {
    'duration': [10, 20, 5, 30, 25],
    'packets': [100, 200, 50, 300, 250],
<<<<<<< HEAD
    'label': [0, 1, 0, 1, 1]
=======
    'attack': [0, 1, 0, 1, 1]
>>>>>>> 9e70d997db5b184eef168f3858319eeb4602f972
}

df = pd.DataFrame(data)

X = df[['duration', 'packets']]
<<<<<<< HEAD
y = df['label']
=======
y = df['attack']
>>>>>>> 9e70d997db5b184eef168f3858319eeb4602f972

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train, y_train)

print("Model trained successfully")
