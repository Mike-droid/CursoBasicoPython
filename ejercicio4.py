#Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.

def run():
    nombre = input("Escribe tu nombre: ")
    cantidad = int(input("¿Cuantas veces quieres que se repita tu nombre?: "))
    for x in range(1,cantidad+1):
        print(nombre)


if __name__ == "__main__":
    run()