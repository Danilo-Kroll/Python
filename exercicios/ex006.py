# 006 Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

num = int(input("Digite um número: "))

dobro = num * 2
triplo = num * 3
raiz = num ** (1/2)
# raiz: função pow(num, (1/2))

print("O dobro de",num,"é",dobro)
print("O trilpo de",num,"é",triplo)
print("A raiz de",num,"é",raiz)