nave = 150000
c = 0
distancia = int(input("¿Distancia que vas a recorrer?"))

while distancia > nave :
    distancia = distancia - nave
    c += 1
    print(distancia)

print(f"Parada {c}")

 

