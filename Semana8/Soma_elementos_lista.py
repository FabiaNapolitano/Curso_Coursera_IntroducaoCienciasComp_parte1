# o código é uma função soma_elementos que recebe como parâmetro uma lista com
# números inteiros e devolve um número inteiro correspondente à soma dos elementos
# da lista recebida.

def soma_elementos(lista):
    soma = 0
    for i in lista:
        x = int(i)
        soma = soma + x
    return soma

def test_answer():
    assert soma_elementos([2, 4, 2, 2, 3, 3, 1]) == 17
    assert soma_elementos([1, 2, 3, 3, 3, 4]) == 16
