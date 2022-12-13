# o código abaixo é um jogo simples chamado NIM. Nesse jogo, n peças são inicial-
# mente dispostas numa mesa ou tabuleiro. Dois jogadores jogam alternadamente,
# retirando pelo menos 1 e no máximo m peças cada um. Quem tirar as últimas
# peças possíveis ganha o jogo. Existe uma estratégia para ganhar o jogo que é
# muito simples: ela consiste em deixar sempre múltiplos de (m+1) peças ao
# jogador oponente.
# OBJETIVO: o programa permite a uma "vítima" jogar o NIM com o computador. O
# computador é claro, deverá seguir a estratégia vencedora descrita acima.

# função de campeonato do jogo com 3 rodadas

def campeonato():
    rodada = 1
    while (rodada <= 3):
        print("\n**** Rodada", rodada, "****")
        rodada += 1
        partida()
        

def partida(): # função que inicia a partida do jogo
    
    n = int(input("\nQuantas peças? "))
    m = int(input("Limite de peças por jogada? "))
                
    estrategia = n % (m+1)
    
    if (estrategia == 0) : # o código deve chamar a função partida para os dois casos
        print("\nVoce começa!")
        while (n != 0) :
            n = usuario_escolhe_jogada(n, m)
            # alterar daqui pra frente!!!!!!
            if (n == 1):
                print("Agora resta apenas uma peça no tabuleiro.\n")
                computador_escolhe_jogada(n, m)
            else:
                print("Agora restam", n,"peças no tabuleiro.\n")
                computador_escolhe_jogada(n, m)   
         
    else:
        print("\nComputador começa!\n")
        n = computador_escolhe_jogada(n, m)
        
        if (n >= m):                    
            print("Agora restam", n,"peças no tabuleiro.")
            usuario_escolhe_jogada(n, m) 
            
    return print("Fim do jogo! O computador ganhou!")
    
        


def computador_escolhe_jogada(n, m): # função para jogada do computador
    estrategia_PC = n % (m+1)
    if (estrategia_PC == 1) :
        print("O computador tirou uma peça.")
    else:
        print("O computador tirou", estrategia_PC, "peças.")

    n = n - estrategia_PC
    return n



def usuario_escolhe_jogada(n, m): # funçao para jogada do usuário
       
    retirada = int(input("\nQuantas peças você vai tirar? "))
    while (retirada > m) :
        print("\nOops! Jogada inválida! Tente de novo.")
        retirada = int(input("\nQuantas peças você vai tirar? \n"))
        print()
        
##    if (retirada == 1):
##        print("Você tirou uma peça")
##        
##    else:
##        print("Você tirou", retirada,"peças.")

   # n = n - retirada
    
##    if (n == 1):
##        print("Agora resta apenas uma peça no tabuleiro.\n")
##    else:
##        print("Agora restam", n,"peças no tabuleiro.\n")
##        
    return retirada



# programa inicia por aqui chamando as funções de acordo com a escolha

print("Bem vindo ao jogo do NIM! Escolha:")
print("\n1 - para jogar uma partida isolada")
escolha = int(input("2 - para jogar um campeonato "))

if (escolha == 1 ):
    print("\nVoce escolheu uma partida isolada!")
    partida()
else:
    print("\nVoce escolheu um campeonato!")
##    rodada = 1
##    while (rodada <= 3):
##        print("\n**** Rodada", rodada, "****")
##        rodada += 1
##        partida()
    campeonato()
    print("\n**** Final do campeonato! ****")
    print("\nPlacar: Você 0 x 3 Computador")







