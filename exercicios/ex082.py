# 082 Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas
# extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final,
# mostre o conteúdo das três listas geradas.

lista = []
msg = "Digite um número: "

while True:
    num = int(input(f"{msg}"))
    continuar = str(input("Deseja continuar [S/N]: ")).upper()
    lista.append(num)
    if continuar == 'S':
        msg = "Digite outro número: "
    elif continuar == 'N':
        break
    else:
        msg = "Opção inválida! Digite outro número: "

# Separar lista
listaPar = []
listaImpar = []

for n in lista:
    if n % 2 == 0:
        listaPar.append(n)
    else:
        listaImpar.append(n)

print(f"Lista completa: {lista}")
print(f"Lista de números PARES: {listaPar}")
print(f"Lista de números ÍMPARES: {listaImpar}")