def run():
    ayuno = int(input("¿Cuantas horas quieres ayunar?[Solo escribe un numero]: "))
    while ayuno!=0:
        ayuno-=1
        if ayuno % 2 == 0:
            continue
        else:
            print("Te quedan " + str(ayuno) + " horas para volver a comer")


if __name__ == "__main__":
    run()