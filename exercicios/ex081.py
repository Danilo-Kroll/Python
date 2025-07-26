# 081 Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

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

lista.sort(reverse=True)        
print(f"Foram digitados: {len(lista)} números")
print(f"Lista em ordem decrescente: {lista}")

if 5 in lista:
    print("O número 5 FOI digitado na lista.")
else:
    print("O número 5 NÃO foi digitado na lista.")