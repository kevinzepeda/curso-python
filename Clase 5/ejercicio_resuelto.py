# Crear una lista vacía para almacenar los contactos
agenda = []

# Ciclo principal para permitir al usuario agregar múltiples contactos
while True:
    print("==== Agregar contacto ====")
    
    # Solicitar al usuario los datos del contacto
    nombre = input("Nombre: ")
    email = input("Email: ")
    telefono = input("Teléfono: ")
    pais = input("País: ")

    # Crear un diccionario con los datos del contacto
    contacto = {
        "Nombre": nombre,
        "Email": email,
        "Teléfono": telefono,
        "País": pais
    }

    # Agregar el diccionario a la lista de contactos (agenda)
    agenda.append(contacto)

    # Preguntar al usuario si desea agregar otro contacto
    continuar = input("¿Deseas agregar otro contacto? (s/n): ")
    
    # Si la respuesta no es "s" (para indicar "sí"), romper el ciclo
    if continuar.lower() != "s":
        break

print("\n==== Agenda ====")

# Mostrar la lista de contactos almacenados en la agenda
for contacto in agenda:
    print("Nombre:", contacto["Nombre"])
    print("Email:", contacto["Email"])
    print("Teléfono:", contacto["Teléfono"])
    print("País:", contacto["País"])
    print("-----------------")