# O código abaixo é uma funçao remove_repetidos que recebe como parâmetro uma
# lista com números inteiros, verifica se tal lista possui elementos repetidos
# e os remove. A função deve devolver uma lista correspondente à primeira lista
# sem elementos repetidos. A lista devolvida deve estar ordenada.
# Dica: pode usar lista.sort()"altera" ou sorted(lista) "ñ altera".





def remove_repetidos(lista):

    lista1 = []
    
    for i in lista:
        if i in lista1:
            next
        else:
            lista1.append(i)        
            
    return (sorted(lista1))
    

def test_answer():
    assert remove_repetidos([2, 4, 2, 2, 3, 3, 1]) == [1, 2, 3, 4]
    assert remove_repetidos([1, 2, 3, 3, 3, 4]) == [1, 2, 3, 4]
    
