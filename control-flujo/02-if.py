edad = 19
#Ten cuidado con el orden de lo que tienen if y elif por cómo se ejecutarán
if edad > 65:
    print("Puedes verlo con 30% de descuento")
elif edad > 54:
    print("Puedes verlo con 20% de descuento")
elif edad > 17:
    print("Puedes ver la pelicula")
else:
    print("No puedes entrar")
    print("Ve a otro lado")

print("Listo")