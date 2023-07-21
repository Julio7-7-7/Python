from turtle import st

def conversor(tipo_pesos, valor_dolar):
    pesos = int(input("Ingrese la cantidad en " + tipo_pesos + ": "))
    dolar= pesos / valor_dolar
    dolar = str(dolar)
    print("Tienes " + dolar + " dolares")

menu = """
Bienvenido al conversor de monedas💰
1 - Pesos argentinos
2 - Bolivianos
3 - Soles

Elige una opción """

opcion = int(input(menu))

if opcion == 1:
    conversor("Pesos argentinos", 5)
elif opcion == 2:
    conversor("Bolivianos", 7)
elif opcion == 3:
    conversor("Soles", 10)
else:
    print("Escoge una opción válida")   