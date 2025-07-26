# 079 Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores 
# únicos digitados, em ordem crescente.

lista = []
msg = "Digite um número: "

while True:
    num = int(input(f"{msg}"))
    continuar = str(input("Deseja continuar [S/N]: ")).upper()
    
    # Não add SE já estiver na lista
    if num in lista:
        print("Esse número já está na lista.")    
    else:
        lista.append(num)
   
    if continuar == 'S':
        msg = "Digite outro número: "
    elif continuar == 'N':
        break
    else:
        msg = "Opção inválida! Digite outro número: "
    
    # Opção 2
    '''
    if num not in lista:
        lista.append(num)
    else:
        print("Esse número já está na lista.")
    r = str(input("Quer continuar? [S/N] "))
    if r in 'Nn':
        break
    '''
    
lista.sort(reverse=True)        
print(lista)