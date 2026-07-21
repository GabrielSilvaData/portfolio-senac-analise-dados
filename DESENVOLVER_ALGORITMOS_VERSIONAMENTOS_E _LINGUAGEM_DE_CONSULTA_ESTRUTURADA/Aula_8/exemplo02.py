# ======================================
# ####### EXEMPLO - Função com repetição (entrada de dados + cálculo)

# DEFINIÇÃO DA FUNÇÃO
# Esta função recebe dois parâmetros (a e b)
# Esses parâmetros representam os valores que serão somados
def somar(a, b):
    # Aqui realizamos o cálculo da soma
    r = a + b

    # Exibimos o resultado diretamente na tela
    print(f'Resposta {r}')



# USO COM REPETIÇÃO (FOR)
# O laço for será executado 3 vezes
# Isso significa que o usuário irá digitar os números 3 vezes
for i in range(3):

    # A cada repetição, o usuário informa dois valores
    # input() sempre retorna texto, por isso usamos int() para converter para número inteiro
    n1 = int(input('Número1: '))
    n2 = int(input('Número2: '))

    # CHAMADA DA FUNÇÃO
    # Passamos os valores digitados para a função
    # n1 será enviado para o parâmetro "a"
    # n2 será enviado para o parâmetro "b"
    somar(n1, n2)

    # Após a chamada:
    # 1. A função recebe os valores
    # 2. Realiza o cálculo (a + b)
    # 3. Exibe o resultado com print()
    # 4. O programa volta para o laço e repete o processo


# ---------------------------------------------------------------------

# SAÍDA ESPERADA (exemplo)
# Número1: 5
# Número2: 3
# Resposta 8
#
# Número1: 10
# Número2: 2
# Resposta 12
#
# Número1: 7
# Número2: 1
# Resposta 8
#
# (repete 3 vezes no total)