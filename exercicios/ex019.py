# 019 Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um progrma que ajude
# ele, lendo o nome deles e escrevendo o nome do escolhido.

import random

a1 = str(input("1º aluno: "))
a2 = str(input("2º aluno: "))
a3 = str(input("3º aluno: "))
a4 = str(input("4º aluno: "))

escolhido = random.choice([a1, a2, a3, a4])

print("O aluno escolhido foi {}.".format(escolhido))

# Opção 2
lista = [a1, a2, a3, a4]
escolhido2 = random.choice(lista)
print("O aluno escolhido foi {}.".format(escolhido2))