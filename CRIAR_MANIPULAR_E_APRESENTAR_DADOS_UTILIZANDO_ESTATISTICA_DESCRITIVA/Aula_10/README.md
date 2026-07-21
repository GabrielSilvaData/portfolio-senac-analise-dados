# 📊 Aula 10 – Processamento de Grandes Volumes de Dados com Polars

Nesta aula foi apresentada a biblioteca **Polars**, uma alternativa ao **Pandas** desenvolvida para processamento de grandes volumes de dados com maior desempenho. Foram realizados testes comparativos de leitura de arquivos CSV, medindo o tempo de execução entre as duas bibliotecas e demonstrando como automatizar a importação e consolidação de múltiplos arquivos do programa **Novo Bolsa Família**.

A base de dados utilizada foi obtida no **Portal da Transparência**, contendo informações mensais dos pagamentos do programa Bolsa Família.

## 📚 Conteúdos abordados:

- Introdução à biblioteca **Polars**.
- Diferenças entre **Pandas** e **Polars**.
- Leitura de arquivos CSV utilizando `pl.read_csv()`.
- Configuração de separador (`separator`) e codificação (`encoding`).
- Medição do tempo de execução utilizando `datetime`.
- Visualização das primeiras linhas dos dados com `head()`.
- Consulta das colunas (`columns`) e dimensões (`shape`) do DataFrame.
- Automatização da leitura de múltiplos arquivos CSV.
- Utilização de listas para processar vários meses de dados.
- Consolidação de diversos DataFrames utilizando `pd.concat()`.
- Liberação de memória durante o processamento com `del`.

## 🧩 Exercícios desenvolvidos:

Durante a aula foram desenvolvidos exemplos práticos como:

- Comparação do desempenho entre Pandas e Polars na leitura de arquivos CSV.
- Importação da base de dados do Novo Bolsa Família.
- Medição do tempo de processamento das bibliotecas.
- Visualização da estrutura e das informações do conjunto de dados.
- Leitura automática de diversos arquivos mensais utilizando um laço de repetição.
- Consolidação dos dados de vários meses em um único DataFrame.
- Preparação de uma base unificada para análises futuras.

## 🎯 Objetivo da aula:

Compreender as vantagens da biblioteca **Polars** para o processamento de grandes conjuntos de dados, comparando seu desempenho com o Pandas e aprendendo técnicas para automatizar a leitura e consolidação de múltiplos arquivos CSV, tornando o processamento mais eficiente em projetos de análise de dados.
