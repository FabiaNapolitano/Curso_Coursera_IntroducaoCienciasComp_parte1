# O código abaixo faz a leitura de uma sequência de números digitados pelo usuário
# e, para cada número digitado, informar o seu fatorial.

import string

a = list(string.ascii_lowercase)
print(a)

alfabeto = []
c = 0
for i in range(ord('A'), ord('Z')+1):
    alfabeto.insert(c, chr(i))
    c += 1

print(alfabeto)


n = 1

while n > 0:

    n = input("Digite um número inteiro positivo: ")
    if (n == "0") :
        break
    while n in alfabeto or n in a :
        print("Inválido!")
        n = input("Digite um número inteiro positivo: ")
        if (n == "0") :
            break
        
    n = int(n)
    fat = n
    x = int(n)

    while ( n != 1 ):        
        fat = fat * (n-1)
        n -= 1
    print("Fatorial de", x , " = ", fat)
    
    
