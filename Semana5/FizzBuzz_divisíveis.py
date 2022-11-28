#o código abaixo é uma função que recebe como parâmetro um número inteiro e
# devolve "Fiz" se o número for divisível por 3 e não for divisível por 5;
# devolve "Buzz" se o número for divisível por 5 e não for divisível por 3;
# devolve "FizzBuzz" se o número for divisível por 3 e por 5;
# caso o número não seja divisível por 3 e também não seja divisível por 5,
# ela deve devolver o número recebido como parâmetro.

def fizzbuzz(x):
    a = x % 3
    b = x % 5

    if (a == 0 and b != 0) :
        return "Fizz"
    if (a != 0 and b == 0) :
        return "Buzz"
    if (a == 0 and b == 0) :
        return "FizzBuzz"
    if (a != 0 and b != 0) :
        return x
    

def test_answer():
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(4) == 4
