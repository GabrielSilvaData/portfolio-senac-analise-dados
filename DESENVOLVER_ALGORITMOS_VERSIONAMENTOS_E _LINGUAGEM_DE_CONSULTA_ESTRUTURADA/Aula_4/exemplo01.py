# Estrutura If
idade = int(input('Insira a idade: '))

if idade >= 18:
    print('Você é Adulto')
else:
    print('Você não é adulto')
# --------------------------------------
    

pontos = int(input('Informe os pontos: '))
if pontos >= 100:
    print('Excelente!')
elif pontos >= 50:
    print('Bom desempenho')
elif pontos >= 25:
    print('Satisfatório')
else:
    print('Pratique mais...')

# -------------------------------------
pontos = int(input('Informe os pontos: '))
if pontos < 25:
    print('Pratique mais...')
elif pontos < 50:
    print('Satisfatório')
elif pontos < 100:
    print('Bom desempenho')
else:
    print('Excelente')

# Operadores AND e OR
usuario = input('Nome: ').lower()
senha = input('Senha: ')

if usuario == "admin" and senha == "1234":
    print('Login realizado com sucesso')
else:
    print('Usuário ou senha incorretos')


# Exemplo IFs Encadado
nota = 3
if nota >= 9:
    print('A')
elif nota >= 7:
    print('B')
elif nota >= 5:
    print('C')
elif nota >= 3:
    print('D')
else:
    print('E')


# Exemplo IFs Não Encadeado
nota = 10
if nota >= 9:
    print('A')

if nota >= 7:
    print('B')

if nota >= 5:
    print('C')

if nota >= 3:
    print('D')
else:
    print('E')


# Ifs aninhados
nota = float(input('Insira a nota: '))
frequencia = float(input('Informe a frequência: '))

if nota >= 7:
    # Aprovado por nota, mas precisa checar a frequência
    if frequencia >= 75:
        print('Aluno aprovado por Nota e Frequência')
    else:
        print('Reprovado por freqência baixa')
else:
    print('Reprovado por nota baixa. ')
    