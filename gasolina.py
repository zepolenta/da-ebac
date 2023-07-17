import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados do arquivo CSV
df = pd.read_csv('gasolina.csv')

# Criar o gráfico de linha
plt.plot(df['dia'], df['venda'])
plt.xlabel('Dia')
plt.ylabel('Preço de Venda')
plt.title('Preço Médio de Venda da Gasolina em São Paulo (Julho 2021)')
plt.grid(True)

# Salvar o gráfico como imagem
plt.savefig('gasolina.png')
