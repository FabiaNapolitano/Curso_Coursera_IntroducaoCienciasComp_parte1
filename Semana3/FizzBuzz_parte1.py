#Este código identifica se um número inteiro digitado é divisível por 3

a = int(input("Digite um número inteiro: "))

div = a % 3

if (div == 0):
    print("Fizz")
else:
    print(a)
    
