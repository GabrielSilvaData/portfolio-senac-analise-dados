# 🗄️ Aula 05 – Relacionamentos em Banco de Dados e Integração com Pandas

Nesta aula foram aprofundados os conceitos de **modelagem de bancos de dados relacionais**, abordando a criação de **chaves primárias** e **chaves estrangeiras**, além da realização de consultas utilizando **JOIN** para relacionar informações de múltiplas tabelas.

Também foi demonstrado como integrar essas tabelas ao **Python** utilizando **Pandas**, realizando junções entre DataFrames e aplicando filtros para análise de dados.

## 📚 Conteúdos abordados:

- Conceito de banco de dados relacional.
- Criação de **Primary Key (Chave Primária)**.
- Criação de **Foreign Key (Chave Estrangeira)**.
- Relacionamento entre tabelas.
- Comando `ALTER TABLE`.
- Utilização de `AUTO_INCREMENT`.
- Consultas utilizando `JOIN`.
- Relacionamento entre múltiplas tabelas.
- Filtragem de registros utilizando:
  - `WHERE`
  - `BETWEEN`
- Conexão entre Python e MySQL utilizando SQLAlchemy.
- Importação de tabelas para DataFrames com `pd.read_sql()`.
- Junção de DataFrames utilizando `pd.merge()`.
- Utilização dos parâmetros:
  - `on`
  - `left_on`
  - `right_on`
- Tratamento de exceções durante a conexão e manipulação dos dados.

## 🧩 Exercícios desenvolvidos:

Durante a aula foram desenvolvidos exemplos práticos como:

- Criação das chaves primárias das tabelas de um sistema de biblioteca.
- Criação das chaves estrangeiras para estabelecer relacionamentos entre usuários, livros, empréstimos e itens emprestados.
- Consulta SQL relacionando diversas tabelas utilizando `JOIN`.
- Filtragem de empréstimos realizados em um período específico utilizando `BETWEEN`.
- Importação das tabelas do banco de dados para o Pandas.
- Realização de múltiplos `merge()` para consolidar informações em um único DataFrame.
- Filtragem dos empréstimos devolvidos durante o mês de novembro.
- Exibição das informações de usuários, livros, datas de empréstimo e devolução e valores dos empréstimos.

## 🎯 Objetivo da aula:

Compreender a importância dos relacionamentos em bancos de dados, aprender a utilizar **JOIN** para combinar informações de diferentes tabelas e integrar esses dados ao Python utilizando o Pandas, preparando conjuntos de dados completos para análise e geração de relatórios.
