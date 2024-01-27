# 005 Faça um progrma que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

num = int(input("Digite um número: "))

antes = num - 1
depois = num + 1

print("O número antecessor é", antes, "e o sucessor é", depois)

# Opção 2
print("O número antecessor é {} e o sucessor é {}".format(antes, depois))

# Opção 3
print("O número antecessor é {} e o sucessor é {}".format((num-1), (num+1))