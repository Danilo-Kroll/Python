# 013a Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto para
# pagamento à vista e com 4% de aumento para pagamento parcelado.

preco = float(input("Qual o preço: R$"))

vista = preco - (preco * 5 / 100)
parcelado = preco + (preco * 4 / 100)

print("À vista com desconto de 5%: R${:.2f}.".format(vista))
print("Parcelado com aumento de 4%: R${:.2f}.".format(parcelado))

qtdParcela = int(input("Informe o número de parcelas: "))

print("Ficará em {}x de R${:.2f}.".format(qtdParcela, (parcelado / qtdParcela)))