print("Bienvenido a la calculadora")
print("Tiene disponibles las operaciones de suma resta multi y divi")
print("Puede salir en cualquier momento typeando salir")

resultado = ""
while True:
    if not resultado:
        resultado = input("Ingrese un número: ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)
    op = input("Ingrese la operación: ")
    if op.lower() == "salir":
        break
    n2 = input("Ingrese el segundo número: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)

    if op.lower() == "suma":
        resultado += n2
    elif op.lower() == "resta":
        resultado = - n2
    elif op.lower() == "multi":
        resultado *= n2
    elif op.lower() == "div":
        resultado /= n2
    else:
        print("Operación inválida")
        break
    print(f"El resultado es {resultado}")
