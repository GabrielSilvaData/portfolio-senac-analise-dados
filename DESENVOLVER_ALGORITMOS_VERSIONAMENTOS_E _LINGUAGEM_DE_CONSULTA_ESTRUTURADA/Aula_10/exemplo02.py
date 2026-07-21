# ======================================
# ####### EXEMPLO 1 - FOR SEM TRATAMENTO DE ERRO

# Este laço for será executado 5 vezes
for i in range(5):

    # ENTRADA DE DADOS

    # Aqui pode ocorrer erro se o usuário digitar algo que não seja número
    # Exemplo: letras ou símbolos geram ValueError
    total_produzido = float(input('Valor total da venda: '))

    # Aqui também pode ocorrer erro de conversão
    funcionarios = int(input('Total de Funcionários: '))
    
    # PROCESSAMENTO

    # Se o usuário digitar 0 para funcionários,
    # ocorre erro de divisão por zero (ZeroDivisionError)
    media_por_funcionario = total_produzido / funcionarios

    # SAÍDA
    print(f'Média por funcinário: {media_por_funcionario:.2f}')

# IMPORTANTE:
# Se ocorrer qualquer erro durante uma das execuções,
# o programa é interrompido imediatamente.
# As próximas repetições do for NÃO serão executadas.
# -------------------------------------




# ======================================
# ####### EXEMPLO 2 - FOR COM TRY/EXCEPT
# Este laço também será executado 5 vezes
for i in range(5):

    # O try tenta executar o código que pode gerar erro
    try:
        # ENTRADA DE DADOS
        total_produzido = float(input('Valor total da venda: '))
        funcionarios = int(input('Total de Funcionários: '))
        
        # PROCESSAMENTO
        media_por_funcionario = total_produzido / funcionarios

        # SAÍDA
        print(f'Média por funcinário: {media_por_funcionario:.2f}')

    # TRATAMENTO DE ERRO DE CONVERSÃO
    # Ocorre quando o usuário não digita um número válido
    except ValueError:
        print('Informe um número.')

    # TRATAMENTO DE DIVISÃO POR ZERO
    # Ocorre quando funcionarios recebe valor 0
    except ZeroDivisionError:
        print('Funcionário não pode ser Zero.')

# IMPORTANTE:
# Mesmo que ocorra erro em uma das repetições,
# o laço continua executando normalmente.
# O erro é tratado e o programa segue para a próxima iteração.