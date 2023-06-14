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

    

    #Si mi numero es mayor que 1000000 No hacerlo
    if numero >= 1000000:
        print("El numero es muy grande")
    
    # Si mi numero es mayor que 0
    elif numero < 0:
        print("No es posible elevar numeros negativos")
    # Si no
    else:
        numero_calculado = cuadradoDeUnNumero(x=numero)
        print(f"El resultado es: {numero_calculado}")

except:
    print("Ingresa un número correcto")