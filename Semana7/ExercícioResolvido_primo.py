# o código abaixo faz a leitura de um número inteiro e retorna se ele é um primo


def éPrimo(n):
    fator = 2
    if x == 2:
        return True
    while n % fator != 0 and fator <= n/2:
        fator = fator +1
    if n % fator == 0:
        return False
    else:
        return True


n = int(input("Digite um número inteiro: "))

while n > 0:
    if éPrimo(n):
        print(n, "é primo!")
    else:
        print(n, "não é primo!")
    n = int(input("Digite um número inteiro: "))


