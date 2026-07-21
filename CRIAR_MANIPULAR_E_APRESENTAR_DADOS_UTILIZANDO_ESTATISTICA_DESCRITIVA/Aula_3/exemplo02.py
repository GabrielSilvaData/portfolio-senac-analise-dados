# -----------------------------------------------------------
# IMPORTAÇÃO DAS BIBLIOTECAS

# Pandas
# Biblioteca utilizada para análise e manipulação de dados.
# Trabalha com chamados DataFrames,
# que são estruturas tabulares "tabela".
#
# Benefícios:
# - Facilita leitura de arquivos CSV e Excel
# - Permite criar filtros e consultas rapidamente
# - Ajuda no tratamento e organização de dados
# - Muito utilizada em Ciência de Dados e Análise de Dados
import pandas as pd



# NumPy
# Biblioteca voltada para cálculos numéricos e operações matemáticas.
# É muito rápida e eficiente para trabalhar com grandes volumes de dados.
#
# Benefícios:
# - Operações matemáticas de alta performance
# - Possui funções estatísticas prontas
# - Trabalha com Arrays NumPy
# - Base para várias bibliotecas de dados e IA
import numpy as np



# Biblioteca do Python utilizada para interação com o sistema operacional.
# Neste código ela está sendo usada para limpar a tela do terminal.
import os


# -----------------------------------------------------------
# LIMPANDO A TELA
# O comando 'cls' limpa o terminal no Windows.
# Em Linux normalmente usamos 'clear'.
os.system('cls')



# -----------------------------------------------------------
# LEITURA DO ARQUIVO CSV
# read_csv()
# Função do Pandas utilizada para ler arquivos CSV.
# O conteúdo do arquivo será armazenado em um DataFrame.

# DataFrame:
# Estrutura de dados do Pandas parecida com uma tabela
# contendo linhas e colunas.
df_planilha_custos = pd.read_csv('planilha_de_custos.csv')


# -----------------------------------------------------------
# MOSTRANDO OS DADOS
print('\nDados Obtido')

print(100 * '-')


# head()
# Mostra as primeiras linhas do DataFrame.
# Muito utilizado para visualizar as 5 primeiras linhas do DataFrame.
print(df_planilha_custos.head())


# -----------------------------------------------------------
# PREPARAÇÃO DOS DADOS
# Criando uma nova coluna chamada:
# 'Custo Total (R$)'
#
# Fórmula utilizada:
#
# custo total =
# preço de compra +
# imposto +
# frete +
# taxa operacional

df_planilha_custos['Custo Total (R$)'] = (

    # Valor original do produto
    df_planilha_custos['Preco de Compra (R$)'] 

    +

    # Cálculo do imposto
    (
        df_planilha_custos['Preco de Compra (R$)']
        *
        df_planilha_custos['Imposto (%)']
        / 100
    )

    +

    # Soma do frete
    df_planilha_custos['Frete (R$)']

    +

    # Soma da taxa operacional
    df_planilha_custos['Taxa Operacional (R$)']
)

# Pulando linha
print()

# Mostrando novamente as primeiras linhas
# agora com a nova coluna criada
print(df_planilha_custos.head())

print()


# Selecionando apenas duas colunas (opcional):
# Produto e Custo Total [['coluna1', 'coluna2']]
# é usado para selecionar múltiplas colunas.
print(df_planilha_custos[['Produto', 'Custo Total (R$)']].head(10))




# -----------------------------------------------------------
# USO DA BIBLIOTECA NUMPY

# np.array()
# Converte os dados da coluna do Pandas "séries" em um Array NumPy.
#

# Array NumPy:
# Estrutura semelhante a listas do Python,
# porém muito mais rápida e otimizada para cálculos matemáticos.
#
# Benefícios do Array NumPy:
# - Maior desempenho
# - Menor consumo de memória
# - Ideal para cálculos estatísticos e científicos

# Criando um array com os dados da coluna "Custo Total (R$)"
array_custo_total = np.array(
    df_planilha_custos['Custo Total (R$)']
)

# print(array_custo_total)


# -----------------------------------------------------------
# MEDIDAS DE TENDÊNCIA CENTRAL
print('\nMedidas de Tendência Central')
print(30 * "=")



# np.mean() Calcula a média dos valores.
media = np.mean(array_custo_total)
print(f'\nMédia dos Custos: {media:.2f}')


# Mediana:
# Valor central da sequência ordenada.
# np.median()  Calcula a mediana dos valores.
mediana = np.median(array_custo_total)
print(f'\Mediana dos Custos: {mediana}')




# -----------------------------------------------------------
# MEDIDAS DE POSIÇÃO - QUARTIS

# np.quantile()
# Calcula quartis e outras divisões estatísticas.

# Quartis:
# Dividem os dados em 4 partes.

# Primeiro Quartil (25%)
q1 = np.quantile(array_custo_total, 0.25)

# Segundo Quartil (50%)
# Equivale à mediana
q2 = np.quantile(array_custo_total, 0.50)

# Terceiro Quartil (75%)
q3 = np.quantile(array_custo_total, 0.75)




print('\nMedidas de Posição')

print(30 * "=")

print(f'Q1: {q1}')

print(f'Q2: {q2}')

print(f'Q3: {q3}')

