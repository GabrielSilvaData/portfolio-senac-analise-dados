# instala a biblioteca pandas
# pip install pandas

# comando para desinstalar a biblioteca
# pip uninstall pandas

# importa o pandas
import pandas as pd



# CRIAÇÃO DOS DADOS
# -----------------------------------------------

# dicionário contendo cargos e salários
dados = {
    'cargos': ['assistente', 'auxiliar', 'gerente'],
    'salários': [2500, 1800, 7500]
}


# exemplo de uso de método em string
# transforma a primeira letra em maiúscula
# 'python'.capitalize()



# EXIBIÇÃO DO DICIONÁRIO
# -----------------------------------------------
# exibe o dicionário completo
print(dados)

# mostra o tipo da variável
# nesse caso será dict
print(type(dados))



# USANDO O PANDAS
# -----------------------------------------------
# converte o dicionário em um DataFrame
# DataFrame funciona como uma tabela
df_dados = pd.DataFrame(dados)

# exibe o DataFrame completo
print(df_dados)



# EXIBINDO COLUNAS ESPECÍFICAS
# -----------------------------------------------
print('\nPrintando os Cargos: ')

# exibe apenas a coluna cargos
print(df_dados['cargos'])


print('\nPrintando os Salários: ')

# exibe apenas a coluna salários
# o nome precisa ser exatamente igual ao da coluna
print(df_dados['salários'])