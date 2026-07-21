
# EXIBIÇÃO DE TÍTULO
print('=== Cálculo de Produtividade ===')

# -------------------------------------
# BLOCO TRY
# O try é utilizado para "tentar" executar um bloco de código
# que pode gerar erro durante a execução do programa.
# Isso é comum quando trabalhamos com entrada de dados do usuário,
# pois não temos controle sobre o que será digitado.

try:
    # ENTRADA DE DADOS

    # Pode gerar ValueError se o usuário digitar texto
    # Exemplo: "abc" não pode ser convertido para float
    total_produzido = float(input('Valor total da venda: '))

    # Pode gerar ValueError se não for número inteiro
    funcionarios = int(input('Total de Funcionários: '))
    
    # PROCESSAMENTO
    # Pode gerar ZeroDivisionError se funcionarios for 0
    # pois não existe divisão por zero em matemática
    media_por_funcionario = total_produzido / funcionarios

    # SAÍDA
    print(f'Média por funcinário: {media_por_funcionario:.2f}')


# -------------------------------------
# BLOCO EXCEPT - TRATAMENTO DE ERROS
# Este bloco trata erro de conversão de dados
# Ocorre quando o usuário digita algo que não é número
except ValueError:
    print('Erro: informe apenas valores numéricos.')


# Este bloco trata divisão por zero
# Ocorre quando funcionarios = 0
except ZeroDivisionError:
    print('Erro: o número de funcionários não pode ser zero.')



# Sem o try/except, o programa seria interrompido com erro,
# exibindo uma mensagem técnica, q talvez o usuário, não entenda

# Com o tratamento:
# o programa continua rodando
# mostramos uma mensagem amigável
# evitamos quebra do sistema


# "O try tenta executar, o except trata o erro."