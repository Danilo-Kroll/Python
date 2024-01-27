# 014 Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.

c = float(input("Informe a temperatura em ºC: "))

f = (c * 9 / 5) + 32

print("A temperatura de {:.1f}ºC corresponde a {:.1f}ºF!".format(c, f))