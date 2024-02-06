# 033 Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

num1 = int(input("Número 1: "))
num2 = int(input("Número 2: "))
num3 = int(input("Número 3: "))

if num1 < num2 and num1 < num3:
	menor = num1
if num2 < num1 and num2 < num3:
	menor = num2
if num3 < num1 and num3 < num2:
	menor = num1


if num1 > num2 and num1 > num3:
	maior = num1
if num2 > num1 and num2 > num3:
	maior = num2
if num3 > num1 and num3 > num2:
	maior = num1

print("O menor número é {}.".format(menor))
print("O maior número é {}.".format(maior))