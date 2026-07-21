import pandas as pd  # 0:06:34.962290
import polars as pl  # 0:00:51.861622
from datetime import datetime
import os

ENDERECO_DADOS = r'./../dados/'

try:
    print('Obtendo os dados')
    inicio = datetime.now()

    # Lista p/ guardar cada arquivo que termina com csv
    # Esta lista que utilizaremos
    lista_arquivos = []

    df_bolsa_familia = None

    # listar os nomes dos arquivos da pasta dados
    lista_dir_arquivos = os.listdir(ENDERECO_DADOS)

    # Verifica, se todos são CSVs
    for arquivo in lista_dir_arquivos:
        if arquivo.endswith('.csv'):
            lista_arquivos.append(arquivo)

    # print(lista_arquivos)

    # Leitura dos Arquivos
    for arquivo in lista_arquivos:
        df = pl.read_csv(ENDERECO_DADOS + arquivo, separator=';',  encoding='iso-8859-1')
        # df = pd.read_csv(ENDERECO_DADOS + arquivo, sep=';',  encoding='iso-8859-1')
        print(df.head())

        # Concatenar (Juntar os DataFraemes)
        if df_bolsa_familia is None:
            df_bolsa_familia = df
        else:
            df_bolsa_familia = pl.concat([df_bolsa_familia, df])  # Polars
            # df_bolsa_familia = pd.concat([df_bolsa_familia, df])  # Pandas

        del df
        
        print(f'\nArquivo {arquivo} processado com sucesso!')
        print(df_bolsa_familia.shape)

    
    df_bolsa_familia = df_bolsa_familia.with_columns(
        pl.col('VALOR PARCELA').str.replace(',', '.').cast(pl.Float64)
    )

    # Salvando em arquivo Parquet
    print('\nIniciando a Gravação do Arquivo Parquet...')
    df_bolsa_familia.write_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet')

    print('\nArquivo Parquet Salvo com sucesso...')
    final = datetime.now()
    print(f'\nTotal do tempo gasto {final - inicio}')

except Exception as e:
    print(f'Erro ao obter os dados {e}')


