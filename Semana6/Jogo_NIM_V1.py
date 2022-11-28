def campeonato():
    rodada = 1
    while (rodada <= 3) :
        print("\n**** Rodada", rodada, "****")
        rodada += 1
        partida()


def usuario_escolhe_jogada(n, m) :
    retirada = int(input("\nQuantas peças você vai tirar? "))
    while (retirada > m or retirada <= 0 ):
        print("\nOops! Jogada inválida! Tente de novo.")
        retirada = int(input("\nQuantas peças você vai tirar? "))
    if (retirada == 1) :
        print("\nVocê tirou uma peça.")
    else:
        print("Você tirou", retirada, "peças.")
    
    return retirada


def computador_escolhe_jogada(n, m):
    
    estrategia_PC = n % (m + 1)
    if (estrategia_PC == 0) :
        print("O computador tirou", m, "peças.")
        return m
    else:
        if (estrategia_PC == 1) :
            print("O computador tirou uma peça!")
        else:
            print("O computador tirou", estrategia_PC, "peças.")
        return estrategia_PC


def partida():
    n = int(input("\nQuantas peças? "))
    while (n <= 0):
        print("\nOops! Jogada inválida! Tente de novo.")
        n = int(input("\nQuantas peças? "))
        
    m = int(input("Limite de peças por jogada? "))

    while (n <= m) :
        print("\nOops! Jogada inválida! Tente de novo.")
        m = int(input("Limite de peças por jogada? "))
       
    estrategia = n % (m + 1)

    if (estrategia == 0) :
        print("\nVocê começa!")
        while ( n != 0) :
            retirada = usuario_escolhe_jogada(n, m)
            
            n = n - retirada
            
            if (n == 1):
                print("Agora resta apenas uma peça no tabuleiro.\n")
            else:
                print("Agora restam", n, "peças no tabuleiro.\n")
                
            retirada_PC = computador_escolhe_jogada(n, m)           

            n = n - retirada_PC
            
            if (n >= m):                    
                print("Agora restam", n,"peças no tabuleiro.")
            else:
                print("Fim do jogo! O computador ganhou!")
                return
    else:
        print("\nComputador começa!\n")
        while (n != 0) :
            retirada_PC = computador_escolhe_jogada(n, m)

            n = n - retirada_PC
            
            if (n > m) :
                print("Agora restam", n, "peças no tabuleiro.")
            else:
                print("Fim do jogo! O computador ganhou!")
                return
            retirada = usuario_escolhe_jogada(n, m)

            n = n - retirada

            if (n == 1):
                print("Agora resta apenas uma peça no tabuleiro.\n")
            else:
                print("Agora restam", n, "peças no tabuleiro.\n")                
        
        
print("Bem vindo ao jogo do NIM! Escolha:")
#print("\n1 - para jogar uma partida isolada")
escolha = int(input("\n1 - para jogar uma partida isolada\n2 - para jogar um campeonato "))

if (escolha == 1 ):
    print("\nVoce escolheu uma partida isolada!")
    partida()    
else:
    print("\nVoce escolheu um campeonato!")
    campeonato()
    print("\n**** Final do campeonato! ****")
    print("\nPlacar: Você 0 x 3 Computador")        



                
            
