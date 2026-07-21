print('Olá mundo!')
print('Gabriel Silva')

# print('Olá mundo!')
# O símbolo # é usado para comentar uma linha.
# Comentários não são executados pelo Python.
# Servem para explicar o código.

# Atalhos úteis no VS Code:
# Ctrl + ;  -> Comenta ou descomenta a linha
# Alt + Shift + ↓ -> Copia as linhas para baixo


# Variáveis (espaços onde guardamos valores). Estes "espaços" podem ser usados mais para frente no código.
# No exemplo abaixo, estamos Criando duas variáveis na memória do computador (nome e idade)
# Ao fazer o uso do sinal de "=", estamos informando para o python, que as variáveis estão Recebendo os valores # que estão à direita do sinal de igual.
# Isto é chamado de Atribuição. No caso da idade: idade = 26, estamos atribuindo o valor 26 para dentro da # variável idade
nome = 'João'   # guardando um texto na variável. Lê-se, nome recebe João
idade = 26      # guardando um número na variável. Lê-se, idade recebe 26

# Mostrando os valores na tela
print(nome)
print(idade)

# Usando f-string para imprimir, textos e variáveis montando uma frases
print(f'Nome: {nome}')
print(f'Idade: {idade}')

# Também podemod usar o f-string para imprimir, textos e mais de uma variável
print(f'Nome: {nome}, Idade: {idade}') 


# Operadores matemáticos
# +  soma
# -  subtração
# *  multiplicação
# /  divisão (resultado com decimal)
# %  resto da divisão
# // divisão inteira (descarta o resto)

# Alterando o valor da variável
nome = 'Pedro'  # agora nome guarda outro valor. O nome João, foi sobreposto "apagado".

# Criando variáveis numéricas
n1 = 5
n2 = 2

# Realizando cálculos e guardando os resultados em outra variável
# Isto também é atribuição. Estamos atribuindo através do "=" os valores das operações em outra variável.
# Realizamos as operações entre n1 e n2 e cada resultado, está sendo guardado em uma variável. 
soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2
modulo = n1 % n2
divisao_inteira = n1 // n2

# Mostrando os resultados
print(f'Soma: {soma}')
print(f'Subtração: {subtracao}')
print(f'Multiplicação: {multiplicacao}')
print(f'Divisão: {divisao}')
print(f'Módulo (resto): {modulo}')
print(f'Divisão Inteira: {divisao_inteira}')

# Mostrando o valor atualizado da variável
# Algumas linhas acima, fizemos a variável nome receber o nome de outra pessoa, que no caso foi o nome Pedro. O # nome João, que estava guardado na variável foi perdido. Neste caso, houve uma sobreposição de valores, onde # # somente o último valor fica armazenado. O nome João foi perdido, somente a partir da linha que foi feita a # # nova atribuição para Pedro. Exemplo: Se o nome Pedro foi atribuido na linha 40, desta linha para frente, a # # variável nome irá guardar o valor de Pedro, porém até a linha 39, a variável nome ainda estaria guardando o # # nome João.

print(nome)

# Usando o resultado em outro cálculo
total = n1 + n2      # primeiro cálculo
total = total + 5    # Acrescentando 5 ao resultado anterior. Isto é o que chamamos de acumulação. Já havia um valor dentro de total e a partir daí, fizemos o total receber + 5.

print(total)

# Primeiro somamos n1 + n2
# Depois pegamos esse resultado e somamos mais 5
# Isso mostra que podemos reutilizar valores guardados em variáveis
