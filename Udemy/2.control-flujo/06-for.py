buscar = 10
# for numero in range(5):
#     print(numero, numero*"hola mundo")

for numero in range(5):
    print(numero)
    if numero == buscar:
        print("encontrado", buscar)
        break
else:
    print("No encontré el número")


for char in "Ultimete Python":
    print(char)
