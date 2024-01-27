# 009 Faça um progrma que leia um número inteiro qualquer e mostre na tela a sua tabuada.

num = int(input("Digite um número para ver sua tabuada: "))

print(
	"-------------------\n",
	num,"x  1 = ",num*1, "\n",
	num,"x  2 = ",num*2, "\n",
	num,"x  3 = ",num*2, "\n",
	num,"x  4 = ",num*3, "\n",
	num,"x  5 = ",num*4, "\n",
	num,"x  6 = ",num*6, "\n",
	num,"x  7 = ",num*7, "\n",
	num,"x  8 = ",num*8, "\n",
	num,"x  9 = ",num*9, "\n",
	num,"x 10 = ",num*10, "\n",
	"-------------------"
	)

# Opção 2
print("-" * 12)
print("{} x {:2} = {}".format(num, 1, num*1))
print("{} x {:2} = {}".format(num, 2, num*2))
print("{} x {:2} = {}".format(num, 3, num*3))
print("{} x {:2} = {}".format(num, 4, num*4))
print("{} x {:2} = {}".format(num, 5, num*5))
print("{} x {:2} = {}".format(num, 6, num*6))
print("{} x {:2} = {}".format(num, 7, num*7))
print("{} x {:2} = {}".format(num, 8, num*8))
print("{} x {:2} = {}".format(num, 9, num*9))
print("{} x {:2} = {}".format(num, 10, num*10))
print("-" * 12)