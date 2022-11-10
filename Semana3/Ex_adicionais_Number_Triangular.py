# O código abaixo verifica se o número informado pelo usuário é triangular
# lembrando que um número triangular é o produto de 3 números inteiros.
# EX: 4 * 5 * 6 = 120 então 120 é um número triangular.
# Para escrever o código é usada a fórmula triangular que diz :
# um número x é triangular, se e somente se, n = 8*x +1 for um quadrado. De modo
# equivalente, se a raiz triangular positiva n = (Raiz²(8x+1)-1)/2 for um número
# inteiro.

import math
x = int(input("Digite um número triangular: "))

n = math.pow(8*x+1, 1/2)
n = (n - 1) % 2

if n > 0 :    
    print("O número", x,"NÃO é triangular.\n")
    
else:
    print("O número", x,"é triangular.\n")


print("*****ABAIXO SEGUE A LISTA DOS 100 PRIMEIROS NÚMEROS TRIANGULARES*****")
x = 0
linha = 0
while (linha < 100) :

    n = math.pow(8*x+1, 1/2)
    n = (n - 1) % 2

    if n > 0:
        x += 1 

    else:
        linha += 1
        print(linha, "-",x)
        x += 1
       
