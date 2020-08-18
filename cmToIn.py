inches = 2.54

def convierte_cm_en_in(estatura_cm):
    estatura_cm = float(estatura_cm)
    estatura_in = estatura_cm / inches
    estatura_in = round(estatura_in,2)
    estatura_in = str(estatura_in)
    print("Tu estatura en pulgadas es: " + estatura_in)

menu = """
Por favor, ingresa tu estatura en cm: 
"""

estatura = input(menu)

convierte_cm_en_in(estatura)