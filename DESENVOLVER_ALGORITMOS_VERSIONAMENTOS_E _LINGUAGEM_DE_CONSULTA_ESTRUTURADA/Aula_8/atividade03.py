# ======================================
# ####### EXEMPLO - Uso de função com CONSTANTES

# DEFINIÇÃO DA FUNÇÃO
# Esta função recebe o valor excedente de peso excedente (e) e calcula o 
# valor da multa com base em uma constante
def calcula_multa(e):
    # MULTA_VALOR é uma CONSTANTE definida fora da função
    # Mesmo estando fora, ela pode ser utilizada aqui (escopo global)
    multa = e * MULTA_VALOR

    # retorna o valor calculado
    return multa




# PROGRAMA PRINCIPAL
# CONSTANTES
# Constantes são valores que NÃO devem ser alterados durante a execução
# Por convenção, escrevemos constantes em letras MAIÚSCULAS
MULTA_VALOR = 5.0   # valor da multa por quilo excedente
LIMITE = 100        # limite máximo permitido de peso



# ENTRADA DE DADOS
# O usuário informa o peso pescado
# input() retorna texto, então usamos float() para permitir casas decimais
peso_pescado = float(input('Peso: '))

# Verificamos se o peso ultrapassa o limite permitido
if peso_pescado > LIMITE:

    # cálculo do excedente
    # representa quanto ultrapassou o limite
    excedente = peso_pescado - LIMITE

    # CHAMADA DA FUNÇÃO
    # enviamos o excedente para a função calcular a multa e retirna um valor
    vl_multa = calcula_multa(excedente)

    # SAÍDA
    print(f'Valor da Multa R$ {vl_multa}')

else:
    # caso não ultrapasse o limite, não há multa
    print(f'Peso {peso_pescado}. Sem Multa!')

# ---------------------------------------------------------------------





# OBSERVAÇÕES IMPORTANTES

# 1. CONSTANTES:
#    MULTA_VALOR e LIMITE são valores fixos do sistema.
#    Eles representam regras do problema (valor da multa e limite permitido).
#    Por isso, não devem ser alterados durante a execução.

# 2. USO DE CONSTANTES NA FUNÇÃO:
#    A função calcula_multa(e) utiliza MULTA_VALOR mesmo sem receber esse valor por parâmetro.
#    Isso acontece porque a constante está no escopo global.
#    Não consiguimos acessar as variáveis que foram definidas dentro de uma função.

# 3. ORGANIZAÇÃO:
#    - A função cuida apenas do cálculo da multa
#    - O programa principal cuida da entrada, decisão e saída

# 4. BOA PRÁTICA:
#    Usar constantes evita "números mágicos" espalhados no código,
#    facilitando manutenção e entendimento.
#    Se o limite de peso ou a multa for alterado pelo governo, é só mudar o valor da constante.