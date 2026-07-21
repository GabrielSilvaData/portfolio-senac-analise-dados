# ======================================
# ####### EXEMPLO 1 - Função de saudação


# DEFINIÇÃO DA FUNÇÃO
# Função que apenas exibe uma mensagem (Esta função não recebe nenhum parâmetro)
# A indentação é importante, para o python saber quaiscomandos estão dentro da função
def saudacao_inicial():
    print(f'Oim como vai?')


# chamada da função
# apenas depois da chamada a função é executada
saudacao_inicial()

# Podemos chamar a função quantas vezes quisermos
saudacao_inicial()
saudacao_inicial()
saudacao_inicial()
saudacao_inicial()
# ---------------------------------------------------------------------



# ####### EXEMPLO 2 - Função de saudação
# DEFINIÇÃO DA FUNÇÃO
# FUNÇÃO QUE RECEBE PARÂMETRO
# Os parâmentros recebidos vem dentro dos parênteses.
# No exemplo, a função recebe um parâmetro chamado x
def saudacao(x):
    print(f'Oi, {x} como vai?')


# Criamos uma variável recebendo um nome por atribuição
nome = 'Anna'

# CHAMADA DA FUNÇÃO
# Passamos a variável "nome" por parâmentro para a função
# O valor da variável nome 'Anna', será enviado para o parâmetro x
# da função saudacao(x), que foi definida mais acima.
# Então o parâmetro x passa a ter o valor 'Anna' dentro dele.
# Logo em seguida o bloco da função é executado, printando a saudação, já com o nome da pessoa.
# "Oi Anna, como va?"
saudacao(nome)
# ---------------------------------------------------------------------




# ------------------------
# ####### EXEMPLO 3 - USO COM REPETIÇÃO
# Aqui estamos chamando a função 5 vezes usando o for, 
# então a função será executada 5 vezes.
nome = 'Pedro'
for i in range(5):
    # ERRO COMUM: a função exige um argumento
    # saudacao() - Isso daria erro

    # Correto: precisamos passar um valor, pois a função saudacao(x):
    saudacao(nome)


# SAÍDA IMPRESSA NA TELA
# "Oi Pedro, como va?"
# "Oi Pedro, como va?"
# "Oi Pedro, como va?"
# "Oi Pedro, como va?"
# "Oi Pedro, como va?"
# ---------------------------------------------------------------------




# ======================================
# EXEMPLO 4 - Função com mais de um parâmetros (soma)

# DEFINIÇÃO DA FUNÇÃO
# Recebe dois valores (a e b) e calcula a soma
# Observe que os valores respeitam a ordem que forem chamados. 
# Como n1 = 10 e n2 = 25, realizando a chamada da função soma(n1, n2), por de baixo dos panos
# o que está ocorrendo é soma(10, 25), pois n1 é o primeiro parâmetro e vale 10, n2 é o segundo valendo 25.
# Na definição da função, observe "def somar(a, b):" O parâmetro "a" vem primeiro, então "a" recebe
# o valor de "n1", que também é o primeiro valor na chamada da função soma(n1, n2), e "b" recebe o valor de "n2".
# Ou seja, as funções seguem a ordem dos parâmetros que são enviados.
def somar(a, b):
    print(f'O valor de a é {a}')
    print(f'O valor de b é {b}')
    r = a + b  # realiza o cálculo
    
    # Exibe o resultado (não usa return)
    print(f'Resposta {r}')


# Criamos duas variáveis
n1 = 10
n2 = 25

# Chamamos a função passando os valores
# n1 → vai para 'a'
# n2 → vai para 'b'
somar(n1, n2)


# SAÍDA NA TELA
# O valor de a é 10
# O valor de b é 25
# Resposta 35
# ---------------------------------------------------------------------