# 020 O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alnos.
# Faça m programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

a1 = str(input("1º aluno: "))
a2 = str(input("2º aluno: "))
a3 = str(input("3º aluno: "))
a4 = str(input("4º aluno: "))

lista = [a1, a2, a3, a4]

random.shuffle(lista)

print("A ordem será: {}".format(lista))