valor = float(input('Informe o valor: '))
forma_pagamento = input('Forma de Pagamento: ').lower()

if valor > 250 and forma_pagamento == 'à vista':
    # desconto = valor * 0.16
    valor_novo = valor - valor * 0.16
    print(f'O total a pagar {valor_novo}')
else:
    print(f'Sem desconto. Valor a pagar: {valor}')
