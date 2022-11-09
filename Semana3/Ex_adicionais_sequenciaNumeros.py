n = (input("Digite a sequência de n > 0: "))

cont_par = 0
cont_impar = 0

for i in n:
    
    if (i == " " or i == ","):
        next
        
    else:
        inteiro = int(i)
        par = (inteiro % 2)
        
        if (par == 0):
            cont_par += 1           
            
        else:
            cont_impar += 1       
    

print ("Números pares:", cont_par)
print ("Números ímpares:",cont_impar)
