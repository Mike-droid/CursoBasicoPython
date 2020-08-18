import random


def generate_password():
    capitals = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    lower = ['a','b','c','d','e','g','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    symbols = ['!','?','#','$','&','%','(',')','*','^','/','°']
    numbers = ['1','2','3','4','5','6','7','8','9','0']

    characters = capitals + lower + symbols + numbers

    password = []

    for i in range(15):
        random_character = random.choice(characters) #!Seleccionamos un caracter al azar de las listas
        password.append(random_character)

    password = ''.join(password) #!Todos los caracteres se unen en una cadena sin espacios
    return password


def run():
    password = generate_password()
    print("Your new password is: " + password)


if __name__ == "__main__":
    run()