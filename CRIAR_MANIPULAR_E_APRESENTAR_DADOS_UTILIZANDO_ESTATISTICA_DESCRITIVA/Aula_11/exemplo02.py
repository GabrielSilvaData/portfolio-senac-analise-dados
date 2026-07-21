import pandas as pd  # 0:06:34.962290
import polars as pl  # 0:00:51.861622
from datetime import datetime
# pip install fastparquet  # Para ler o arquivo parquet

ENDERECO_DADOS = r'./../dados/'

try:
    print('Lendo arquivo Parquet')
    inicio = datetime.now()

    # Leitura Direta
    # df_bolsa_familia = pd.read_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet')  # 00:36
    df_bolsa_familia = pl.read_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet')  # # 00:12
    # print(df_bolsa_familia.head())

    df_filtrado = df_bolsa_familia.filter(pl.col('VALOR PARCELA') > 2500)
    print(df_filtrado.shape)

    # Ordenando e mostrando os 20 primeiros
    # print(df_bolsa_familia.sort('VALOR PARCELA', descending=True).head(20))

    final = datetime.now()
    print(f'\nTotal do tempo gasto {final - inicio}')

except Exception as e:
    print(f'Erro ao ler arquivo parquert {e}')
