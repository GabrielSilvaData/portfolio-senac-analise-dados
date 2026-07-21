# ======================================
# ####### EXEMPLO - CAIXA ELETRÔNICO COM TRY/EXCEPT

print('CAIXA ELETRÔNICO')

# O try tenta executar a entrada de dados que pode gerar erro
try:
    # Definição do saldo inicial
    saldo = 1000

    # Pode gerar ValueError se o usuário digitar algo que não seja número
    saque = float(input('Informe o valor do saque: '))


# EXCEPTS:
# Erro de conversão (ex: letras no lugar de números)
except ValueError:
    print('Valor inválido')

# Interrupção manual (Ctrl + C)
except KeyboardInterrupt:
    print('Programa encerrado pelo usuário')


# BLOCO ELSE
# Executa somente se NÃO houver erro no try
else:
    # Verifica se o valor do saque é maior que o saldo disponível
    if saque > saldo:
        print('Saldo Insuficiente')

    # Verifica se o valor informado é inválido (zero ou negativo)
    # Aqui é importante garantir que o saque seja maior que zero
    elif saque < 2:
        print('Saque precisa ser a partir de R$ 2,00')

    else:
        # Se passou por todas as validações, realiza o saque
        saldo -= saque

        print('\nSaque realizado com sucesso')
        print(f'Saldo em conta R$ {saldo:.2f}')


# FINALLY
# Sempre executa, com erro ou sem erro
finally:
    print('Operação finalizada!')

print('\nPrograma Encerrado')  # Fim


# ======================================
# Nesta correção, consideramos que o valor para o saque é a partir de R$ 2,00, 
# por conta da menor cédula em REAL
# Não dá para sacar R$ 0,00 ou R$ 1,00 ou 1,01 ou -1,00 ou -1,01
# Se fosse considerar a partir de R$ 5,00, bastaria substituir o 2 por 5