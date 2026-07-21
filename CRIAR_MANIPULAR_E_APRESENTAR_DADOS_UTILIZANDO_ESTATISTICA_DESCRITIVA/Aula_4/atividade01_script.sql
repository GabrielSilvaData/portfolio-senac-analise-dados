
-- ATIVIDADE 1 – BÁSICO

-- 1. Mostrar todos os dados da tabela
SELECT * FROM materiais_construcao;

-- 2. Mostrar apenas produto e preço
SELECT produto, preco FROM materiais_construcao;



-- ATIVIDADE 2 – WHERE SIMPLES
-- 1. Mostrar apenas produtos da categoria "cimento"
SELECT * 
FROM materiais_construcao
WHERE categoria = 'cimento';

-- 2. Mostrar produtos com preço maior que 200
SELECT * 
FROM materiais_construcao
WHERE preco > 200;

-- 3. Mostrar produtos do fornecedor "local"
SELECT * 
FROM materiais_construcao
WHERE fornecedor = 'local';
