# 025 Crie um progrma que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input("Digite seu nome completo: ")).upper().strip()

print("Esse nome possui SILVA? {}".format(('SILVA' in nome)))