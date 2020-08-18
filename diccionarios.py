def run():
    mi_diccionario = {
        'llave1' : 1,
        'llave2' : 2,
        'llave3' : 3
    }
    
    """ print(mi_diccionario['llave1'])
    print(mi_diccionario['llave2'])
    print(mi_diccionario['llave3']) """

    poblacion_pais={
        'Argentina' : 44938712,
        'Brasil' : 210147125,
        'Colombia' : 50372424
    }

    #print(poblacion_pais['Argentina'])

    """ for pais in poblacion_pais.keys(): #!Con keys accedemos a la llave del diccionario
        print(pais) """

    """ for pais in poblacion_pais.values(): #!Con values accedemos al valor del diccionario
        print(pais) """

    for pais,poblacion in poblacion_pais.items(): #!Con items accedemos a la clave y al valor
        print(pais + " tiene " + str(poblacion) + " habitantes")


if __name__ == "__main__":
    run()