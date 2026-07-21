# ATIVIDADE 1 - Notas de 10 alunos (Versão 2 FOR)

# Algoritmo Recebe 4 notas e calcula a média para cada um dos 10 alunos
# As nostas são informadas pelo usuários.
# repete o bloco para 10 alunos
for aluno in range(10):  
    print(f"\n---- Aluno {aluno + 1} ----")     # mostra o número do aluno (1 a 10)
    soma_notas = 0      # inicializa a soma das notas para o aluno atual

    for nota in range(4):   # repete o bloco para 4 notas
        valor_nota = float(input(f"Digite a nota {nota + 1}: "))    # recebe a nota do usuário
        soma_notas += valor_nota        # acumula a soma das notas

    media_final = soma_notas / 4     # calcula a média final
    print(f"A média final do aluno {aluno + 1} é: {media_final:.2f}")  # exibe a média com 2 casas decimais
# =============================================================


# ATIVIDADE 1 VERSÃO 2 - Usando 4 variáveis e apenas 1 FOR
for aluno in range(3):      # repete o bloco para 10 alunos
    print(f"\n---- Aluno {aluno + 1} ----")     # mostra o número do aluno (1 a 10)
    soma_notas = 0      # inicializa a soma das notas para o aluno atual

    n1 = float(input(f"Digite a nota Nota 1: ")) # recebe as notas do usuário
    n2 = float(input(f"Digite a nota Nota 2: "))
    n3 = float(input(f"Digite a nota Nota 3: "))
    n4 = float(input(f"Digite a nota Nota 4: "))
    
    media_final = (n1 + n2 + n3 + n4) / 4  # acumula a soma das notas

    print(f"A média final do aluno {aluno + 1} é: {media_final:.2f}")  # exibe a média com 2 casas decimais

# -------------------------------------------------------------------------------------------------------------
