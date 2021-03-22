def palindromo(palabra):
    palabra = palabra.lower()
    palabra = palabra.replace(' ','')
    #Compara y devuelve si es igual que al revés
    return palabra == palabra[::-1]


def run():
    palabra = input('Escribe una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo:
        print('Es palíndromo')
    else:
        print('No es palíndromo')
            


if __name__ == '__main__':
    run()


# palabra = input("Escribe una palabra: ")
# palabra = palabra.lower()
# palabra = palabra.replace(' ','')

# #La convierte "al revés"
# palabra_inversa = palabra[::-1]

# if palabra == palabra_inversa:
#     print('Es palíndromo')
# else:
#     print('No es palíndromo')
