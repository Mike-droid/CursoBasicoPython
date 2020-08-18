""" def imprimir_mensaje():
    print("Mensaje especial")
    print("Estoy aprendiendo a usar funciones")

imprimir_mensaje() """

""" def conversacion(mensaje):
    print("Hola")
    print(mensaje)
    print("Adios")

opcion = input("Elige una opcion[1,2,3]: ")

if opcion=='1':
    conversacion("Elegiste la opcion 1")
elif opcion=='2':
    conversacion("Elegiste la opcion 2")
elif opcion=='3':
    conversacion("Eligiste la opcion 3")
else:
    print("Escoge una opción correcta") """

def suma(numA,numB):
    print("Se suman dos numeros ")
    resultado = numA+numB
    return resultado

sumatoria =  suma(3,7)
print(sumatoria)