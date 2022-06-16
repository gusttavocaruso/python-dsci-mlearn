import pandas as pd

dataframe = pd.read_csv('./files/tempo_salarios.csv')

print(dataframe)
print(dataframe['AnosdeExperiencia'])
print(dataframe.Salario)
print(dataframe['Salario'][5:11])

# Tamanho da coleção
print(len(dataframe))

# Tipo dos dados da coleção
print(dataframe.dtypes)

# Limitar consulta para começo/fim (head/tail) de coleção
print(dataframe.head())
print(dataframe.tail())
print(dataframe.head(10))

# Lista com Tamanho, Média, Desvio Padrão, Minimo, Máximo e Quartis de coleção
print(dataframe.describe())

# Somente valores númericos das colunas
print(dataframe.Salario[5:11].values)


# Acessar um item da coleção diretamente
print(dataframe.loc[4])
print(dataframe.iloc[4])

# Filtrar valores
print(dataframe.loc[dataframe.Salario > 80000])

# Selecionar unica coluna >> iloc[intervalo_linha, intervalo_coluna]
print(dataframe.iloc[0:6, 0:1])
print(dataframe.iloc[0:6, 1:])

# Converter dados em uma Matriz NumPy
print(dataframe.iloc[0:6, 0:1].values)
