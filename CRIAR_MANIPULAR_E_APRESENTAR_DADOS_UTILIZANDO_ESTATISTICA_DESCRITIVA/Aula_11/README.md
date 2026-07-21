# 📊 Aula 11 – Processamento de Dados com Polars e Arquivos Parquet

Nesta aula foi aprofundado o uso da biblioteca **Polars** para o processamento de grandes volumes de dados. Foram apresentadas técnicas para automatizar a leitura de múltiplos arquivos CSV, consolidar todas as informações em um único DataFrame, converter tipos de dados, salvar o resultado no formato **Parquet** e realizar análises de forma mais eficiente utilizando leitura preguiçosa (*Lazy Loading*).

A base de dados utilizada foi a do **Novo Bolsa Família**, disponibilizada pelo **Portal da Transparência**.

## 📚 Conteúdos abordados:

- Automatização da leitura de arquivos utilizando o módulo `os`.
- Identificação automática de arquivos CSV em uma pasta.
- Processamento de múltiplos arquivos com laços de repetição.
- Consolidação de DataFrames utilizando `pl.concat()`.
- Conversão de tipos de dados com `with_columns()` e `cast()`.
- Tratamento de valores numéricos armazenados como texto.
- Geração e gravação de arquivos no formato **Parquet**.
- Leitura de arquivos Parquet utilizando `read_parquet()`.
- Comparação de desempenho entre leitura de arquivos CSV e Parquet.
- Filtragem de registros utilizando `filter()`.
- Introdução ao conceito de **Leitura Preguiçosa (Lazy Loading)** com `scan_parquet()`.
- Execução do plano de processamento com `collect()`.
- Conversão de colunas para arrays NumPy.
- Construção de Boxplots utilizando Matplotlib.
- Medição do tempo de execução para avaliação de desempenho.

## 🧩 Exercícios desenvolvidos:

Durante a aula foram desenvolvidos exemplos práticos como:

- Leitura automática de todos os arquivos CSV presentes em um diretório.
- Consolidação de diversos meses da base do Bolsa Família em um único DataFrame.
- Conversão da coluna **VALOR PARCELA** para o tipo numérico.
- Exportação da base consolidada para o formato **Parquet**.
- Leitura do arquivo Parquet para comparação de desempenho.
- Filtragem de beneficiários com parcelas acima de um determinado valor.
- Utilização da leitura preguiçosa (*Lazy Loading*) para otimizar consultas.
- Conversão dos dados para arrays NumPy.
- Construção de Boxplots para análise da distribuição dos valores das parcelas.

## 🎯 Objetivo da aula:

Compreender como utilizar o **Polars** para processar grandes volumes de dados de forma eficiente, automatizando a leitura de arquivos, utilizando o formato **Parquet** para melhorar o desempenho e aplicando técnicas como **Lazy Loading** para otimizar consultas e análises estatísticas em projetos de Ciência e Análise de Dados.
