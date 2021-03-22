# pesos = input("¿Cuánta luka tienes?: ")
# pesos = float(pesos)
# valor_dolar = 3747
# dolares = pesos/valor_dolar
# dolares = round(dolares, 2)
# dolaresString = str(dolares)
# print("Tienes $" + str(dolares) + " dólares.")

# dolares = input("¿Cuántos dólares tienes?: ")
# dolares = float(dolares)
# valor_peso = 1/3747
# pesos = dolares/valor_peso
# pesos = round(pesos, 2)
# print("Tienes $" + str(pesos) + " pesos.")

def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿Cuánta "+ tipo_pesos + "luka tienes?: ")
    pesos = float(pesos)
    dolares = pesos/valor_dolar
    dolares = round(dolares, 2)
    print("Tienes $" + str(dolares) + " dólares.")

menu = """
Bienvenido al conversor de monedas 💰

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    conversor("COP", 3475)
elif opcion == 2:
    conversor("ARS", 73.92)
elif opcion == 3:
    conversor("MXN", 21.75)
else:
    print('Elige una opción válida, por fa')