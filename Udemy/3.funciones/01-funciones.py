# def hola(nombre):
#     print(f"Hola {nombre}")
#     print("Ultimate Python")

# hola("Julio")


# #Argumentos por defecto 
# def saludoPer(nombre, apellido="Toledo"):
#     print(f"Hola {nombre} {apellido}")

# saludoPer("Julio", "César")

# def arCuadrada(ancho, alto):
#     area = ancho * alto
#     print(f"El area de un cuadrado es {str(area)}")

# arCuadrada(5,4)

def areaRectangulo(alto, ancho):
    if alto != ancho:
        area = ancho * alto
        print(f"El area del rectangulo es = {str(area)}")
    else:
        print("Los datos no son los de un rectangulo")

areaRectangulo(5,5)
areaRectangulo(5,6)

def verificador(n):
    mensaje = f"El numero {n} es par" if n % 2 == 0 else f"El numero {n} es impar"
    print(mensaje)

verificador(2)
verificador(3)


def maximoMej(x,y,z):
    if x>y and x>z:
        print(f"El mayor es {x}")
    elif y>x and y>z:
        print(f"El mayor es {y}")
    else:
        print(f"El mayor es {z}")


maximoMej(2,4,5)
maximoMej(2,1,0)
maximoMej(5,6,2)

def celciusFar(grado):
    temp = (grado * 9/5) +32
    print(f"La temperatura {grado} C° es = a {temp} F°")

celciusFar(20)