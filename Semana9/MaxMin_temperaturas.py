# dada uma lista de temperaturas de um mês, informar qual a maior e a menor
# temperatura.

def minima(temperaturas):
    minima = float(temperaturas[0])
    for i in temperaturas:
        i = float(i)
        if i < minima:
            minima = float(i)
        else:
            next
    return minima        



def maxima(temperaturas):
    maxima = float(temperaturas[0])
    for i in temperaturas:
        i = float(i)
        if i > maxima:
            maxima = float(i)
        else:
            next
    return maxima




def MinMax(temperaturas):
    print("A menor temperatura do mês foi:", minima(temperaturas),"ºC")
    #outra solução mais simples já oferecida pelo python com listas é min():
    print("A menor temperatura do mês foi:", min(temperaturas),"ºC")
    
    print("A maior temperatura do mês foi:", maxima(temperaturas),"ºC")
    #outra solução mais simples já oferecida pelo python com listas é max():
    print("A maior temperatura do mês foi:", max(temperaturas),"ºC")
    return





temperaturas_mes = [12.5, 6, 24, 32]

temperaturas = MinMax(temperaturas_mes)

def test_answer():
    assert maxima([12.5, 6, 24, 32]) == 32
    assert maxima([36, 6, 24, 32]) == 36
    assert maxima([22.3,22.5,21.6,20.2,17.5,16.7,16.2,17.2,18.6,19.8,20.1,21.6]) == 22.5
    assert minima([22.3,22.5,21.6,20.2,17.5,16.7,16.2,17.2,18.6,19.8,20.1,21.6]) == 16.2


