import pandas as pd

df = pd.read_csv('./files/tempo_salarios.02.csv')

# coleção com valores vazio NaN
print(df)

# substitui NaN por valor ()
print(df.fillna('x'))

# estratégia: substituir por NaN por medidas estatisticas
print(df.fillna(df.mean()))
print(df.fillna(df.median()))
print(df.fillna(df.mode()))
print(df.fillna(df.std()))
print(df.fillna(df.var()))

# estratégia: interpolar os valores anterior/posterior da lista
print(df.fillna(df.interpolate()))
