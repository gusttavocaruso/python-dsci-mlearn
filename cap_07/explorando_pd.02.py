import pandas as pd

transport = pd.read_csv('./files/transportes.csv', index_col=0)

print(transport)

print(transport.loc['Motocicleta'])
