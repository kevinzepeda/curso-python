# Escribir mi nombre e imprimirlo en la consola


# Variable de nombre
# nombre = 'Kevin Zepeda'
# edad = 27

# Solicitar Nombre a usuario
nombre = input("¿Cuál es tu nombre?: ")

# Solicitar Edad a usuario
edad = int(input("¿Cuál es tu edad?: "))

# Imprimierdo la cadena a partir de nombre y edad, calculando año de nacimiento
print(f"Mi nombre es: {nombre} y mi edad es: {edad} años, naci en {2023 - edad}")