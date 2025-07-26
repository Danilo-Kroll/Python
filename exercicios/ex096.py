# 096 Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno
# retangular (largura e comprimento) e mostre a área do terreno.

def area(a, l):
    r = a * l
    print(f'A área de um terreno de {a}x{l} é de {r}m².')


print("Controle de Terrenos")
print('-'*30)

a = float(input("Largura (m): "))
b = float(input("Altura (m): "))

area(a, b)