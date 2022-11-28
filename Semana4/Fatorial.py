# Este codigo faz a leitura de um número informado pelo usuário e retorna o
# seu valor fatorial Ex: 5! = 5 * 4 * 3 * 2 * 1 = 120 EX: 0! = 1

num = int(input("Digite o valor de n: "))

n = num
contador = num
fat = 0

if (num == 0 or num == 1) :
    print("1")
else:
    
    while (contador <= num and contador > 1) :

        fat = n * (contador-1)
        n = fat
        contador -= 1
    
    print(fat)
