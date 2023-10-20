import pandas as pd
import matplotlib.pyplot as plt

# Carregando os dados do arquivo CSV
df = pd.read_csv("dados_pesquisa.csv")

# Gráfico de barras para contar o número de entrevistados em cada cidade
cidade_counts = df['Cidade'].value_counts()
plt.figure(figsize=(10, 6))
plt.bar(cidade_counts.index, cidade_counts.values)
plt.xlabel('Cidade')
plt.ylabel('Número de Entrevistados')
plt.title('Número de Entrevistados por Cidade')
plt.xticks(rotation=45)
plt.show()

# Gráfico de histograma para visualizar a distribuição das idades
plt.figure(figsize=(8, 6))
plt.hist(df['Idade'], bins=10, edgecolor='k')
plt.xlabel('Idade')
plt.ylabel('Frequência')
plt.title('Distribuição de Idades dos Entrevistados')
plt.show()

# Gráfico de pizza para mostrar a distribuição das respostas
resposta_counts = df['Resposta'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(resposta_counts.values, labels=resposta_counts.index, autopct='%1.1f%%', startangle=140)
plt.axis('equal')
plt.title('Distribuição das Respostas')
plt.show()