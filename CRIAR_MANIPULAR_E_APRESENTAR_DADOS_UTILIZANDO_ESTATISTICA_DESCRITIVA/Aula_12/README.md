### Continuação da Aula

Na continuação da aula foi explorado o conceito de **Pipeline de Processamento** utilizando **Lazy Loading** do Polars. As transformações passaram a ser definidas antes do carregamento dos dados em memória, permitindo consultas mais rápidas e eficientes em arquivos Parquet.

#### 📚 Conteúdos abordados:

- Configuração da exibição de números sem notação científica (`pl.Config.set_fmt_float()`).
- Construção de um plano de execução utilizando `scan_parquet()`.
- Seleção de colunas com `select()`.
- Conversão de colunas para o tipo `Categorical`.
- Agrupamento de registros utilizando `group_by()`.
- Agregação dos valores com `agg()`.
- Ordenação dos resultados utilizando `sort()`.
- Execução do pipeline com `collect()`.
- Medição do tempo de processamento após a execução do plano.

#### 🧩 Exercício desenvolvido:

- Construção de um pipeline para calcular o valor total das parcelas do Bolsa Família por município.
- Agrupamento dos municípios e soma dos valores pagos.
- Ordenação dos municípios em ordem decrescente pelo valor total recebido.
- Comparação da eficiência do processamento utilizando Lazy Loading.

#### 🎯 Objetivo

Demonstrar como o **Polars Lazy API** permite criar um pipeline de transformações antes da leitura efetiva dos dados, tornando o processamento de grandes bases mais eficiente e reduzindo o consumo de memória.
