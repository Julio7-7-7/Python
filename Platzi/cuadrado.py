def run():
    pass

x = 0
i = 1
n = int(input("¿Cuantos numeros desea ingresar?: "))
for i in range(n):
    suma= int(input("Digite el numero: "))
    x = suma + x
print("La media es: " , x / i )


if __name__ == "__main__":
    run()