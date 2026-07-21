# pip install sqlalchemy pymysql
from sqlalchemy import create_engine
import pandas as pd 

host = 'localhost'
user = 'root'
password = ''
database = 'bd_biblioteca'

engine = create_engine(
    f'mysql+pymysql://{user}:{password}@{host}/{database}'
)

# conectando no banco
try:
    df_usuarios = pd.read_sql('tb_usuarios', engine)
    df_livros = pd.read_sql('tb_livros', engine)
    df_alugados = pd.read_sql('tb_alugados', engine)
    df_itens_alugados = pd.read_sql('tb_itens_alugados', engine)

    print(df_livros.head())  # teste a conexão
except Exception as e:
    print(f'Falha na conexão {e}')


# Juntando os dataframes
try:
    df_merge1 = pd.merge(df_livros, df_itens_alugados, on='id_livro')
    df_merge2 = pd.merge(df_merge1, df_alugados, on='id_aluguel')
    df_final = pd.merge(df_merge2, df_usuarios, on='id_usuario')
    # print(df_final)
    
    filtro = (
        (df_final['data_devolucao'] >= '2024-11-01') &
        (df_final['data_devolucao'] <= '2024-11-30')
    )

    df_novembro = df_final[filtro]

    print(
        df_novembro[[
            'id_usuario', 'nome',
            'id_aluguel', 'data_aluguel', 'data_devolucao', 'valor',
            'id_livro', 'titulo'
        ]]
    )

except Exception as e:
    print(f'Erro tratamento dos dados {e}')




# ######  ATENÇÃO  #######:
# Quando os nomes das colunas são diferentes é necessário informar o parâmetro "left on" e "right_on", como no exemplo abaixo.
# No exemplo, left on é o nome do campo da primeira tabela e right_on é o nome do campo da segunda.
#
# df_merge = pd.merge(
#     df_clientes,
#     df_pedidos,
#     left_on='codigo_cliente',
#     right_on='cliente_codigo'
# )