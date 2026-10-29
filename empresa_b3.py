import pandas as pd

df = pd.read_excel ("ABEV3_evolucao.xlsx")
print(df)
df['valor'].max()
df['valor'].min()
df['valor'].mean()
df['valor'].std()

#selecionar linhas e colunas 
df[0:1]
#selecionar linhas e colunas 
colunas = ['conta', 'valor']
df[23:24][colunas]
#filtrar linhas atraves valor 
linhas = df['trimestre']== "lucro"
colunas = ['valor']
df[linhas][colunas].mean()

import seaborn as sns
import matplotlib.pyplot as plt
#grafico do lucro
linhas = df['conta'] == 'lucro'
colunas = ['trimestre', 'valor']
dados = df[linhas][colunas]
sns.lineplot(dados, x= 'trimestre', y='valor')
plt.title('Grafico do Lucro')
plt.xticks(rotation = 45)