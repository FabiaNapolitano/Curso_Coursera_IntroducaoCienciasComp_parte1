# Este código faz a leitura de 4 pontos cardiais e calcula a distância entre eles

# d(x,y) = Raiz²((x1 - x2)² + (y1 - y2)²

import math

x1 = float(input("Digite o ponto x1 do plano cartesiano: "))
y1 = float(input("Digite o ponto y1 do plano cartesiano: "))
x2 = float(input("Digite o ponto x2 do plano cartesiano: "))
y2 = float(input("Digite o ponto y2 do plano cartesiano: "))


dist = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

if (dist >= 10):
    print ("longe")
else:
    print ("perto")
