# 080 Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista = []
maior = 0
menor = 0
cont = 1
posicao = 1

for n in range(1, 6):
    num = int(input("Digite um número: "))
    
    if cont == 1:
        maior = num
        menor = num
        lista.append(num)
        print("Adicionado na lista")
    else:
        if num > maior:
            maior = num
            lista.insert(posicao, num)
            print("Adicionado ao final da lista")
        elif num < menor:
            menor = num
            lista.insert(0, num)
            print("Adicionado na posição 0")
        else:
            lista.insert(1, num)
            print("Adicionado na posição 1")

    cont += 1
    posicao +=1

    # Opção 2
    '''
    if c in range(0, 5):
        n = int(input("Digite um valor: "))
        if c ==0 or n > lista[-1]:
            lista.append(n)
            print("Add")
        else:
            pos = 0
            while pos < len(lista):
                if n <= lista[pos]:
                    lista.insert(pos, n)
                    print(f'Add na posção {pos}')
                    break
                pos += 1
    '''
    
print(lista)