def es_primo(numero):
    for i in range(2, numero):
        print(i)
        if numero % i == 0:
            print("Su mínimo múltiplo es: " + str(i))
            return False
        if i >= (numero/2):
            break
    return True


def run():
    numero = int(input('Escribe un número: '))
    if es_primo(numero):
        print(str(numero) + ' es primo')
    else:
        print(str(numero) + ' no es primo')


if __name__ == '__main__':
    run()