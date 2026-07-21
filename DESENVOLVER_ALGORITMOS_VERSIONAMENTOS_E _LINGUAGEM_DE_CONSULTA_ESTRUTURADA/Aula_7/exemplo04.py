# ------------------------------------------------------------------------
# dicionario = {} => Cria vazio
# dicionario["chave"] = valor => Adiciona/Modifica
# print(dicionario["chave"]) => Acessa valor
# del dicionario["chave"] => Remove item
# dicionario.clear() => Limpa tudo dentro do dicionário
# ------------------------------------------------------------------------

# criando um dicionário com produtos e seus preços
# criando um dicionário com dados de uma pessoa
pessoa = {}

pessoa["nome"] = "João"
pessoa["idade"] = 25
pessoa["cidade"] = "Niterói"

print(pessoa)  # mostrando o dicionário

# acessando uma chave específica
print(pessoa["nome"])  # nome da pessoa

# alterando o valor de uma chave
pessoa["idade"] = 26

# adicionando uma nova chave 
pessoa["profissao"] = "Programador"

# removendo uma informação
del pessoa["cidade"]

print(pessoa)
