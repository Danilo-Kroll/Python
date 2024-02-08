# 037 Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário
# escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input("Digite um número inteiro: "))

print("""Você deseja que ele seja convertido para
[1] - Binário
[2] - Octal
[3] - Hexadecimal""")

tipo = int(input("Opção: "))

bi = bin(num)
oc = oct(num)
he = hex(num)

if tipo == 1:
	print("Binário: {}.".format(bi))
elif tipo == 2:
	print("Binário: {}.".format(oc))
elif tipo == 3:
	print("Binário: {}.".format(he))
else:
	print("Inválido!")