#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.

def run(salario,horas):
    dinero_ganado = salario * horas
    print("Has ganado {} dólares".format(dinero_ganado))


if __name__ == "__main__":
    salario = float(input("¿Cuanto ganas en dólares por hora?: "))
    horas = int(input("¿Cuantas horas trabajaste?: "))
    run(salario,horas)