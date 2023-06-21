range(65) # range(0,64) [0,1,...64]

for item in range(16):
    print(item)

nombres = ["Fran", "Kevin", "Gio", "Manuel"]
# Acceder al indice

#Es posible asignr n variables para n objetos iterables
nombre, edad = ("Kevin", 27)

print(nombre)
print(edad)

enumerate(nombres) # iterable [(idx,val)]

for idx, nombre in enumerate(nombres):
    print(f"{idx}, {nombre}")
