# o código abaixo recebe um número inteiro maior ou igual a 2 como parâmetro e
# devolve o maior número primo menor ou igual ao número passado à função.

def maior_primo(x):
    
    if ( x == 1 or x == 0 or x == 2) :
        return x

    else:        
        
        contador = x  
        maior_primo = 0
        
        while x >= 2 :
            while (contador > 1) :
                if (contador == 0) :
                    x -=1
                    
                primo = x % (contador-1)
                if (primo != 0) :
                    contador -= 1
                else:
                    if (contador == 2) :
                        if (maior_primo > 0 and x > 2):
                            x = 0
                            contador = 0
                            return maior_primo
                        maior_primo = x
                        x -= 1
                        contador = x
                    else:
                        x -=1
                        contador = x
                        if (maior_primo > 0 and x == 2):
                            return maior_primo
                        else:
                            next
                

def test_asnwer():
    assert maior_primo(100) == 97
    assert maior_primo(7) == 7
    assert maior_primo(5) == 5
    assert maior_primo(13) == 13
    assert maior_primo(15) == 13
    
                
       
