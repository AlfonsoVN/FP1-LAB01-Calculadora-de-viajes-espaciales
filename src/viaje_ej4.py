distancia_marte = 225000000

for velocidad in range(10000, 50001, 10000):
    tiempo_horas = distancia_marte / velocidad 
    tiempo_dias = (tiempo_horas // 24)
    print(f"Velocidad: {velocidad} Tiempo: {tiempo_dias} días en llegar.")

