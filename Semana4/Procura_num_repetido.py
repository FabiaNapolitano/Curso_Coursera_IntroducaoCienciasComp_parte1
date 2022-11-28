# O codigo abaixo recebe um número inteiro na entrada e verifica se o número
# recebido possui ao menos um dígito com um dígito adjacente igual a ele.
# Caso exista, imprima "sim"; se não existir, imprima "não".

n = int(input("Digite um número inteiro: "))

cont = 0
x = ""
string = str (n)
y = len(string)

while cont == 0 :

    for i in string :

        if x == i :
            if (cont == 1):
                next
            else:
                print("sim")
                cont = 1
            
        else:
            x = i
            y -= 1        
        
            if (y == 0):
                cont = 1
            

if ( y == 0 ) :
    print("não")    
else:
    next
