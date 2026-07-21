# 🗄️ Aula 04 – Consultas SQL e Integração com Python

Nesta aula foram apresentados os conceitos fundamentais da **Linguagem de Consulta Estruturada (SQL)** para realizar consultas em bancos de dados relacionais. Também foi demonstrado como integrar o **Python** ao **MySQL** utilizando as bibliotecas **SQLAlchemy**, **PyMySQL** e **Pandas**, permitindo executar consultas SQL e importar os resultados para análise em DataFrames.

## 📚 Conteúdos abordados:

- Instalação das bibliotecas:
  - SQLAlchemy
  - PyMySQL
  - Pandas
- Configuração da conexão entre Python e MySQL.
- Criação da conexão utilizando `create_engine()`.
- Leitura de consultas SQL com `pd.read_sql()`.
- Estrutura básica de consultas SQL.
- Comando `SELECT`.
- Seleção de colunas específicas.
- Filtragem de registros utilizando `WHERE`.
- Comparações com operadores relacionais (`>`, `<`, `=`).
- Ordenação de resultados utilizando `ORDER BY`.
- Ordenação crescente (`ASC`) e decrescente (`DESC`).
- Operadores lógicos:
  - `AND`
  - `OR`
- Pesquisa de registros utilizando `LIKE`.
- Diferença entre aspas (`''`) e crases (```` `` ````) em comandos SQL.

## 🧩 Exercícios desenvolvidos:

Durante a aula foram desenvolvidos exemplos práticos como:

- Conexão entre Python e um banco de dados MySQL.
- Importação de dados da tabela **cadastro_produtos** para um DataFrame do Pandas.
- Consulta de produtos e preços utilizando SQL.
- Filtragem de produtos por:
  - Marca.
  - Tipo de produto.
  - Faixa de preço.
- Ordenação dos produtos por preço.
- Pesquisa de produtos utilizando o operador `LIKE`.
- Resolução de exercícios utilizando uma base de dados de materiais de construção, realizando consultas por:
  - Categoria.
  - Fornecedor.
  - Preço dos produtos.

## 🎯 Objetivo da aula:

Aprender os fundamentos da linguagem SQL e sua integração com Python, desenvolvendo consultas para extrair, filtrar e organizar informações armazenadas em bancos de dados relacionais, preparando os dados para análises utilizando o Pandas.
