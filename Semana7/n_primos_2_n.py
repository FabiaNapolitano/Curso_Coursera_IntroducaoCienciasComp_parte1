# o código é uma função n_primos que recebe como argumento um número inteiro
# maior ou igual a 2 como parâmetro e devolve a quantidade de números primos que
# existem entre 2 e n (incluindo 2 e, se for o caso, n).

def primo(n):
    x = n
    while n % (x - 1) != 0:
            x -= 1
    if x - 1 == 1 :
        return True
    else:
        return False
                

def n_primos(n):
    primos = 0
    while n >= 2 :
        if primo(n):
            primos += 1
        
        n -= 1
    return primos
        
