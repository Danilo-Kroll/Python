# 015 Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de
# dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e
# R$0,15 por km rodado.

dia = int(input("Total de dias alugados? "))
km = float(input("Total de km rodados? "))

valorDia = dia * 60
valorKm = km * 0.15

print("Valor total pelos dias alugados: R${:.2f}.".format(valorDia))
print("Valor total pelos km rodados: R${:.2f}.".format(valorKm))
print("Valor total a pagar: R${:.2f}.".format(valorDia + valorKm))