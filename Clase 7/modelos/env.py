
clavesDeAcceso = {
    "usuario": "kevinzepeda",
    "password": "Contraseña",
}

def createToken(clave):
    return clave["usuario"] + clave["password"]