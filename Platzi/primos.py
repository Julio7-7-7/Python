def es_primo(numero):
    contador = 0

    for i in range(numero):
        if numero % i == 0:
            True
        else:
            False


def run():
    numero = int(input("Ingresa un numero: "))
    if es_primo(numero):
        print("Es primo")
    else:
        print("No es primo")



if __name__ == "__main__":
    run()