# 067 Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado
# pelo usuário. O programa será interrompido quando o número solicitado for negativo. 

while True:
	n = int(input("Escolha a tabuada: "))
	if n >= 0:
		print("-" * 10)
		print(f"{n} x 1 = {n*1}")
		print(f"{n} x 2 = {n*2}")
		print(f"{n} x 3 = {n*3}")
		print(f"{n} x 4 = {n*4}")
		print(f"{n} x 5 = {n*5}")
		print(f"{n} x 6 = {n*6}")
		print(f"{n} x 7 = {n*7}")
		print(f"{n} x 8 = {n*8}")
		print(f"{n} x 9 = {n*9}")
		print(f"{n} x 10 = {n*10}")
		print("-" * 10)
	else:
		break
print("FIM!")

# Opção 2
	''' no lugar de vários prints
	for c in range(1, 11):
		print(f'{n} x {c} = {n*c}')
	'''