import pandas as pd
import matplotlib.pyplot as plt

# Carregando os dados do arquivo CSV
df = pd.read_csv("dados_pesquisa.csv")

# Criar uma figura e subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Gráfico de barras para contar o número de entrevistados em cada cidade
cidade_counts = df['Cidade'].value_counts()
axs[0, 0].bar(cidade_counts.index, cidade_counts.values, color='skyblue')
axs[0, 0].set_xlabel('Cidade')
axs[0, 0].set_ylabel('Número de Entrevistados')
axs[0, 0].set_title('Número de Entrevistados por Cidade')
axs[0, 0].tick_params(axis='x', rotation=45)

# Gráfico de histograma para visualizar a distribuição das idades
axs[0, 1].hist(df['Idade'], bins=10, edgecolor='k', color='salmon')
axs[0, 1].set_xlabel('Idade')
axs[0, 1].set_ylabel('Frequência')
axs[0, 1].set_title('Distribuição de Idades dos Entrevistados')

# Gráfico de pizza para mostrar a distribuição das respostas
colors = ['#87CEEB', '#FFA07A', '#87CEEB']  # Cores personalizadas usando códigos RGB
resposta_counts = df['Resposta'].value_counts()
axs[1, 0].pie(resposta_counts.values, labels=resposta_counts.index, autopct='%1.1f%%', startangle=140, colors=colors)
axs[1, 0].axis('equal')
axs[1, 0].set_title('Distribuição das Respostas')

# Remover o subplot vazio
fig.delaxes(axs[1, 1])

# Ajustar a disposição dos subplots
plt.tight_layout()

# Exibir todos os gráficos juntos
plt.show()