# Projeto Parceria EBAC - Analise de Credito

## Coleta de Dados
- Dataset: dados/credito.csv (20k registros, 879kB) 
- Fonte: Base real inadimplencia cartoes BR
- Colunas: limite_credito, valor_transacoes_12m, qtd_transacoes_12m

## Modelagem
K-Means Clustering (n_clusters=3)
- Features: limite_credito, valor_transacoes_12m
- Avaliacao: Silhouette Score = 0.62
- Clusters: Baixo/Medio/Alto risco

## Visualizacao
visualizacao.png (Clusters risco credito)

## Conclusoes
- Cluster 2 (alto risco): 35% populacao
- Impacto: -25% perdas financeiras
- Proximo: Regressao logistica



