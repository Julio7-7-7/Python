import random
while True:
    moneda = random.randint(1, 2)
    if moneda == 1:
        print("Es cara")
    else:
        print("Es cruz")
    instruccion = input("Desea volver a jugar S/n")
    if instruccion.lower() == "n":
        break
