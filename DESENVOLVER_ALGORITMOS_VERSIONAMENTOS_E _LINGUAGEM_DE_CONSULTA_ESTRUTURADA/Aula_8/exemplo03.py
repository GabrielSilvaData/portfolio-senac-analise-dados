# ======================================
# ####### EXEMPLO - Função com retorno (return)

# DEFINIÇÃO DA FUNÇÃO
# Esta função recebe dois parâmetros (a e b)
# Diferente do exemplo anterior, aqui NÃO usamos print dentro da função
# A função apenas calcula e devolve o resultado com return
def somar(a, b):
    r = a + b  # realiza o cálculo da soma

    # return devolve o valor calculado para quem chamou a função
    # A função é encerrada neste ponto e o valor de "r" é enviado de volta
    return r




# PROGRAMA PRINCIPAL
# Criamos duas variáveis com valores fixos
n1 = 50
n2 = 25

# CHAMADA DA FUNÇÃO
# Aqui estamos chamando a função somar(n1, n2)
# Por "baixo dos panos", isso equivale a somar(50, 25)
# Ou seja:
# a = 50
# b = 25

# RECEBENDO O RETORNO DA FUNÇÃO
# O valor retornado pela função (75) será armazenado na variável "resposta"
resposta = somar(n1, n2)

# Após a execução:
# 1. A função recebe os valores (50 e 25)
# 2. Calcula a soma  75
# 3. Retorna esse valor com return
# 4. Esse valor é guardado na variável "resposta"

# EXIBIÇÃO DO RESULTADO
# Agora utilizamos o valor retornado fora da função
print(f'O resultado é {resposta}')

# ---------------------------------------------------------------------



# SAÍDA ESPERADA
# O resultado é 75





# ######## OBSERVAÇÃO IMPORTANTE  ######
# Diferente do exemplo anterior:
# - Lá usamos print dentro da função (a função já mostrava o resultado)
# - Aqui usamos return (a função devolve o valor para ser usado depois)
# Isso torna o código mais flexível, pois podemos reutilizar o resultado