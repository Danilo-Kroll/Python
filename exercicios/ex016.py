# 016 Crie um progrma que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

import math

num = float(input("Digite um valor: "))

print("Sua porção inteira é {}.".format(math.floor(num)))
print("Sua porção inteira é {}.".format(math.trunc(num)))

# Opção 2 -> sem pacote
print("Sua porção inteira é {}.".format(int(num)))


# Opção 3 -> indicando a biblioteca
from math import trunc

num2 = float(input("Digite um valor: "))

print("Sua porção inteira é {}.".format(trunc(num2)))