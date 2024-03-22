def no_space(texto):
    nuevo_texto = ""
    for char in texto:
        if char != " ":
            nuevo_texto += char
    return nuevo_texto


def reverse(texto):
    otxet = ""
    for char in texto:
        otxet = char + otxet
    return otxet


def es_palindromo(texto):
    texto = no_space(texto)
    otxet = reverse(texto)
    return texto.lower() == otxet.lower()


print(es_palindromo("waos soaw"))
