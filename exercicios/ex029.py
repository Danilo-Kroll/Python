# 029 Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem
# dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input("Digite a velocidade: "))

multa = (velocidade - 80) * 7

if velocidade > 80:
	print("Você ultrapassou a velocidade máxima de {}Km/h! Sua multa é de R${:.2f}.".format(velocidade, multa))
else:
	print("Velocidade de {}Km/h está dentro do permitido.".format(velocidade))