# 010 Crie um programa que leia quanto dinheiro uma pessa tem na carteira e mostre quantos Dólares
# ele pode comprar.

real = float(input("Quantos reais você tem: R$"))
dolar = float(input("Qual o valor do dolar: U$"))

result = real / dolar

print("Voê pode comprar U${:.2f}".format(result))