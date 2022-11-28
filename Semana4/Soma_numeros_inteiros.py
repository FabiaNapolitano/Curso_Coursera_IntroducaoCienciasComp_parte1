# Este codigo faz a leiura de um número inteiro e calcula a soma destes
# Ex: 123 = 1 + 2 + 3 = 6

# Abaixo tem duas soluções diferentes para o mesmo desafio

num = int(input("Digite um número inteiro: "))
 

string = str(num)
inteiro = 0

for i in string:
    i = int(i)
    inteiro = i + inteiro

print(inteiro)

#print ("****** SEGUNDA SOLUÇÃO *******")

##soma = 0
##result = 0
##
##while num > 0 :
##    
##    resto = num % 10
##    inteiro = num // 10
##    num = inteiro
##    soma = soma + resto
##
##print(soma)
