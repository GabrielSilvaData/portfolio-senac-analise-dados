# valor = float(input("Digite o valor da compra: R$ "))

# if valor > 250:
#     desconto = valor * 0.16
#     valor_final = valor - desconto
#     print(f"Desconto aplicado: R$ {desconto:.2f}")
#     print(f"Valor final: R$ {valor_final:.2f}")
# else:
#     print(f"Valor final (sem desconto): R$ {valor:.2f}")

# valor = float(input("Digite o valor da compra: R$ "))
# pagamento = input("Forma de pagamento (a vista/parcelado): ").lower()

# if valor > 250 and pagamento == "a vista":
#     desconto = valor * 0.16
#     valor_final = valor - desconto
#     print(f"Desconto aplicado: R$ {desconto:.2f}")
#     print(f"Valor final: R$ {valor_final:.2f}")
# else:
#     print(f"Valor final (sem desconto): R$ {valor:.2f}")

# estoque = int(input("Digite a quantidade em estoque: "))
# quantidade = int(input("Digite a quantidade solicitada: "))
# peso = float(input("Digite o peso total do pedido (kg): "))

# if estoque >= quantidade and peso <= 50:
#     print("O pedido pode ser liberado.")
# else:
#     print("O pedido não pode ser enviado. Revise as condições de estoque e transporte.")

tempo = float(input("Digite o tempo de filiação (anos): "))
valor = float(input("Digite o valor movimentado nos últimos 6 meses (R$): "))

if tempo > 3 or valor > 5000:
    print("O cooperado tem direito ao benefício especial.")
else:
    print("O cooperado ainda não atende aos critérios para o benefício.")