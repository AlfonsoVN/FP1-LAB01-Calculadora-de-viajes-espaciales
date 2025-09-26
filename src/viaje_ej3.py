edad = int(input("Edad:"))
n_fisico = int(input("Nivel fisico:"))

if edad < 18:
    print("Debes ser mayor de edad")
elif n_fisico < 5:
    print("Debes estar en mejor forma")
else:
    print("¡Listo para despegar!")