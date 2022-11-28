# Este codigo faz a leiura de um número que indica a quantidade de números
# ímpares que será impresso. Ex: n = 5 => 1 3 5 7 9

num = int(input("Digite o valor de n: "))

teste = 0
n = 1
while (num > 0) :
    teste = n % 2
    
    if (teste != 0) :
        print(n)
        num -= 1
        n += 1
    else:
        n += 1
