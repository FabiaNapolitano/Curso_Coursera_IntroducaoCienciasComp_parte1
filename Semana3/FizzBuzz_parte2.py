#Este código identifica se um número inteiro digitado é divisível por 5

a = int(input("Digite um número inteiro: "))

div = a % 5

if (div == 0):
    print("Buzz")
else:
    print(a)
