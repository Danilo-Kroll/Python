# 036 Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte
#o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não
# pode exceder 30% do salário ou então o empréstimo será negado.

valorCasa = float(input("Digite o valor da casa: R$"))
salario = float(input("Digite o salário do comprador: R$"))
anos = int(input("Digite em quantos anos deseja pagar: "))

parcela = valorCasa / (anos * 12)
salarioExcede = salario * 0.30

print("Para pagar uma casa de R${:.2f} em {} anos, a parcela será de R${:.2f} por mês.".format(valorCasa, anos, parcela))

if parcela <= salarioExcede:
	print("Empréstimo ACEITO!")
else:
	print("Empréstimo NEGADO!")