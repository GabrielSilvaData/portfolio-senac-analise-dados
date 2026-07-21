# ======================================
# ####### EXEMPLO - TRY COM MÚLTIPLAS EXCEÇÕES E ELSE
print('=== Cálculo de Produtividade ===')

# -------------------------------------
# BLOCO TRY
# O try tenta executar um conjunto de instruções que podem gerar erro
try:
    # ENTRADA DE DADOS

    # Pode gerar erro se o valor digitado não for numérico
    total_produzido = float(input('Valor total da venda: '))

    # Também pode gerar erro, se não for um número inteiro válido
    funcionarios = int(input('Total de Funcionários: '))    
    
    # PROCESSAMENTO
    # Pode gerar erro se funcionarios for 0 (divisão por zero)
    media_por_funcionario = total_produzido / funcionarios


# -------------------------------------
# TRATAMENTO DE MÚLTIPLAS EXCEÇÕES
# Aqui temos uma forma diferente de tratar erros:
# usamos parênteses para agrupar mais de um tipo de erro no mesmo except

# ValueError => ocorre quando a conversão falha (ex: letras no lugar de números)
# TypeError => ocorre quando há incompatibilidade de tipos
# (menos comum neste exemplo, mas importante conhecer)
except (ValueError, TypeError):
    print('O valor precisa ser numérico')


# Tratamento específico para divisão por zero
except ZeroDivisionError:
    print('Funcionário não pode ser Zero.')


# -------------------------------------
# BLOCO ELSE
# O else no try/except executa somente, se NÃO houver erro no try
# Ou seja, se tudo ocorrer corretamente, este bloco será executado
else:
    print(f'Média por funcinário: {media_por_funcionario:.2f}')


# -------------------------------------
# É possível tratar mais de um erro no mesmo except usando (erro1, erro2)
# O Python verifica os excepts de cima para baixo
# O else é opcional, mas melhora a organização:
# separa claramente o que é "tentativa" (try) do que é "sucesso" (else)

# DIFERENÇA EM RELAÇÃO A OUTROS EXEMPLOS:
# Antes:
# - o print ficava dentro do try

# Agora:
# - o print está no else
# - isso garante que só será executado, se não houver erro