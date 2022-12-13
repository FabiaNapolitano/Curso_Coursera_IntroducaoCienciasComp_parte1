# o código abaixo recebe como entradas dois números inteiros correspondentes a
# largura e à altura de um retângulo. E deve imprimir, usando repetições while
# uma cadeia de caracteres que represente o retângulo informado com caracteres
# '#' na saída. PS: Aqui o retângulo não pode ser preenchido com '#' somente bordas.


largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))
x = largura
y = altura

while altura > 0:
    
    while largura > 0 :
        if largura == x :
            print("#", end = "")
        else:
            if altura == y :
                print("#", end = "")
            else:
                if altura == 1 :
                    print("#", end = "")
                else:
                    if largura == 1:
                        print("#")
                    else:
                        print(end = " ")
                
                
        largura -= 1

    if largura == 0 and altura == y:
        print()
        
    largura = x    
    altura -= 1
        
