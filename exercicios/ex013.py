# 013 Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input("Informe o salário: R$"))
aumento = float(input("Informe o % de aumento: "))

result = salario + (salario * aumento / 100)

print("Com um aumento de {:.2f}%, seu salário que era de R${:.2f} passará para R${:.2f}.".format(aumento, salario, result))