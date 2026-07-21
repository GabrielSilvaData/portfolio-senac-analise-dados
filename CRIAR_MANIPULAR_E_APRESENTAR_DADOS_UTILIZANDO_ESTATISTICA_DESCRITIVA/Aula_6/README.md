# 📊 Aula 06 – Análise Estatística Descritiva e Visualização de Dados

Nesta aula foram aprofundados os conceitos de **Estatística Descritiva** aplicados à análise de dados reais utilizando as bibliotecas **Pandas**, **NumPy** e **Matplotlib**. Os dados foram obtidos a partir de uma base pública do **Instituto de Segurança Pública do Rio de Janeiro (ISP-RJ)**, permitindo realizar análises sobre ocorrências de roubo de veículos por município.

Além da análise estatística, foram desenvolvidas visualizações gráficas para facilitar a interpretação dos resultados.

## 📚 Conteúdos abordados:

- Importação das bibliotecas:
  - Pandas
  - NumPy
  - Matplotlib
- Leitura de arquivos CSV hospedados na internet utilizando `read_csv()`.
- Tratamento da codificação de caracteres (`encoding`).
- Seleção de colunas específicas.
- Agrupamento de dados utilizando `groupby()`.
- Soma de valores por categoria.
- Ordenação de dados com `sort_values()`.
- Conversão de Series para Arrays NumPy.
- Cálculo de medidas de tendência central:
  - Média (`np.mean()`)
  - Mediana (`np.median()`)
- Comparação entre média e mediana.
- Cálculo de medidas de posição:
  - Primeiro Quartil (Q1)
  - Segundo Quartil (Q2)
  - Terceiro Quartil (Q3)
- Identificação de municípios acima e abaixo dos quartis.
- Cálculo de medidas de dispersão:
  - Valor máximo
  - Valor mínimo
  - Amplitude Total
- Identificação de outliers utilizando o método do **Intervalo Interquartil (IQR)**.
- Criação de gráficos de barras horizontais utilizando Matplotlib.
- Tratamento de exceções com `try` e `except`.

## 🧩 Exercícios desenvolvidos:

Durante a aula foram desenvolvidos exemplos práticos como:

- Importação de uma base pública de ocorrências de roubo de veículos do ISP-RJ.
- Agrupamento das ocorrências por município.
- Cálculo da média e mediana dos roubos de veículos.
- Determinação dos quartis da distribuição dos dados.
- Identificação dos municípios com maiores e menores índices de roubo.
- Cálculo da amplitude total da distribuição.
- Identificação de possíveis outliers utilizando o método IQR.
- Construção de gráficos comparando os municípios com maiores e menores quantidades de roubos.

## 🎯 Objetivo da aula:

Aplicar técnicas de Estatística Descritiva em um conjunto de dados reais, utilizando Pandas e NumPy para análise estatística e Matplotlib para visualização gráfica, desenvolvendo habilidades fundamentais para exploração, interpretação e apresentação de dados na área de Análise de Dados.
