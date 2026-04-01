import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

# Compte des labels
sns.countplot(x="label", data=df)
plt.title("Distribution des labels")
plt.show()

# Heatmap corrélation
sns.heatmap(df.corr(), annot=True, fmt=".2f")
plt.title("Corrélation entre features")
plt.show()