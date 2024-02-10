# 044 Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal
# e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros

valor = float(input("Preço do produto: R$"))

print("""Condição de Pagamento:
[1] À vista dinherio/cheque: 10% de desconto
[2] À vista no cartão: 5% de desconto
[3] Em até 2x no cartão: Preço normal
[4] 3x ou mais no cartão: 20% de juros""")

condicao = int(input("Opção: "))

if condicao == 1:
	print("[1] À vista dinherio/cheque: 10% de desconto:")
	print("R${:.2f}.".format(valor - (valor * 0.10)))
elif condicao == 2:
	print("[2] À vista no cartão: 5% de desconto:")
	print("R${:.2f}.".format(valor - (valor * 0.05)))
elif condicao == 3:
	print("[3] Em até 2x no cartão: Preço normal:")
	print("R${:.2f}.".format(valor))
	print("2x de R${:.2f}.".format(valor / 2))
elif condicao == 4:
	parcela = int(input("Quantas parcelas? "))
	print("[4] 3x ou mais no cartão: 20% de juros:")
	print("R${:.2f}.".format(valor + (valor * 0.20)))
	print("{}x de R${:.2f}.".format(parcela, (valor + (valor * 0.20)) / parcela))
else:
	print("Condição INVÁLIDA. Tente novamente!")