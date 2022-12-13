# o código abaixo deve ler uma sequência de números inteiros terminadas por zero
# e imprimir a sequência inversa dos números digitados.

n = 1
lista = []

while n != 0 :

    n = int(input("Digite uma sequência de número terminada por zero: "))

    lista.append(n)

indice = len(lista)
lista_inversa = []
while indice > 0 :
    lista_inversa.append(lista[indice - 1])
    indice -= 1

print(lista_inversa)
