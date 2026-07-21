# -----------------------------------------------------------
# INSTALAÇÃO DAS BIBLIOTECAS
# pip install sqlalchemy pymysql pandas

# sqlalchemy: Biblioteca utilizada para conexão e manipulação de bancos de dados utilizando Python.
# pymysql: Driver responsável por permitir a comunicação entre o Python e o MySQL.


# IMPORTAÇÃO DAS BIBLIOTECAS
from sqlalchemy import create_engine
import pandas as pd


# VARIÁVEIS DE CONEXÃO
host = 'localhost'  # endereço do servidor no PC atual. Pode ser 127.0.0.1 também
user = 'root'  # usuário do banco
password = ''  # senha do banco
database = 'bd_mod2_aula04'  # nome do banco de dados



# CRIANDO A URL DE CONEXÃO 
# create_engine() é uma Função do SQLAlchemy utilizada para criar a conexão com o banco de dados.
# Esta parte "mysql+pymysql" informa que o mysql é o banco utilizado e pymysql o driver de conexão.
# Aqui usamos as variáveis de conexão criadas anteriormente, seguindo sempre este modelo.
engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')


# Comando SQL ou 'script' responsável por selecionar os dados da tabela.
query = 'SELECT produto, `preço unitario` FROM cadastro_produtos;'


# pd.read_sql() é um método do pandas, que lê os dados do banco através da conexão criada.
# usamos a query sql criada anteriormente e a url de conexão
df_produtos = pd.read_sql(query, engine)


# Mostra os dados obtidos do banco.
print(df_produtos)