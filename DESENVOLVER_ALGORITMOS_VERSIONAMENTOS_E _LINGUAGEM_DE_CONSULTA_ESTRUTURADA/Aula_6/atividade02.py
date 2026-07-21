# Atividade 02
# Crie um Algoritmo que recebe valores de vendas (não sabemos quantos) e calcule 
# o desconto de 10% para vendas acima de R$ 1000,00.
# O programa deve parar quando a resposta for N.

c = 0
resposta = 'S'
while resposta != 'N':
    c += 1
    valor = float(input(f'Digite o valor da {c}º venda: '))
    if valor > 1000:
        desconto = valor * 0.1
        valor -= desconto
    print(f'O valor da {c}º venda é: {valor}')

    resposta = input('Deseja continuar? [S/N] ').upper()
