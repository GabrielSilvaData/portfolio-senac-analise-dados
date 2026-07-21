# ======================================
# ####### EXEMPLO - MÉDIA DE NOTAS COM TRY/EXCEPT

# FUNÇÃO
# Recebe uma lista de notas, soma todos os valores e calcula a média
# len(lista_notas) retorna a quantidade de elementos da lista
def calcula_media(lista_notas):
    tot = sum(lista_notas)             # soma todas as notas
    med = tot / len(lista_notas)       # calcula a média
    return tot, med                   # retorna dois valores


# -------------------------------------
# PROGRAMA PRINCIPAL

contador = 1  # controla a numeração dos alunos

# while True cria um loop contínuo
# o programa só será encerrado quando encontrarmos o break
while True:
    print(f'Aluno {contador}')
    
    # ENTRADA DE DADOS
    # Nome não precisa de conversão, pois é texto
    aluno = input('Nome do aluno: ')
    
    # Lista para armazenar as 4 notas
    notas = []

    # -------------------------------------
    # BLOCO TRY
    # Tentamos executar a entrada das notas
    try:
        # for garante que sempre serão solicitadas 4 notas
        for i in range(4):
            # Pode gerar ValueError se o usuário digitar texto
            nota = float(input('Informe a nota: '))
            notas.append(nota)  # adiciona a nota na lista

    # -------------------------------------
    # BLOCO EXCEPT
    # Executa se houver erro na conversão para float
    except ValueError:
        print('Erro: Informe apenas valores válidos!')

    # -------------------------------------
    # BLOCO ELSE
    # Executa somente se NÃO houver erro no try
    else:
        # Chamada da função passando a lista de notas
        # Esperameos que a função retorne dois valores: o total e a média
        total, media = calcula_media(notas)
    
        print('\nRESULTADO')
        print(f'Aluno: {aluno}')
        print(f'Total de Pontos: {total}')
        print(f'Média: {media:.2f}')

    # -------------------------------------
    # BLOCO FINALLY
    # Sempre executa, independente de erro ou não
    finally:
        print(f'Processo encerrado para o aluno {contador}')  



    # -------------------------------------
    # CONTROLE DE REPETIÇÃO
    # Pergunta se o usuário deseja continuar
    opcao = input('Deseja calcular para outro aluno? ').strip().upper()

    # Se a resposta for diferente de 'S', encerra o loop
    if opcao != 'S':
        break

    # Incrementa o contador para o próximo aluno
    # O loopretorna ao início
    contador += 1


print('\nPrograma Encerrado!')