# Progroama que calcule
# X = lo va a multiplicar entre si
# X = se va a sumar 5 veces
# r se le va a resta X

# Restrinciones
# No
from sys import argv
from functions import multiplicar
from functions import suma
from functions import resta


def main():
    x = int(argv[1])
    print(f"Resultado de multiplicacion: {multiplicar(x)}")
    resultado = suma(num=x)
    print(f"Resultado de suma: {resultado}")
    print(f"Resultad de resta: {resta(resultado=resultado, num=x)}")



if __name__ == '__main__':
    print("Usted esta ejecutando esto en consola\n")
    main()