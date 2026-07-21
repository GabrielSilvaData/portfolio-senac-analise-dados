# ======================================
# ####### EXEMPLO - Funções com menu de opções

# DEFINIÇÃO DAS FUNÇÕES
# Cada função foi criada para realizar um único cálculo específico.
# Essa separação facilita a organização e reutilização do código.

def dobro(x):
    # Recebe um valor e retorna o dobro
    return x * 2


def triplo(x):
    # Recebe um valor e retorna o triplo
    return x * 3


def quadrado(x):
    # Recebe um valor e retorna o quadrado (x * x)
    return x * x


def metade(x):
    # Recebe um valor e retorna a metade
    return x / 2



# PROGRAMA PRINCIPAL
# ENTRADA
# O usuário informa um número inteiro
# input() retorna texto, por isso usamos int() para converter
n = int(input('Informe um número: '))


# EXIBIÇÃO DO MENU
# Apresentamos as opções disponíveis para o usuário escolher
print('\n////// MENU DE OPÇÕES //////')
print('[1] - Dobro')
print('[2] - Triplo')
print('[3] - Quadrado')
print('[4] - Metade')

# O usuário escolhe uma das opções
opcao = int(input('Escolha uma opção: '))  # Entrada


# PROCESSAMENTO
# ESTRUTURA DE DECISÃO (match case)
# Dependendo da opção escolhida, uma função diferente será chamada
match opcao:

    case 1:
        # Chamada da função dobro
        # O valor de n é enviado para o parâmetro x
        resposta = dobro(n)

    case 2:
        # Chamada da função triplo
        resposta = triplo(n)

    case 3:
        # Chamada da função quadrado
        resposta = quadrado(n)

    case 4:
        # Chamada da função metade
        resposta = metade(n)

    case _:
        # Caso o usuário digite uma opção inválida
        # Não chamamos nenhuma função
        resposta = 'Opção Inválida'



# SAÍDA DE DADOS 
# Neste trecho, a variável "resposta" pode ter dois tipos de conteúdo:
# - Um número (quando o usuário escolhe uma opção válida do menu)
# - Um texto (quando o usuário digita uma opção inválida)
# Como queremos trabalhar com formatação de números (ex: duas casas decimais),
# precisamos tomar cuidado: a formatação {:.2f} só funciona com valores numéricos.
# Por isso, usamos o if para verificar, se a resposta NÃO é a mensagem de erro "Opção Inválida".
# Ou seja, se for um valor válido (número), apenas exibimos o resultado normalmente.
# Caso seja a mensagem 'Opção Inválida', sabemos que é uma String "texto",
# então exibimos normalmente, sem tentar aplicar formatação numérica, pois isso daria um erro no terminal.
if resposta != 'Opção Inválida':
    print(f'Resultado: {resposta}')
else:
    print(f'Resultado: {resposta}')



# OBSERVAÇÕES
# As funções foram definidas no início e são chamadas conforme a escolha do usuário.
# Cada função possui uma única responsabilidade (um cálculo específico).
# O match case permite controlar o fluxo do programa de forma organizada.
# O uso de funções evita repetição de código e facilita manutenção.