import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('gasolina.csv')
df['data'] = pd.to_datetime(df['data'])
df['dia'] = df['data'].dt.day
plt.figure(figsize=(10,6))
sns.lineplot(data=df, x='dia', y='preco')
plt.title('Preço Gasolina SP')
plt.xlabel('Dia')
plt.ylabel('Preço R$')
plt.savefig('gasolina.png')
plt.show()
