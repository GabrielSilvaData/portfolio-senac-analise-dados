# --------------------------------------------------------
###### ATIVIDADE 1
# Enunciado: Verificar se um número é positivo, negativo ou zero.
# O programa deve receber um número informado pelo usuário e usar 
# match/case para classifica-lo em positivo, negativo, ou zero.

num = float(input("Digite um número: "))

# Verifica se o número é positivo, negativo ou zero
match num:
    case num if num > 0:
        print(f"{num} é positivo")
    case num if num < 0:
        print(f"{num} é negativo")
    case 0:
        print(f"{num} Zero é neutro")