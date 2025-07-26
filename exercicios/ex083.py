# 083 Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo
# deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

exp = str(input("Digite a expressão: "))
cont1 = 0
cont2 = 0

listaExp = []
for palavra in exp:
    listaExp.append(list(palavra))
    if palavra == "(":
        cont1 += 1
    if palavra == ")":
        cont2 += 1

print(listaExp)
print(cont1)
print(cont2)

if cont1 == 0 and cont2 == 0:
    print("Não possui parênteses.")
elif cont1 % 2 == 0 and cont2 % 2 == 0:
    print("Expressão CORRETA!")
else:
    print("Expressão INCORRETA!")