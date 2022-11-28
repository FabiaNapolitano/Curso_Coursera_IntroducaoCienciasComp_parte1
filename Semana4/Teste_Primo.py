# Este código recebe um número inteiro positivo na entrada e verifica se é primo.

n = int(input("Digite um número inteiro: "))

if ( n == 1 or n == 0) :
    print("não primo")

else:
    
    contador = n
    teste = 0

    while (contador > 0) :
        primo = n % contador
        contador -= 1
        
        if (primo == 0) :
            teste += 1
            
    if (teste > 2) :
        contador = 0
        print("não primo")
        
    else:
        print("primo")
        
contadorp = 1
sequencia = 1
Asequencia = 0
print ("**** ABAIXO A LISTA DOS 100 PRIMEIROS NÚMEROS PRIMOS ****\n")

while (sequencia < 102) :
      
    if ( sequencia < 3 ) :
        if ( sequencia == 1 ):
            sequencia += 1
            contadorp += 1

        else:
            Asequencia += 1
            print (Asequencia, "  - PRIMO: ", contadorp)
            contadorp += 1
            sequencia += 1
    else:

        x = contadorp -1
        teste = contadorp % x
        
        while ( ( teste != 0 ) and ( x != 1 )):
            x -= 1 
            teste = contadorp % (x)

            if ( x != 1 and teste == 0 ):
                contadorp += 1

            else:
                
                if ( x == 1 ) :
                    if sequencia > 1 :
                        Asequencia += 1
                        
                    print (Asequencia, "  - PRIMO: ", contadorp)
                    sequencia += 1
                    contadorp += 1
                
            
        
