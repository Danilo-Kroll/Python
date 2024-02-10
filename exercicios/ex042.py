# 042 Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será
# formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes

reta1 = int(input("Reta 1: "))
reta2 = int(input("Reta 2: "))
reta3 = int(input("Reta 3: "))

if reta1 < reta2 + reta3 and reta2 < reta3 + reta1 and reta3 < reta2 + reta1:
	print("Podem formar um triângulo!")
	if reta1 == reta2 == reta3:
		print("É um triângulo EQUILÁTERO!")
	elif reta1 != reta2 != reta3 != reta1:
		print("É um triângulo ESCALENO!")
	else:
		print("É um triângulo ISÓSCELES!")
else:
	print("Não formam um triângulo!")