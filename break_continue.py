def run():
    """ for contador in range(1000):
        if contador % 2 != 0:
            continue #!Lo que está después de continue no se va a ejecutar
        print(contador) """

    """ for i in range(400):
        print(i)
        if i == 140:
            break #!Aquí le digo detente y termina todo """

    texto = input("Escribe un texto: ")
    for letra in texto:
        if letra=='o':
            break
        print(letra)


if __name__ == "__main__":
    run()