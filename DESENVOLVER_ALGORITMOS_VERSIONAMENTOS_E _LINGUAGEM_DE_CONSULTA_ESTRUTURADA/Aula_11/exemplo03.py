# instala as bibliotecas necessárias
# sqlalchemy -> cria a conexão entre Python e banco de dados
# pymysql -> permite a comunicação com o MySQL
# pandas -> utilizado para análise e manipulação de dados
# pip install sqlalchemy pymysql

# importa a função create_engine da biblioteca sqlalchemy
from sqlalchemy import create_engine

# importa o pandas
import pandas as pd



# DADOS DE CONEXÃO COM O BANCO
# -----------------------------------------------
# endereço do servidor do banco de dados
host = 'localhost'
# usuário do MySQL
user = 'root'
# senha do MySQL
password = ''
# nome do banco de dados
database = 'bd_aula11'



# CRIAÇÃO DA CONEXÃO
# -----------------------------------------------
# cria a conexão com o banco MySQL
# mysql+pymysql -> informa o tipo do banco e o driver utilizado
engine = create_engine(
    f'mysql+pymysql://{user}:{password}@{host}/{database}'
)


# LEITURA DA TABELA
# -----------------------------------------------
# lê os dados da tabela tb_produtos
# e armazena em um DataFrame do pandas
df = pd.read_sql('tb_produtos', engine)



# EXIBIÇÃO DOS DADOS
# 
# exibe as 5 primeiras linhas da tabela
print(df.head())