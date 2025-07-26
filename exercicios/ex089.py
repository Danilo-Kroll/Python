# 089 Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas
# de cada aluno individualmente.

lista = list()
dado = list()

while True:
    nome = dado.append(str(input('Digite um nome: ')))
    n1 = dado.append(float(input('Nota 1: ')))
    n2 = dado.append(float(input('Nota 2: ') ))

    lista.append(dado[:])
    dado.clear()

    continuar = str(input('Deseja continuar [S/N]? '))
    if continuar in 'Nn':
        break

print(lista)

print('='*30)
print('BOLETIM')
print('='*30)

ordem = 1
n = len(lista)
c = 0

# Transformar em tabela
while n > 0:
    print(f'{ordem}: {lista[c][0]},  Média: {(lista[c][1] + lista[c][2]) / 2}')

    ordem += 1
    n -= 1
    c += 1

print('='*30)

aluno = int(input("Qual aluno deseja vizualizar as notas: ")) - 1

print(f'{aluno + 1}: {lista[aluno][0]} = Nota 1: {lista[aluno][1]} = Nota 1: {lista[aluno][2]}') 

# avaliar professor