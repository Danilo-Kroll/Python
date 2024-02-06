# 034 Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o
# aumento é de 15%.

salario = float(input("Informe seu salário: "))

if salario > 1250:
	print("Aumento de 10%. Seu salário passará para R${:.2f}".format(salario + (salario * 0.10)))
else:
	print("Aumento de 15%. Seu salário passará para R${:.2f}".format(salario + (salario * 0.15)))

# Opção 2
if salario > 1250:
	novo = salario + (salario * 0.10)
else:
	novo = salario + (salario * 0.15)

print("Seu salário passará para R${:.2f}".format(novo))