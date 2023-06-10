# Clase 3 Funciones y Variables
[Video de la clase](https://youtu.be/3UIkkmbMvd4)


## Creación de código con Python

VS Code es un tipo especial de editor de texto que se llama compilador. En la parte superior, notará un editor de texto y, en la parte inferior, verá una terminal donde puede ejecutar comandos.

En la terminal, puede ejecutar el comando `code` para comenzar a escribir código.

En el editor de texto anterior, puede escribir `print("hello, world")`. Este es un famoso programa canónico que casi todos los programadores escriben durante su proceso de aprendizaje.

En la ventana de terminal, puede ejecutar comandos. Para ejecutar este programa, deberá mover el cursor a la parte inferior de la pantalla, haciendo clic en la ventana de la terminal. Ahora puede escribir un segundo comando en la ventana del terminal. Junto al signo de dólar, escriba `python hello.py` y presione la tecla Intro en su teclado.

Recuerde, las computadoras realmente solo entienden ceros y unos. Por lo tanto, cuando ejecute `python hello.py`, python interpretará el texto que creó `hello.py` y lo traducirá a ceros y unos que la computadora pueda entender.

El resultado de ejecutar el comando `python hello.py`  es: `hello, world`

¡Felicitaciones! Acabas de crear tu primer programa.

## Funciones
Las funciones son verbos o acciones que la computadora o el lenguaje informático ya sabrá realizar.

En su `hello.py` programa, la función `print` sabe cómo imprimir en la ventana del terminal.

La printfunción toma **argumentos**. En este caso, **"hello, world"** son los argumentos que `print` toma la función.

## Bugs
Los errores son una parte natural de la programación. Imagine en nuestro `hello.py` programa que accidentalmente escribió `print("hello, world"` un aviso de que nos perdimos el final `)` requerido por el compilador. Si cometo este error a propósito, ¡el compilador generará un error en la ventana de la terminal!

A menudo, los mensajes de error le informarán sobre su error y le brindarán pistas sobre cómo solucionarlo. Sin embargo, habrá muchas veces que el compilador no sea de este tipo.

## Mejorar su primer programa de Python

Podemos personalizar tu primer programa en Python.
En nuestro editor de texto hello.pypodemos añadir otra función. inputes una función que toma un aviso como argumento. Podemos editar nuestro código para decir

```
input("¿Cuál es tu nombre?: ")
print("Hello, world")
```
Sin embargo, esta edición por sí sola no permitirá que su programa genere lo que ingresa su usuario. Para eso, tendremos que presentarle las variables.

## Variables

Una variable es solo un contenedor para un valor dentro de su propio programa.
En su programa, puede introducir su propia variable en su programa editándola para leer

```
name = input("¿Cuál es tu nombre?: ")
print("hello, world")
```
Tenga en cuenta que este `=` signo igual en el medio `name = input("Cuál es tu nombre ")` tiene un papel especial en la programación. Este signo igual asigna literalmente lo que está a la derecha a lo que está a la izquierda. Por lo tanto, el valor devuelto por `input("¿Cuál es tu nombre?: ")` se asigna a name.


Si edita su código de la siguiente manera, notará un error

```
nombre = input("¿Cuál es tu nombre?: ")
print("Hola, nombre")
```

El programa devolverá `Hola, name` a la ventana de terminal independientemente de lo que escriba el usuario.
Editando más nuestro código, puede escribir:
```
name = input("¿Cuál es tu nombre?: ")
print("Hola,")
print(name)
```

El resultado en la ventana de terminal sería:
```
¿Cuál es tu nombre?: Kevin
Hola,
Kevin
```

¡Nos estamos acercando al resultado que podríamos pretender!

Puede obtener más información en la documentación de Python sobre tipos de datos .

## Comentarios
Los comentarios son una forma para que los programadores rastreen lo que están haciendo en sus programas e incluso informen a otros sobre sus intenciones para un bloque de código. En resumen, ¡son notas para usted y para otros que verán su código!
Puede agregar comentarios a su programa para poder ver qué es lo que está haciendo su programa. Puede editar su código de la siguiente manera:

```
# Preguntar al usuario por su nombre
nombre = input("¿Cuál es tu nombre?: ")
print("Hola,")
print(nombre)
```

Los comentarios también pueden servirle como lista de tareas pendientes.

## pseudocódigo
El pseudocódigo es un tipo importante de comentario que se convierte en un tipo especial de lista de tareas, especialmente cuando no comprende cómo realizar una tarea de codificación. Por ejemplo, en su código, puede editar su código para decir:
```
# Pregunta por el nombre
nombre = input("¿Cuál es tu nombre?: ")

# Imprime en la consola Hola
print("Hola,")

# Imprime en la consola el valor de 'nombre'
print(nombre)
```
### Mejorando aún más su primer programa de Python
Podemos editar aún más nuestro código de la siguiente manera:
```
# Pregunta al usuario por su nombre
name = input("¿Cuál es tu nombre?: ")

# Imprime en la consola Hola + el valor de 'nombre'
print("hello, " + name)
```
Resulta que algunas funciones toman muchos argumentos.

Podemos usar una coma ,para pasar múltiples argumentos editando nuestro código de la siguiente manera:

```
# Solicitar nombre al usuario
nombre = input("¿Cuál es tu nombre?: ")

# Imprimir el nombre en la consola como un parameto adicional
print("Hola,", nombre)
```
La salida en la terminal, si escribimos `Kevin` la salida sería `Hola, Kevin`

## Cadenas y Parámetros
Una cadena, conocida como stren Python, es una secuencia de texto.
Rebobinando un poco en nuestro código a lo siguiente, hubo un efecto secundario visual de que el resultado apareciera en varias líneas:
```
# Solicitar nombre al usuario
nombre = input("¿Cuál es tu nombre?: ")
print("Hola,")
print(nombre)
```
Las funciones toman argumentos que influyen en su comportamiento. Si observamos la documentación, printnotará que podemos aprender mucho sobre los argumentos que toma la función de impresión.

Puede utilizar una cadena tipo f
```
# Solicitar nombre al usuario
nombre = input("¿Cuál es tu nombre?: ")
print(f"Hola, {nombre}")
```
Observe la f en los argumentos de `print(f"Hola, {nobre}")`. Esta f es un indicador especial para que Python trate esta cadena de una manera especial, diferente a los enfoques anteriores que hemos ilustrado en esta lección. Espere que usará este estilo de cadenas con bastante frecuencia en este curso.

## Más sobre strings
Nunca debe esperar que su usuario coopere según lo previsto. Por lo tanto, deberá asegurarse de que la entrada de su usuario sea corregida o verificada.

Resulta que las cadenas están integradas en la capacidad de eliminar espacios en blanco de una cadena.

Al utilizar el método `strip` en nombre `nombre = nombre.strip()`, eliminará todos los espacios en blanco a la izquierda y a la derecha de la entrada de los usuarios. Puedes modificar tu código para que sea:

```
# Solicitar nombre al usuario
nombre = input("¿Cuál es tu nombre?: ")

# Elimina espacios al principio y al final
nombre = nombre.strip()

# Crea una cadena f con la variable nombre y despues la imprime
print(f"Hola, {nombre}")
```

Al volver a ejecutar este programa, independientemente de cuántos espacios escriba antes o después del nombre, eliminará todos los espacios en blanco.

Usando el método `title` , titularía el nombre del usuario:

```
# Solicitar nombre al usuario
nombre = input("¿Cuál es tu nombre?: ")

# Elimina espacios al principio y al final
nombre = nombre.strip()

# Transforma la primer letra al estilo capital
nombre = nombre.title()

# Crea una cadena f con la variable nombre y despues la imprime
print(f"Hola, {nombre}")
```
En este punto, es posible que esté muy cansado de escribir `python` repetidamente en la ventana de la terminal. Usted nos hace que la flecha hacia arriba de su teclado recuerde los comandos de terminal más recientes que ha realizado.
Tenga en cuenta que puede modificar su código para que sea más eficiente:

```
# Solicitar nombre al usuario
nombre = input("¿Cuál es tu nombre?: ")

# Elimina espacios al principio y al final despues aplica un transfomacion a letra capital
nombre = nombre.strip().title()

# Crea una cadena f con la variable nombre y despues la imprime
print(f"Hola, {nombre}")
```
Esto crea el mismo resultado que su código anterior.

¡Incluso podríamos ir más allá!

```
# Solicitar nombre al usuario, quita espacios y transforma a letra capital
nombre = input("¿Cuál es tu nombre?: ").strip().title()

# Crea una cadena f con la variable nombre y despues la imprime
print(f"Hola, {nombre}")
```

Puede obtener más información sobre las cadenas en la documentación de [Python](https://docs.python.org)

## Enteros o int
En Python, un número entero se conoce como `int`.

En el mundo de las matemáticas, estamos familiarizados con los operadores +, -, *, / y %. Es posible que ese último operador % u operador de módulo no le resulte muy familiar.

Podemos escribir `code calculadora.py` en la terminal. Esto creará un nuevo archivo en el que crearemos nuestra propia calculadora.
Primero, podemos declarar algunas variables.
```
x = 1
y = 2

z = x + y

print(z)
```
Naturalmente, cuando ejecutamos `python calculadora.py` obtenemos el resultado en la ventana de terminal de 3. Podemos hacer esto más interactivo usando la función `input`.

```
x = input("Valor para X: ")
y = input("Valor para Y: ")

z = x + y

print(z)
```
Al ejecutar este programa, descubrimos que la salida es incorrecta como 12. ¿Por qué podría ser esto?
Anteriormente, hemos visto cómo el signo `+` concatena dos cadenas. Debido a que su entrada desde su teclado en su computadora ingresa al compilador como texto, se trata como una cadena. Por lo tanto, necesitamos convertir esta entrada de una cadena a un número entero. Podemos hacerlo de la siguiente manera:

```
x = input("Valor para X: ")
y = input("Valor para Y: ")

z = int(x) + int(y)

print(z)
```
El resultado ahora es correcto. El uso de int(x), se denomina "conversión", donde un valor se cambia temporalmente de un tipo de variable (en este caso, una cadena) a otro (aquí, un número entero).

Podemos mejorar aún más nuestro programa de la siguiente manera:

```
x = int(input("Valor para X: "))
y = int(input("Valor para y: "))

print(x + y)

```
Esto ilustra que puede ejecutar funciones en funciones. La función más interna se ejecuta primero y luego se ejecuta la más externa. Primero, inputse ejecuta la función. Entonces, la intfunción.

Puede obtener más información en la Documentación de Python de int.

### Gana la legibilidad
Al decidir sobre su enfoque para una tarea de codificación, recuerde que uno podría presentar un argumento razonable para muchos enfoques del mismo problema.

Independientemente del enfoque que adopte para una tarea de programación, recuerde que su código debe ser legible. Debes usar comentarios para darte a ti mismo y a otros pistas sobre lo que está haciendo tu código. Además, debe crear código de una manera que sea legible.

## Conceptos básicos de Punto Flotante
Un valor de punto flotante es un número real que tiene un punto decimal, como 0.52.

Puede cambiar su código para admitir números flotantes de la siguiente manera:

```
x = float(input("Valor de x: "))
y = float(input("Valor de y: "))

print(x + y)

```
Este cambio le permite a su usuario ingresar 1.2y 3.4presentar un total de 4.6.

Sin embargo, imaginemos que desea redondear el total al entero más cercano. Si mira la documentación de Python, `round` verá que los argumentos disponibles son `round(number[n, ndigits])`. Esos corchetes indican que el programador puede especificar algo opcional. Por lo tanto, podría hacer `round(n)` para redondear un dígito a su entero más cercano. Alternativamente, podría codificar de la siguiente manera:

```
# Obtener valores del usuario
x = float(input("Valor de x: "))
y = float(input("Valor de y: "))

# Crear un resultado rendondeado
z = round(x + y)

# Imprimir el resultado en consola
print(z)
```
La salida se redondeará al entero más próximo.

¿Qué pasaría si quisiéramos formatear la salida de números largos? Por ejemplo, en lugar de ver 1000, es posible que desee ver 1,000. Podrías modificar tu código de la siguiente manera:

```
# Obtener valores del usuario
x = float(input("Valor de x: "))
y = float(input("Valor de y: "))

# Crear un resultado rendondeado
z = round(x + y)

# Imprimir el resultado en consola
print(f"{z:,}")
```
Aunque bastante difícil de entender, esto `print(f"{z:,}")` crea un escenario en el que la salida `z` incluirá comas donde el resultado podría verse como 1,000 o 2,500.

### Más sobre números flotantes
¿Cómo podemos redondear los valores de punto flotante? Primero, modifica tu código de la siguiente manera:
```
# Obtener valores del usuario
x = float(input("Valor de x: "))
y = float(input("Valor de y: "))

# Crear un resultado rendondeado
z = x / y

# Imprimir el resultado en consola
print(z)
```
Al ingresar 2 como `x` y 3 como `y`, el resultado z 0.6666666666 aparentemente se vuelve infinito como cabría esperar.

Imaginemos que queremos redondear esto hacia abajo, podríamos modificar nuestro código de la siguiente manera:

```
# Obtener valores del usuario
x = float(input("Valor de x: "))
y = float(input("Valor de y: "))

# Crear un resultado rendondeado
z = round(x / y, 2)

# Imprimir el resultado en consola
print(z)
```
Como era de esperar, esto redondeará el resultado a los dos puntos decimales más cercanos.

También podríamos usar fstring (cadena f) para formatear la salida de la siguiente manera:

```
# Obtener valores del usuario
x = float(input("Valor de x: "))
y = float(input("Valor de y: "))

# Crear un resultado rendondeado
z = x / y

# Imprimir el resultado en consola
print(f"{z:.2f}")
```

Este código difícil de entender `fstring` muestra lo mismo que nuestra estrategia de redondeo anterior.

Puede obtener más información en la documentación de Python de float.

## Def
¿No sería bueno crear nuestras propias funciones?

Recuperemos nuestro código final `hello.py` escribiendo `code hello.py` en la ventana de la terminal. Su código de inicio debe tener el siguiente aspecto:

```
# Solicitar nombre al usuario, quita espacios y transforma a letra capital
nombre = input("¿Cuál es tu nombre?: ").strip().title()

# Crea una cadena f con la variable nombre y despues la imprime
print(f"Hola, {nombre}")
```

¡Podemos mejorar nuestro código para crear nuestra propia función especial que diga "hola" por nosotros!

Borrando todo nuestro código en nuestro editor de texto, empecemos de cero:
```
nombre = input("¿Cuál es tu nombre?: ")
Hola()
print(nombre)
```
Al intentar ejecutar este código, su compilador arrojará un error. Después de todo, no hay una función definida para `Hola()`.

Podemos crear nuestra propia función llamada hellode la siguiente manera:

```
def hola():
    print("Hola,")


nombre = input("¿Cuál es tu nombre?: ")
hola()
print(nombre)
```
Observe que todo lo que está debajo def `hola()` está sangrado o tabulado. Python es un lenguaje sangrado. Utiliza sangría para comprender qué es parte de la función anterior. Por lo tanto, todo en la función `hola()` debe estar sangrado.
Cuando algo no está sangrado, lo trata como si no estuviera dentro de la hellofunción. Ejecutándose `python hello.py` en la ventana de la terminal, verá que su resultado no es exactamente como lo desea.

Podemos mejorar aún más nuestro código:

```
# Create our own function
def hola(nombre):
    print("Hola,", nombre.strip().title())


# Output using our own function
nombre = input("¿Cúal es tu nombre?: ")
hola(nombre)
```

Aquí, en las primeras líneas, estás creando tu función `hola`. Esta vez, sin embargo, le está diciendo al compilador que esta función toma un solo parámetro: una variable llamada `nombre`. Por lo tanto, cuando llama `hola(nombre)` la computadora pasa `nombre` a la función hola como `nombre`. Así es como pasamos valores a funciones. 

¡Muy útil! Ejecutando `python hello.py` en la ventana de terminal, verá que la salida es mucho más cercana a nuestro ideal presentado anteriormente en esta lección.

### Podemos cambiar nuestro código para agregar un valor predeterminado a hello:

```
# Definimos una funcion
def hola(nombre="Kevin"):
    print("Hola,", Kevin)

# Solicitar nombre a usuario
nombre = input("¿Cúal es tu nombre?: ")

# llama a la función con nombre como argumento
hola(nombre)

# Llama a la función sin argumentos
hello()
```
Pruebe su código usted mismo. Observe cómo el primero `hola` se comportará como cabría esperar y el segundo `hola`, al que no se le pasa un valor, generará de forma predeterminada `Hola, Kevin`.

No tenemos que tener nuestra función al comienzo de nuestro programa. Podemos moverlo hacia abajo, pero debemos decirle al compilador que tenemos una función `main` y que tenemos una función `hola` separada.

```
def main():

    # Solicitar nombre a usuario
    nombre = input("¿Cúal es tu nombre?: ")

    # llama a la función con nombre como argumento
    hola(nombre)

    # Llama a la función sin argumentos
    hello()


# Definimos una funcion
def hola(nombre="Kevin"):
    print("Hola,", Kevin)
```

Esto solo, sin embargo, creará una especie de error. ¡ Si corremos `python hello.py` no pasa nada! La razón de esto es que nada en este código está realmente llamando a la función `main` y dando vida a nuestro programa.

La siguiente modificación muy pequeña llamará a la mainfunción y restaurará nuestro programa para que funcione correctamente:

```
def main():

    # Solicitar nombre a usuario
    nombre = input("¿Cúal es tu nombre?: ")

    # llama a la función con nombre como argumento
    hola(nombre)

    # Llama a la función sin argumentos
    hello()


# Definimos una funcion
def hola(nombre="Kevin"):
    print("Hola,", Kevin)


main()
```

## Valores devueltos
Puede imaginar muchos escenarios en los que no solo desea que una función realice una acción, sino también que devuelva un valor a la función principal. Por ejemplo, en lugar de simplemente imprimir el cálculo de x + y, es posible que desee que una función devuelva el valor de este cálculo a otra parte de su programa. Este “retroceder” de un valor lo llamamos valor devuelto.

Volviendo a nuestro codigo `calculadora.py`  escribiendo code calculator.py. Borre todo el código allí. Vuelva a trabajar el código de la siguiente manera:

```
def main():
    x = int(input("Valor de x: "))
    print("x elevado al cuadrado es:", square(x))


def square(n):
    resultado = n * n
    return resultado

main()
```
Efectivamente, `x` se pasa a square. Luego, el cálculo de `x * x` vuelve a la función principal.

Resumiendo
A través del trabajo de esta única lección, ha aprendido habilidades que usará innumerables veces en sus propios programas.

Creando tus primeros programas en Python;
funciones;
Bugs;
variables;
Comentarios;
pseudocódigo;
Instrumentos de Strings;
parámetros;
cadenas formateadas;
enteros;
Principios de legibilidad;
flotadores;
Crear sus propias funciones; y
Valores de retorno.