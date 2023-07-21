def conversacion(mensaje):
    print("Hola")
    print(mensaje)
    print("adios")

opcion = int(input("Escoge una opcion  1, 2, 3 : "))
if opcion == 1:
    conversacion("Escogiste la opcion 1")
elif opcion == 2:
    conversacion("Escogiste la opcion 2")
elif opcion == 3:
    conversacion("Escogiste la opcion 3")
else:
    print("Escoge una opcion valida")
    
def suma(a, b):
    print("Se suman dos numeros")
    resultado = a + b
    return resultado

sumatoria = suma(1 , 4)
print(sumatoria)