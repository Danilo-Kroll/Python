# 051 Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10
# primeiros termos dessa progressão.

p = int(input("Primeiro termo: "))
r = int(input("Razão aritimética: "))
f = p + (10 - 1) * r

for n in range(p, f + r, r):
	print(n)