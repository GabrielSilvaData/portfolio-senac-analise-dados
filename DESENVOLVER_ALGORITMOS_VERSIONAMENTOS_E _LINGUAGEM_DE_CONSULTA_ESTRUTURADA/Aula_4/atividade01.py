valor = float(input('Informe o valor: '))

if valor > 250:
    # desconto = valor * 0.16
    valor_novo = valor - valor * 0.16
    print(f'O total a pagar {valor_novo}')
else:
    print(f'Sem desconto. Valor a pagar: {valor}')
