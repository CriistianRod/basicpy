import random

def run():
    numero_aleatorio = random.randint(1, 100)
    numero_ingresado = int(input('Elige un número del 1 al 100: '))
    while numero_ingresado != numero_aleatorio:
        if numero_ingresado < numero_aleatorio:
            numero_ingresado = int(input('Elige un número más grande: '))
        if numero_ingresado > numero_aleatorio:
            numero_ingresado = int(input('Elige un número más pequeño: '))
    
    print('¡Ganaste!')

if __name__ == '__main__':
    run()