# ATIVIDADE 1

# Informe o código da região
codigo = int(input("Informe o código da região: "))

# Verifica a região correspondente ao código
match codigo:
    case 1:
        print('Sul')
    case 2:
        print('Norte')
    case 3:
        print('Leste')
    case 4:
        print('Oeste')
    case num if num == 5 or num == 6:
        print('Nordeste')
    case 7 | 8 | 9:
        print('Sudeste')
    case 10:
        print('Centro-Oeste')
    case _:
        print('Prouduto Importado')

# ----------------------------------------------------------------