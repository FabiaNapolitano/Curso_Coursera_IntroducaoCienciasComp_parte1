#Este código identifica se um número inteiro digitado é divisível por 3 e 5

a = int(input("Digite um número inteiro: "))

div3 = a % 3
div5 = a % 5

if (div3 == 0 and div5 == 0):
    print("FizzBuzz")
else:
    print(a)
