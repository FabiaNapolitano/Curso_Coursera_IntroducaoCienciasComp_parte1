#Este código recebe um número intero e imprime se este número é par ou ímpar.


a = int(input("Digite um número inteiro: "))

par = a % 2

if (par == 0):
    print("par")
else:
    print("ímpar")
