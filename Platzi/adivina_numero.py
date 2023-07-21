import random


def run():
    number = random.randint(1, 100)
    numero_elegido = int(input("Elige un numero"))
    while numero_elegido != number:
        if numero_elegido < number:
            print("Escoge un numero mas alto")
        else:
            print("Escoge un numero mas bajo")
        numero_elegido = int(input("Ingresar otro numero"))
    print("Ganaste")
    

if __name__ == "__main__":
    run()