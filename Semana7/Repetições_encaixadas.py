# aprendendo melhor repetições encaixadas

##coluna = 1
##linha = 1
##
##while (linha <= 10):
##    while (coluna <= 10):
##        print(linha * coluna, end = "\t") #end indica o tipo de separação por linha
##        coluna += 1
##    linha += 1
##    print()
##    coluna = 1
##
##
##tab = 1
##while tab <= 10:
##    print("Tabuada do", tab, ":", end = "\t")
##    i = 1
##    while i <= 10:
##        print(tab*i, end = "\t")
##        i += 1
##    print()
##    tab += 1

##fora = 5
##n = 1
##while fora > 0:
##    dentro = 0    
##    while dentro < fora:
##        print(n)
##        n += 1
##        dentro += 1
##    fora -= 1


tab = 1
i = 1
while tab <= 10 and i <= 10:
    print(tab, "x", i, "=", tab*i)
    i += 1
    tab += 1
print()

tab = 0
while tab < 10:
    tab += 1
    i = 0
    while i < 10:
        i += 1
        print(tab,"x",i,"=", tab*i)
    print()
