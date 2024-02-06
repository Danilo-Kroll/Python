# 031 Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

km = float(input("Informe a distância (km): "))

if km <= 200:
	print("Será cobrado o valor de R$0,50 por km. O valor da viagem será R${:.2f}".format(km * 0.50))
else:
	print("Será cobrado o valor de R$0,45 por km. O valor da viagem será R${:.2f}".format(km * 0.45))

# Opção 2
if km <= 200:
	preco = km * 0.50
else:
	preco = km * 0.45

print("O valor da viagem será R${:.2f}".format(preco))
