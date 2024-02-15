# 053 Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input("Digite uma frase: ")).upper().strip().replace(' ', '')

inverso = ''

for f in range(len(frase) - 1, -1, -1):
	inverso += frase[f]
if inverso == frase:
	print("Palíndromo {} x {}".format(frase, inverso))
else:
	print("Diferente {} x {}".format(frase, inverso))

# Opção 2
inverso2 = frase[::-1]

if inverso2 == frase:
	print("Palíndromo {} x {}".format(frase, inverso2))
else:
	print("Diferente {} x {}".format(frase, inverso2))