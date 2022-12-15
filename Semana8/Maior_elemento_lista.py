# o código abaixo é uma função maior_elemento que recebe como parâmetro uma lista
# com números inteiros e devolve um número inteiro correspondente ao maior valor
# presente na lista recebida.

def maior_elemento(lista):
    return max(lista)


def test_answer():
    assert maior_elemento([3,2,8,1,0,5,9]) == 9
    assert maior_elemento([-1,0-8,100]) == 100
