# Importamos un modulo con todas las funciones y variables dentro.
# Recuerda que es POO funciones y variables se llaman (métodos y atributos)
# Es correcto decirlo de ambas formas
import time

# para usar los métodos y atributos llamamos al método en este caso sleep()
# Duerme 5 segundos
time.sleep(5)


# Para importar solo un método especifico
from time import sleep

# Para utilizar el método
sleep(5)

# Puedes importar los "modulos" o "archivos" siempre que esten en tu entorno
# Puede ser en:
#   1. El mismo Folder
#   2. Folder superior o inferior
#   3. Instalados en el amabiente
#
# Para los primeros 2 casos tendras que crear un archivo llamado _init_.py
# Este servira para que python reconozca los modulos.