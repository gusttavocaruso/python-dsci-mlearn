import pandas as pd

datafr = pd.DataFrame({
    'Nome': ['Alice', 'Alice', 'Alice', 'Roberto', 'Roberto', 'Roberto'],
    'Idade': ['19', '22', '32', '19', '22', '32'],
    'Identificação': [1, 2, 3, 4, 5, 6],
    'Cursos': ['Direito', 'Administração', 'Matemática', 'Arquiterura', 'Design', 'Engenharia']
})

print(datafr)

# Pivotando a coleção
print(datafr.pivot(index='Cursos', columns='Nome', values='Identificação'))

print(datafr.pivot(index='Cursos', columns='Nome', values=['Identificação', 'Idade']))
