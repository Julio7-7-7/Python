animal = "vAca redonda"
print(animal.upper())
print(animal.lower())
# primer letra mayuscula
print(animal.strip().capitalize())
# Primer letra de cada palabra en mayuscula
print(animal.title())
# Borra los espacios en blanco a los costados r o l
# principio para escoger o izq o derecha
print(animal.strip())
print(animal.find("re"))
print(animal.replace("vA", "Va"))
print("redonda" in animal)
print("redonda" not in animal)
# Encontrar las ocurrencias dentro de una cadena
print(animal.upper().count('A'))
# Encontrar el último caracter de una cadena
print(animal[-1])
