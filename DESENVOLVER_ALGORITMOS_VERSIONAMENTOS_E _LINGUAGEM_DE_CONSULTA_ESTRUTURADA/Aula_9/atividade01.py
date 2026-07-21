# ======================================
# ####### EXEMPLO - Calculadora com funções e menu


# IMPORTAÇÃO DE BIBLIOTECAS
# random: utilizado para gerar números aleatórios
import random

# os: utilizado para executar comandos do sistema (ex: limpar a tela)
import os


# -------------------------------------
# DEFINIÇÃO DAS FUNÇÕES
# Cada função representa uma operação matemática básica
# Essa separação organiza o código e facilita reutilização

# Todas as funções recebem dois parâmetros (x e y),
# que precisam ser enviados

def soma(x, y):
    # retorna a soma de dois valores
    return x + y


def subtracao(x, y):
    # retorna a subtração entre dois valores
    return x - y


def multiplica(x, y):
    # retorna a multiplicação entre dois valores
    return x * y


def divisao(x, y):
    # retorna a divisão entre dois valores
    # atenção: divisão por zero geraria erro
    return x / y



# PROGRAMA PRINCIPAL
# LIMPEZA DA TELA
# Este código com 'cls' funciona no Windows para limpar o terminal
# Em outros sistemas (Linux/Mac), o comando seria 'clear'
os.system('cls')


# ENTRADA DE DADOS com input
# Aqui o usuário poderia digitar os valores manualmente
# x = int(input('Informe o primeiro número: '))
# y = int(input('Informe o segundo número: '))


# GERAÇÃO DE NÚMEROS ALEATÓRIOS COM A BIBLIOTECA RANDOM
# x recebe um valor entre 10 e 100
# y recebe um valor entre 1 e 9
# Isso simula uma entrada automática de dados
# random possui vários métodos, como randint, uniform, choice, shuffle, etc.
# Estamos usando o randint para gerar um número inteiro aleatório
x = random.randint(10, 100)
y = random.randint(1, 9)

# Exibimos os valores gerados
print(x, y)



# MENU DE OPÇÕES
# Apresentamos as operações disponíveis
print('\n****** MENU DE OPÇÕES: ******')
print('[1] - Somar')
print('[2] - Subtrair')
print('[3] - Multiplicar')
print('[4] - Dividir')

# O usuário escolhe uma opção
opcao = int(input('Escolha uma opção: '))  # ENTRADA


# ESTRUTURA DE DECISÃO
# PROCESSAMENTO
# Dependendo da opção escolhida, chamamos a função correspondente
match opcao:

    case 1:
        # chama a função soma
        resposta = soma(x, y)

    case 2:
        # chama a função subtração
        resposta = subtracao(x, y)

    case 3:
        # chama a função multiplicação
        resposta = multiplica(x, y)

    case 4:
        # chama a função divisão
        resposta = divisao(x, y)

    case _:
        # caso o usuário digite uma opção inválida
        resposta = 'Opção inválida. Tente novamente.'



# SAÍDA DE DADOS
# Exibimos o resultado da operação escolhida

# A variável "resposta" pode ser:
# - Um número (quando a operação foi válida)
# - Um texto (quando a opção foi inválida)

# Caso queira formatar números casas decimais, precisamos garantir que só aplicaremos
#  formatação em valores numéricos.
# Por isso, uma das maneiras é usarmos isinstance para verificar o tipo do dado

# Se em variável resposta houver um número tipo int ou float, entra no if
if isinstance(resposta, (int, float)):
    # Neste caso, é um número, então exibimos normalmente
    print(f'Resultado: {resposta:.2f}')
else:
    # Se for texto, exibimos sem formatação numérica
    print(f'Resultado: {resposta}')



# OBSERVAÇÕES
# As funções foram definidas separadamente para organizar melhor o código.
# O uso do random permite testar o programa sem digitar valores manualmente.
# O match case controla qual operação será executada.
# Caso a opção seja inválida, o programa retorna uma mensagem ao usuário.
# Em programas reais, é importante tratar erros, como divisão por zero.