# o código abaixo é uma função que recebe um único caracter como parâmetro e
# devolve True se ele for uma vogal e False se for uma consoante.

def vogal(x) :

    vogal = True
    vogais = ["a","e","i","o","u","A","E","I","O","U"]
    cont = len(vogais)
    
    for i in vogais:
        if ( i == x ):
            return  vogal
        else:
            cont -=1
            if (cont == 0) :
                return not vogal


def test_answer():
    assert vogal("a") == True
    assert vogal("e") == True
    assert vogal("i") == True
    assert vogal("o") == True
    assert vogal("u") == True
    assert vogal("A") == True
    assert vogal("E") == True
    assert vogal("I") == True
    assert vogal("O") == True
    assert vogal("U") == True
    assert vogal("p") == False
    
    
