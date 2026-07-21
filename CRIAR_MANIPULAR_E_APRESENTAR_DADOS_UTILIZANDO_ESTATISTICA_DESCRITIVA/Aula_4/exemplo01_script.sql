
SELECT * FROM cadastro_produtos;

SELECT Produto, Marca FROM cadastro_produtos;
SELECT * FROM cadastro_produtos;
WHERE Marca = 'Logitech';

-- OBS: Sobre as aspas x as crases: Entre aspas os textos são considerados como textos "strings" 
-- e entre crases são considerados como nomes de colunas ou tabelas
-- Neste exemplo: `Preço Unitario` está entre CRASES, logo é o nome de uma coluna da tabela e
-- no exemplo anterior, 'Logitech', com ASPAS, é um texto comum, sendo usado para comparação.
SELECT * FROM cadastro_produtos
WHERE `Preço Unitario` > 20
ORDER BY `Preço Unitario` ASC;  -- DESC

SELECT Produto, `Preço Unitario`
FROM cadastro_produtos
ORDER BY `Preço Unitario` DESC;

SELECT * FROM cadastro_produtos
WHERE Marca = 'Hashtag'
AND `Preço Unitario` <  25;

SELECT * FROM cadastro_produtos
WHERE `tipo do produto` = 'Mouse'
AND (`marca` = 'Logitech' OR `marca` = 'Multilaser');

SELECT Produto, Marca, `Preço Unitario`
FROM cadastro_produtos
WHERE `Preço Unitario` > 20
AND Marca = 'Hashtag'
ORDER BY `Preço Unitario`;

SELECT * FROM cadastro_produtos
WHERE Produto LIKE '%tv%';  -- procurando um produto, que no nome aparece a palavra 'tv'

