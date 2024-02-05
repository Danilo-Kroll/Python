# 018 Faça um programa que leia um ângulo e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

angulo = float(input("Informe o ângulo: "))

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print("O seno é {:.2f}".format(seno))
print("O seno é {:.2f}".format(cosseno))
print("O seno é {:.2f}".format(tangente))