# Este código faz a leitura de uma sequência de números digitados pelo usuário
# e identifica dentre eles quais são pares e quais são ímpares.

import string

n = [input("\nDigite a sequência de n > 0 separando com espaços: ")]

lista_Aux = []
cont_par = 0
cont_impar = 0
contador = 0
t = 0
x = " "

for i in n[contador]:
    
    if (i != "0" and i != '1' and i != "2" and i != "3" and i != "4" and i != "5" and i != "6" and i != "7" and i != "8" and i != "9" and i != " "):
        next
    else:
        
        lista_Aux.append(i)    
        contador += 1
        
        if (i == " " ):        
            del lista_Aux[contador -1]
            contador -= 1          
            x = i    
            
        else:      
               
            if (x != " " and i != " " ):            
                del lista_Aux[contador -1]            
                contador -= 1
                del lista_Aux[contador -1]            
                contador -= 1
                lista_Aux.append(x+i)            
                contador+= 1  
                
            else:            
                x = i
                
for i in lista_Aux :
    
    inteiro = int(i)
    par = (inteiro % 2) 
    if (par == 0):
        cont_par += 1           
        
    else:
        cont_impar += 1
        
print("\nCaracteres diferentes de números inteiros foram EXCLUÍDOS.")    
print ("Números pares:", cont_par)
print ("Números ímpares:",cont_impar)


