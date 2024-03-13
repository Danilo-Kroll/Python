# 071 Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário
# qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor
# serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print("="*10)
print("BANCO KROLL")
print("="*10)

valor = int(input("Qual valor deseja sacar? R$"))
total = valor
notas = 0
ced = 50

while True:
	if total >= ced:
		total -= ced
		notas += 1
	else:
		if notas > 0:
			print(f"Total de {notas} cédulas de R${ced}")
		if ced == 50:
			ced = 20
		elif ced == 20:
			ced = 10
		elif ced == 10:
			ced = 1
		notas = 0
		if total == 0:
			break