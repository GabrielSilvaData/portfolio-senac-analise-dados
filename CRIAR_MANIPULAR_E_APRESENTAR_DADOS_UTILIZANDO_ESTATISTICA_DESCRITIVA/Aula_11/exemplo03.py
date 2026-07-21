# import pandas as pd 
import polars as pl  
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime


ENDERECO_DADOS = r'./../dados/'

try:
    print('Lendo arquivo Parquet')
    inicio = datetime.now()

    # Leitura Preguiçosa
    df_plano_execucao = pl.scan_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet')  # 

    df_bolsa_familia = df_plano_execucao.collect()
    print(df_bolsa_familia.head(10))

except Exception as e:
    print(f'Erro ao ler arquivo parquert {e}')





try:
    # array 
    array_valor_parcela = np.array(df_bolsa_familia['VALOR PARCELA'])

except Exception as e:
    print(f'Erro ao obter o Array {e}')

try:
    # import matplotlib.pyplot as plt
    # pip install matplotlib
    plt.boxplot(array_valor_parcela, vert=False)
    plt.title('Distribuição Bolsa Família')
    
    final = datetime.now()
    print(f'\nTotal do tempo gasto {final - inicio}')
    plt.show()

except Exception as e:
    print(f'Erro ao Plotar o Gráfico {e}')
