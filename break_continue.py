def run():
    # for contador in range(1000):
    #     if contador % 2 != 0:
    #         continue
    #     print(contador)
    
    # for i in range(10000):
    #     print(i)
    #     if i == 5678:
    #         break

    # texto = input('Escribe un texto: ')
    # for letra in texto:
    #     if letra == 'o':
    #         continue
    #     print(letra)

    i = 0
    frase = input('Ingresa una frase: ')
    while i < len(frase):
        if frase[i] == 'a':
            i+=1
            continue
        print(frase[i])
        i+=1

if __name__ == '__main__':
    run()