#Este código identifica se os números digitados estão em ordem crescente

a = int(input("Digite um número inteiro: "))
b = int(input("Digite um número inteiro: "))
c = int(input("Digite um número inteiro: "))

if (a < b and b < c):
    print("crescente")
else:
    print("não está em ordem crescente")
    

