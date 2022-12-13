# (DIFÍCIL) Soma das hipotenusas
# Dizemos que um número é hipotenusa de um triângulo se exites um triângulo
# retângulo com lados inteiros cuja hipotenusa é igual a esse número. Em outras
# palavras, h é uma hipotenusa se existem números inteiros i e j tais que:
# h² = i² + j²
# Abaixo o código deve ter uma função soma_hipotenusas que receba como parâmetro
# um número inteiro positivo n e devolva a soma de todos os inteiros entre1 e n
# que são comprimento da hipotenusa de algum triângulo retângulo com catetos
# inteiros.
# Dica 1: um mesmo número pode ser hipotenusa de vários triângulos, mas deve ser
# somado apenas uma vez. Uma boa solução para este exercício é fazer um laço de
# 1 até n testando se o número é hipotenusa de algum triângulo e somando em caso
# afirmativo.
# Dica 2: primeiro faça a função é_hipotenusa que diz se um número inteiro é o
# comprimento da hipotenusa de um triângulo com lados de comprimento inteiro/não.


def é_hipotenusa(n):
    i = 1
    j = 1
    while j <= n :        
        while i <= n :            
           if n**2 == (i**2) + (j**2):
               return True
           else:
               i += 1
        j += 1
        i = 1
    return False


def soma_hipotenusas(n):
    soma_hipotenusas = 0
    while n > 1 :
        if é_hipotenusa(n) :
            soma_hipotenusas += n
            n -= 1
        else:
            n -= 1
    return soma_hipotenusas
                     
