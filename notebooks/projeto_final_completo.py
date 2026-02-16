import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

df = pd.read_csv('dados/credito.csv')
print("📊 Coleta:", df.shape)

X = df[['idade','renda']].fillna(0)
scaler = StandardScaler()
kmeans = KMeans(3, random_state=42)
df['cluster'] = kmeans.fit_predict(scaler.fit_transform(X))

print(f"🎯 Avaliação Silhouette: {silhouette_score(scaler.fit_transform(X), df.cluster):.2f}")

plt.figure(figsize=(10,6))
sns.scatterplot(data=df, x='idade', y='renda', hue='cluster')
plt.title('Clusters Risco Crédito - K-Means')
plt.savefig('visualizacao.png')
plt.show()
