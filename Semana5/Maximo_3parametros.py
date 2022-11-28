# o código abaixo é uma função "maximo" do outro exercício, que devolve o maior
#valor dentre dois inteiros recebidos, para que ela passe a receber 3 valores
# inteiros como parâmetros e devolva o maior dentre eles.

def maximo(x, y, z):
    if (x >= y and x >= z) :
        return x
    if (y >= x and y >= z) :
        return y
    if (z >= x and z >= y) :
        return z



def test_answer():
    assert maximo(30, 14, 10) == 30
    assert maximo(0, -1, 1) == 1
    assert maximo(0, 0, 0) == 0
    assert maximo(0, 2, 2) == 2
    assert maximo(2, 2, 0) == 2
