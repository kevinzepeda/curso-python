# Funciones en python

def cuadradoDeUnNumero(x:int) -> int:
    '''
    Funcion para elevar un numero al cuadrado

    params:
    ------
        x (int) : Numero para elevar

    Output:
    ------

        (int): Numero elevado al cuadrado 
    '''
    resultado = x * x
    return resultado

try:
    numero = int(input("¿Qué numero quieres elevar al cuadrado?: "))

    numero_calculado = cuadradoDeUnNumero(x=numero)

    print(f"El resultado es: {numero_calculado}")

except:
    print("Ingresa un número correcto")