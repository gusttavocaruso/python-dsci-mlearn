import pandas as pd

transport = pd.read_csv('./files/transportes.csv', index_col=0)

print(transport)

print(transport.loc['Motocicleta'])

# Excluir linhas 2, 4
print(transport.drop(['Helicóptero', 'Motoplanador']))

# Excluir coluna Autonomia
print(transport.drop('Autonomia', axis = 1)) #metodo axis identifica que é uma coluna

# Excluir duas colunas pelo nome
print(transport.drop(['Peso', 'Consumo'], axis = 1))
