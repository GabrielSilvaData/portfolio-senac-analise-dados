# pip install openpyxl   ---- P/ ler planilhas do Excel
import pandas as pd

df_eletricos = pd.read_excel('vendas_eletronicos.xlsx')

# Primeiras
print(df_eletricos.head(10))

# 
print('\n Maior Valor do Faturamento')
print(45 * '=')
print(df_eletricos.loc[df_eletricos['Faturamento Total (R$)'].idxmax(), 'Produto'])
# print(df_eletricos.loc[df_eletricos['Faturamento Total (R$)'].idxmax()])  # linha inteira
print(df_eletricos['Faturamento Total (R$)'].max())


print('\n Menor Valor do Faturamento')
print(45 * '=')
print(df_eletricos.loc[df_eletricos['Faturamento Total (R$)'].idxmin(), 'Produto'])
print(df_eletricos['Faturamento Total (R$)'].min())


print('\n Total de Unidades Vendidas')
print(45 * '=')
print(df_eletricos['Unidades Vendidas'].sum())


print('\n Média dos Preços')
print(45 * '=')
media_precos = df_eletricos['Preco por Unidade (R$)'].mean()
print(f'Média: {media_precos}')


print('\n Produtos acima da média')
print(45 * '=')
media = df_eletricos['Faturamento Total (R$)'].mean()
print(df_eletricos[df_eletricos['Faturamento Total (R$)'] >= media])











