def solicitarUsuario():
    nombre = input("Nombre: ")
    telefono = input("Telefono: ")
    return {
        "nombre": nombre,
        "telefono": telefono,
    }

contacts = []
agregar_usuario = True


while agregar_usuario:
    contacts.append(solicitarUsuario())
    
    pregunta = input("¿Quieres agregar otro? (S/N)")

    if pregunta.lower() != 's':
        agregar_usuario = False

print(contacts)
breakpoint()
for contact in contacts:
    print(contact["nombre"])
    print(contact["telefonoc"])