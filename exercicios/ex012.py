# 012 Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input("Qual o preço: R$"))
desconto = float(input("Qual o desconto:"))

result = preco - (preco * desconto / 100)

print("Com o desconto de {:.2f}% o produto que custava R${:.2f}, custará R${:.2f}.".format(desconto, preco, result))