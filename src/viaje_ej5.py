respuesta = "s"
while respuesta == "s":
    distancia_km = int(input("Distancia:"))  # distancia Tierra - Luna
    velocidad_kmh = int(input("Velocidad:"))

    tiempo_horas = distancia_km // velocidad_kmh
    tiempo_dias = tiempo_horas // 24
    print(f"Tardarías {tiempo_dias} días en llegar.")
    
    respuesta = input("¿Quieres seguir?")
    if respuesta == "n":
        exit()
    else:
        print("vale")        


