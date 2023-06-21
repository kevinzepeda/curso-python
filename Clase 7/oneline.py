from modelos.env import clavesDeAcceso

def calculadora(a, b, funcion):
    if funcion == '+':
        return a + b
    elif funcion == '-':
        return a - b
    elif funcion == '*':
        return a * b
    elif funcion == '/':
        return a/b
    else:
        print("No existe la funcion")


a = int(input("A: "))
b = int(input("B: "))
operacion = input("¿Que Operecion?: ")

# parametro if condicion else parametro si no se s cumple
funciones = {
    "aritmeticas": ["+", "-", "*", "/"],
    "algebraicas": []
}


# print(calculadora(a,b,operacion)) if operacion in funciones["aritmeticas"] else print("No existe")


# For - Utiles para iteraradores

lista = ["Fran", "Kevin", "Gio", "Manuel"]
print(lista)
lista = [nombre + "-1" for nombre in lista]
print(lista)