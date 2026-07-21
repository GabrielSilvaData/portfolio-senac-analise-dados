# ======================================
# ####### EXEMPLO - USO DE EXCEPTION (ERRO GENÉRICO)

print('=== Cálculo de Produtividade ===')

# -------------------------------------
# O try tenta executar o código que pode gerar erro
try:
    # ENTRADA DE DADOS
    # Pode gerar erro se o valor digitado não for numérico
    total_produzido = float(input('Valor total da venda: '))

    # Também pode gerar erro de conversão
    funcionarios = int(input('Total de Funcionários: '))    
    
    # PROCESSAMENTO
    # Pode gerar erro se funcionarios for 0 (divisão por zero)
    media_por_funcionario = total_produzido / funcionarios


# -------------------------------------
# EXCEPTION GENÉRICO

# Exception é a "classe base" de praticamente todos os erros em Python
# Isso significa que ele captura vários tipos de erro ao mesmo tempo

# "as e" permite armazenar o erro em uma variável
# Assim conseguimos exibir a mensagem real do erro que ocorreu
except Exception as e:
    print(f'Ops! Erro nos valores de entrada: {e}')


# Tratamento de interrupção pelo usuário (Ctrl + C)
# Esse erro ocorre quando o usuário interrompe manualmente o programa
except KeyboardInterrupt:
    print('Operação cancelada pelo usuário')

# -------------------------------------
# BLOCO ELSE
# Executa somente se NÃO ocorrer erro no try
else:
    print(f'Média por funcinário: {media_por_funcionario:.2f}')

# -------------------------------------
# BLOCO FINALLY
# Sempre executa, com erro ou sem erro
# Usado para garantir uma finalização do programa
finally:
    print('Programa encerrado!')


# -------------------------------------
# Exception captura vários erros de uma vez (forma genérica)
# "as e" permite ver a mensagem detalhada do erro
# É útil para não deixar o programa quebrar

# ATENÇÃO:
# Usar Exception pode esconder o tipo real do erro
# Em muitos casos, é melhor tratar erros específicos (ValueError, ZeroDivisionError, etc.)