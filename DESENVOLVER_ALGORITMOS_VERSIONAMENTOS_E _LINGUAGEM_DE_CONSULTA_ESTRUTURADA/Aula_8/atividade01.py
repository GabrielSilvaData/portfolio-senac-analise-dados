# ------------------------
# DEFINIÇÃO DA FUNÇÃO
# Neste momento estamos criando a função.
# A função fica armazenada na memória do programa e só será executada quando for chamada.

def quadrado(n):
    # n é o parâmetro da função.
    # Ele receberá o valor enviado na chamada da função.

    # Aqui realizamos o cálculo do quadrado
    # Multiplicamos o número por ele mesmo
    q = n * n  

    # return devolve o resultado para quem chamou a função
    # Após o return, a função é finalizada
    return q


# ------------------------
# DEFINIÇÃO DA FUNÇÃO
# Outra função com a mesma estrutura, mas com outro objetivo

def dobro(n):
    # Recebe um valor e calcula o dobro
    d = n * 2  

    # Retorna o resultado para o programa principal
    return d  


# ------------------------
# PROGRAMA PRINCIPAL

# ENTRADA DE DADOS
# O usuário informa um número
# input() retorna texto, então usamos int() para converter para número inteiro
numero = int(input('Digite um número: '))


# CHAMADA DA FUNÇÃO (quadrado)
# O valor da variável "numero" é enviado para o parâmetro "n"

# Exemplo:
# Se numero = 6, então a chamada será equivalente a quadrado(6)
# A função executa o cálculo e retorna o resultado
# Esse valor retornado é armazenado na variável "res_quadrado"
res_quadrado = quadrado(numero)


# CHAMADA DA FUNÇÃO (dobro)
# Novamente enviamos o valor da variável "numero" para a função

# Agora o cálculo será diferente, pois a função dobro multiplica por 2
# O valor retornado será armazenado na variável "res_dobro"
res_dobro = dobro(numero)


# SAÍDA DE DADOS
# Agora exibimos todas as informações calculadas
print('\nRESULTADO:')
print(f'Número digitado: {numero}')
print(f'Quadrado: {res_quadrado}')
print(f'Dobro: {res_dobro}')


# ------------------------
# OBSERVAÇÕES IMPORTANTES

# 1. As funções foram definidas no início, mas só executaram quando foram chamadas.
# 2. O mesmo valor (numero) foi utilizado em duas funções diferentes.
# 3. Cada função tem uma responsabilidade específica:
#    - quadrado calcula n * n
#    - dobro calcula n * 2
# 4. O uso do return permite guardar o resultado em variáveis e utilizá-lo depois.