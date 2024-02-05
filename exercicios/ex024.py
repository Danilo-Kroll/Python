# 024 Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cidade = str(input("Digite o nome de uma cidade: ")).upper().strip()

dividido = cidade.split()

print("Essa cidade possui SANTO no nome? {}".format(('SANTO' in dividido[0])))

# Opção 2
print(cidade[:5].upper() == 'SANTO')