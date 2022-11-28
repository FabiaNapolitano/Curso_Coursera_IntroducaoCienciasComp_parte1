# Este código faz a leitura de dois números inteiros como parâmetro e
# devolve o maior deles. Ex: maximo(3,4) 4; maximo(0,-1) 0

def maximo(x, y):
    if x > y:
        return x
    else:
        return y


def test_answer():
    assert maximo(3, 4) == 4
    assert maximo(0, -1) == 0
    
