
# ####### EXEMPLO - Modularização (uso de funções externas)

# IMPORTAÇÃO DAS FUNÇÕES
# Aqui estamos utilizando funções que estão em outro arquivo.
# Isso é chamado de modularização, ou seja, separar o código em partes menores.

# Temos uma pasta chamada "auxiliar" e dentro dela um arquivo "operacoes.py"
# Nesse arquivo estão definidas as funções: dobro, triplo, quadrado e metade

# import:
# - Primeiro informamos o nome da pasta
# - Depois o nome do arquivo (sem .py)
# - Por fim, indicamos quais funções queremos utilizar

# Importando as funções
# Isso permite reutilizar código sem precisar reescrever as funções neste arquivo
from auxiliar.operacoes import dobro, triplo, quadrado, metade


# PROGRAMA PRINCIPAL
# ENTRADA 
# O usuário informa um número inteiro
n = int(input('Informe um número: '))


# EXIBIÇÃO DO MENU
# Mostramos as opções disponíveis para o usuário escolher
print('\n////// MENU DE OPÇÕES //////')
print('[1] - Dobro')
print('[2] - Triplo')
print('[3] - Quadrado')
print('[4] - Metade')

# O usuário escolhe uma das opções
opcao = int(input('Escolha uma opção: '))


# ESTRUTURA DE DECISÃO
# Dependendo da opção escolhida, chamamos uma função diferente
# Obsserve que dentro dos Cases, temos somente as chamadas das funções
# Neste arquivo, não temos as definições de nenhuma das funções. Todas foram
# definidas em outro arquivo
match opcao:

    case 1:
        # Chamada da função dobro, que foi importada do outro arquivo
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
        # Nenhuma função será executada
        resposta = 'Opção Inválida'


# SAÍDA DE DADOS
# Exibimos o resultado final
print(f'Resultado: {resposta}')



# OBSERVAÇÕES
# As funções não estão neste arquivo, mas podem ser utilizadas normalmente após o import.
# Isso evita repetição de código e facilita a organização do projeto.
# Caso o arquivo "operacoes.py" seja alterado, este código já usará a versão atualizada automaticamente.
# Esse tipo de organização é muito comum em projetos maiores.


# ####### IMPORTANDO TODAS AS FUNÇÕES
# Importa o MÓDULO inteiro
# Aqui trazemos todo o arquivo operacoes.py, inclusive variáveis, se houver 
# import auxiliar.operacoes

# Neste import acima, para usar as funções, precisamos informar de onde elas vêm
# Ou seja, usamos o nome do módulo antes da função

# n = 10
# print(auxiliar.operacoes.dobro(n))
# print(auxiliar.operacoes.triplo(n))