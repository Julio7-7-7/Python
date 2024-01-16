# and, or, not

gas = True
encendido = True
sirve = False
edad = 18

if gas and encendido:
    print("Puedes avanzar")

if gas or sirve:
    print("Puedes avanzar")

if gas and not encendido:
    print("Puedes avanzar")

if gas and encendido and not sirve and edad > 17:
    print("Puedes conducir")

if gas and (encendido or edad > 17):
    print("Puedes salir a conducir")
