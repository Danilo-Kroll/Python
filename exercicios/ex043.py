# 043 Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal
# (IMC) e mostre seu status, de acordo com a tabela abaixo:
# - IMC abaixo de 18,5: Abaixo do Peso
# - Entre 18,5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida

peso = float(input("Peso: "))
altura = float(input("Altura: "))

imc = peso / (altura ** 2)

if imc < 18.5:
	print("IMC {:.2f}. Abaixo do peso!".format(imc))
elif imc < 25:
	print("IMC {:.2f}. Peso ideal!".format(imc))
elif imc < 30:
	print("IMC {:.2f}. Sobrepeso!".format(imc))	
elif imc < 40:
	print("IMC {:.2f}. Obesidade!".format(imc))	
else:
	print("IMC {:.2f}. Obesidade mórbida!".format(imc))