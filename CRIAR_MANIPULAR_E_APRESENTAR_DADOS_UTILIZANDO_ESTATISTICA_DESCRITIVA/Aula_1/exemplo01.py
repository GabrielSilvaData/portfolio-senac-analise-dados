import pandas as pd

print('Listas do Python x Séries do Pandas')

produtos = ['Notebooks', 'Smartphone', 'Tablet', 'Smartwatch', 'Câmera']
quantidade_estoque = [15, 30, 20, 10, 25]
print(produtos)
print(quantidade_estoque)

series = pd.Series(produtos)
print(series)


# índice personalizado
estoque = pd.Series(quantidade_estoque, index=produtos)
print(estoque)


# Tipos
# print(type(series))
# print(type(quantidade_estoque))
