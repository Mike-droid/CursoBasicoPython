#Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.

def run():
    nombre = input("Escribe tu nombre, por favor: ")
    print("Hola, " + nombre)


if __name__ == "__main__":
    run()