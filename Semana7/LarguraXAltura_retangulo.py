# o código abaixo recebe como entradas dois números inteiros correspondentes a
# largura e à altura de um retângulo. E deve imprimir, usando repetições while
# uma cadeia de caracteres que represente o retângulo informado com caracteres
# '#' na saída.


largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))
x = largura
while altura > 0:
    
    while largura > 0 :
        print("#" ,end = "")
        largura -= 1
    largura = x    
    altura -= 1
    print()    
