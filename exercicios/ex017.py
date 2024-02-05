# 017 Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo 
# retângulo, calcule e mostre o comprimento da hipotenusa.

import math

co = float(input("Informe o catego oposto: "))
ca = float(input("Informe o catego adjacente: "))

print(math.sqrt(co*co + ca*ca))

print(math.hypot(co, ca))

# Opção 2 -> sem pacote
h = (co**2 + ca**2) ** (1/2)

print(h)