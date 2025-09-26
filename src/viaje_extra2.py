distancia_marte = 225000000

for velocidad in range(10000, 50001, 10000):
    tiempo_horas = distancia_marte / velocidad 
    tiempo_semanas = (tiempo_horas // 24) // 7
    resto= tiempo_semanas % 7
    print(f"Velocidad: {velocidad} Tiempo: {tiempo_semanas} y {resto}días en llegar.")

