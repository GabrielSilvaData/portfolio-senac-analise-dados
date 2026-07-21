# Peso IMC

def calcula_imc(p,a):
    i = p / (a**2)
    return i

def verifica_classificacao(imc):
   match imc:
        case imc if imc < 17:
         classificacao = 'Muito abaixo'
        case imc if imc < 18.5:
         classificacao = 'Abaixo do peso'
        case imc if imc < 25:
         classificacao = 'Peso normal'
        case imc if imc < 30:
         classificacao = 'Acima do peso'
        case imc if  imc < 35:
         classificacao = 'Obesidade grau 1'
        case imc if imc < 40:
         classificacao = 'Obesidade grau 2'
        case _:
         classificacao = 'Obesidade grau 3'


qtd = int(input('Informe a qtd de pessoas:'))
for i in range(qtd):
    print(f'\nPessoa{i+i}')
    peso = float(input('Informe o peso:'))
    altura = float(input('Informe a altura:'))


    imc = calcula_imc(peso,altura)
    #print(imc)

    resposta = verifica_classificacao(imc)

    
         
    # Saida 
    print(30*"=")
    print('Resultado')
    print(f'IMC: {imc:.2f}')
    print(f'Classificacao:{resposta}')

         
         










