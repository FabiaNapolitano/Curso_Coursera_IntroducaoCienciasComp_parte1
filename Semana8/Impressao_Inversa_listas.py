# o código abaixo deve ler uma sequência de números inteiros terminadas por zero
# e imprimir a sequência inversa dos números digitados.

n = 1
lista = []

while n != 0 :

    n = int(input("Digite um número: "))

    lista.append(n)

lista.reverse() #nesta linha o comando reverse inverte os itens da lista

for i in lista:
    if lista[0] == i:
        next
    else:    
        print(i)


