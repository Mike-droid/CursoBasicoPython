dolares = input("¿Cuántos dólares tienes? :")
dolares = float(dolares)
valor_dolarMX = 22.38
pesos = dolares * valor_dolarMX
pesos = round(pesos,2)
pesos = str(pesos)
print("Tienes $" + pesos + " pesos mexicanos")