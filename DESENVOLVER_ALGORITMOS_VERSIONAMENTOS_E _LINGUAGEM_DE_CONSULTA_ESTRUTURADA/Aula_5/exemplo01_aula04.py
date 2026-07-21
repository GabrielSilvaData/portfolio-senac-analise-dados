
# IFs encadeados (IF com ELIF)
# As condições são exclusivas, ou seja, apenas uma delas será verdadeira 
# e o bloco correspondente será executado.

# Exemplo 1:
# nota >= 7 ---- Aprovado
# nota >= 5 ---- Em recuperação
# nota < 5 ---- Reprovado
nota = 10 
if nota >= 7:
    print("Aluno aprovado")
elif nota >= 5:
    print("Aluno em recuperação")
else:
    print("Aluno reprovado")


# -----------------------------------------------------------
# Exemplo 2:
# IFs simples - (sem ELIF)
# As condições são independentes, ou seja, todas podem ser verdadeiras
# e os blocos correspondentes serão executados.

# Enunciado: Verifique o conceito de um aluno com base na nota.
# nota >= 9 ---- A
# nota >= 7 ---- B
# nota >= 5 ---- C
# nota >= 3 ---- D
# nota < 3 ---- E
nota = 10 
if nota >= 9:
    print("Conceito A")

if nota >= 7:
    print("Conceito B")

if nota >= 5:
    print("Conceito C")

if nota >= 3:
    print("Conceito D")
else:
    print("Conceito E")

# -----------------------------------------------------------



# EXEMPLO 3 
# IFs Aninhados - 
# Um If aninhado é um If dentro de outro If. Podendo ser usado para verificar
# condições mais complexas, onde uma condição do If interno, depende da condição
# do If externo ser verdadeira. Nestes casos, também podemos ter Ifs simples ou 
# encadados.

# Enunciado: Verifique se o aluno foi Aprovado e se teve boa frequência.
# Aprovação por nota: nota >= 7
# Aprovação por frequência: frequência >= 75%
nota = float(input("Digite a média final do aluno: "))
frequencia = float(input("Digite a frequência do aluno (em %): "))

if nota >= 7:
    if frequencia >= 75:
        print("Aluno aprovado com bom desempenho e boa frequência.")
    else:
        print("Aluno com boa nota, mas reprovado por falta.")
else:
    print("Aluno reprovado por nota baixa.")
# -----------------------------------------------------------


