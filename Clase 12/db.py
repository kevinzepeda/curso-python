import sqlite3




def insertarUsuario(usuario):
    conn = sqlite3.connect("store.db")
    c = conn.cursor()
    
    nombre = usuario["nombre"]
    apellido = usuario["apellido"]
    correo = usuario["correo"]
    telefono = usuario["telefono"]

    c.execute('''
    INSERT INTO usuarios (nombre, lastname, email, telephone)
    VALUES (?,?,?,?)
    ''', (nombre, apellido, correo, telefono))

    conn.commit()
    conn.close()
    return { "mesage": f"usuario {nombre} creado"}