# 040 Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
# de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))

media = (nota1 + nota2) / 2

if media < 5:
	print("Média {:.2f}. REPROVADO!".format(media))
elif media < 7:
	print("Média {:.2f}. RECUPERAÇÃO!".format(media))
else:
	print("Média {:.2f}. APROVADO!".format(media))