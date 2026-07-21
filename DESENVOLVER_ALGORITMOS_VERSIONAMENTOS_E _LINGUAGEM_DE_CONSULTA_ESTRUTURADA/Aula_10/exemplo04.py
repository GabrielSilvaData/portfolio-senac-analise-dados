# ======================================
# ####### EXEMPLO - TRY COM MÚLTIPLAS EXCEÇÕES, ELSE E FINALLY
print('=== Cálculo de Produtividade ===')

# -------------------------------------
# BLOCO TRY
# O try tenta executar o código que pode gerar erros
try:
    # ENTRADA DE DADOS

    # Pode gerar ValueError, se o usuário digitar texto
    total_produzido = float(input('Valor total da venda: '))

    # Pode gerar ValueError ou TypeError dependendo da entrada
    funcionarios = int(input('Total de Funcionários: '))    
    
    # PROCESSAMENTO
    # Pode gerar ZeroDivisionError se funcionarios for 0
    media_por_funcionario = total_produzido / funcionarios


# -------------------------------------
# TRATAMENTO DE EXCEÇÕES
# Agrupamento de exceções
# Aqui tratamos mais de um tipo de erro no mesmo bloco
# ValueError - erro de conversão (ex: letras no lugar de números)
# TypeError - erro de tipo incompatível
except (ValueError, TypeError):
    print('O valor precisa ser numérico')


# Tratamento de divisão por zero
except ZeroDivisionError:
    print('Funcionário não pode ser Zero.')


# Tratamento de interrupção pelo usuário (Ctrl + C)
# Esse erro ocorre quando o usuário interrompe manualmente o programa
except KeyboardInterrupt:
    print('Operação cancelada pelo usuário')


# -------------------------------------
# BLOCO ELSE
# O else executa apenas, se NÃO ocorrer erro no try
# Isso evita misturar código de sucesso com código que pode falhar
else:
    print(f'Média por funcinário: {media_por_funcionario:.2f}')


# -------------------------------------
# BLOCO FINALLY
# O finally sempre será executado, independente de, se der erro ou não
# É utilizado quando queremos garantir uma ação final no programa
finally:
    print('Programa encerrado!')


# -------------------------------------
# Podemos agrupar exceções usando parênteses: except (erro1, erro2), para uma mesma tratativa
# Também podemos ter vários blocos except em sequência para tratar erros específicos
# O else executa apenas quando não há erro
# O finally executa sempre, sendo útil para instruções que necessitam ser executadas de qualquer forma,
# quwer tenha dado erro ou não