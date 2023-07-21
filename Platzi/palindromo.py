def palindromo(palabra):
    palabra = palabra.replace(" ", "")
    palabra = palabra.lower() 
    invertida = palabra[::-1]
    if palabra == invertida:
       return True
    else:
        return False

def main():
    palabra = input("Escribe una palabra: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("Es palindrono")
    else:
        print("No es palindromo")


if __name__ == "__main__":
    main()
    