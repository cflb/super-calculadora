""" Caulco da velocidade média em Km/h """

from aritmetica import velocidadeMedia


distancia = int(input("Digite a distância total percorrida (Em Km/h): "))
tempo = int(input("Digite o tempo total gasto para percorrer a disntância em horas: "))

print ("A velocidade média é: ")
print (velocidadeMedia(distancia, tempo))

