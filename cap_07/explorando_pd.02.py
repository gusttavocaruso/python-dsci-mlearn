import pandas as pd

transport = pd.read_csv('./files/transportes.csv', index_col=0)

print(transport)

# Busca informações sobre Motocicleta
print(transport.loc['Motocicleta'])

# Excluir linhas 2, 4
print(transport.drop(['Helicóptero', 'Motoplanador']))

# Excluir coluna Autonomia
print(transport.drop('Autonomia', axis = 1)) #metodo axis identifica que é uma coluna

# Excluir duas colunas pelo nome
print(transport.drop(['Peso', 'Consumo'], axis = 1))


# DICA para excluir registros com caracteristica especifica (por ex: consumo zero e peso 450)
autonomia_zero = transport.index[transport.Consumo == 0].tolist()
peso_zero = transport.index[transport['Peso'] == 450].tolist()

temp = autonomia_zero + peso_zero
print(transport.drop(temp))
