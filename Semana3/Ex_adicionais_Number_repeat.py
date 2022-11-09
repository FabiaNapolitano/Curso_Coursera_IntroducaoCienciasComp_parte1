# O código abaixo faz a leitura de um número n > 0 e um número d >=0 e d <=9
# o número d representa o número que deve ser encontrado repetido dentro de n

n = (input("Digite o valor de n (n > 0): "))
inteiron = int(n)
while inteiron < 0 :
    n = (input("Digite o valor de n (n > 0): "))
    inteiron = int(n)

d = (input("\nDigite o valor de d (0<=d<=9): "))
inteirod = int(d)
while inteirod < 0 or inteirod >9 :    
    d = (input("Digite o valor de d (0<=d<=9): "))
    inteirod = int(d)

inteiro = int(n)
repeat = 0
copian = ""
if (inteiro == 0):
    print ("O dígito", d,"ocorre", repeat,"vezes em", n)
    
else:
    
    avanco = 0
    for i in n:
        inteiro = int(i)
        
        if inteiro == 0 and avanco == 0: 
            next
            
        else:
            
            if inteiro >= 0 :
                avanco += 1  
                copian = copian + i
                
                if inteiro >= 0:    
                    if (i == d):
                        repeat += 1
                        
                        
                    else:
                        next

    print ("\nO dígito", d,"ocorre", repeat,"vezes em", copian)
