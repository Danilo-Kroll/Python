# 007 Desenvolva um progrma que leia as duas notas de um aluno, calcule e mostre a sua média.

n1 = float(input("1ª nota: "))
n2 = float(input("1ª nota: "))
media = (n1 + n2) / 2

print("Sua média é: {}".format(media))

# Opção 2 - {:.1f} = uma casa decimal
print("Sua média entre {:.1f} e {:.1f} é {:.1f}".format(n1, n2, media))