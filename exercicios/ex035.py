# 035 Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem
# ou não formar um triângulo.

reta1 = int(input("Reta 1: "))
reta2 = int(input("Reta 2: "))
reta3 = int(input("Reta 3: "))

if reta1 < reta2 + reta3 and reta2 < reta3 + reta1 and reta3 < reta2 + reta1:
	print("Podem formar um triângulo!")
else:
	print("Não formam um triângulo!")