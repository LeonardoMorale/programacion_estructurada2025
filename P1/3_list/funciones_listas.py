'''

List (Array)
son colecciones o conjunto de datos/valores bajo un mismo nombre, para acceder  a los valores se hace con un indice numerico.

Nota: sus valores si son modificables

La lista es una colección ordenada y modificable, permite miembros duplicados.



'''
# Funciones más comunes en las listas


paises = ["México", "Brasil", "España", "Canadá"]

numeros = [23,12,100,34]

# Ordenar ascendentemente
print(numeros)
numeros.sort()
print(numeros)
print(paises)
paises.sort()
print(paises)

# Añadir o Ingresar o Insertar elementos a una lista


# 1er forma 
paises.append("Honduras")

# 2da forma
paises.insert(1, "Honduras")
print(paises)

# Eliminar o Borrar o Quitar elementos a una lista
# 1er forma
paises.pop(1)
print (paises)

# 2da forma
paises.remove("Honduras")
print(paises)

# Buscar un elemento dentro de la lista
# 1er forma
resp="brasil" in paises
if resp:
    print("Si encontré el pais")
else:
    print("No encontré el pais")

# 2da forma
pais_buscar = input("Dame el país a buscar")
for i in range(0, len(paises)):
    if paises[i] == pais_buscar:
        print("Si encontre el pais")
    else:
        print("No encontre el pais")

# Cuantas veces aparece un elemento dentro de una lista

# numeros = [23,12,100,34]

print(f"Este numero 12 aparece: {numeros.count(12)} vez o veces")

numeros.append(12)
print(f"Este numero 12 aparece: {numeros.count(12)} vez o veces")

# Identificar o conocer el índice de un valor

# paises = ["México", "Brasil", "España", "Canadá"]

indice = paises.index("España")
print(indice)
paises.pop(indice)
print(paises)

# Recorrer los valores de la lista
# 1er forma
for i in paises:
    print(i)

# 2da forma
for i in range(0, len(paises)):
    print(f"El valor {i} es: {paises[i]}")

# Unir contenido de listas
# paises = ["México", "Brasil", "Canadá"]
# numeros = [23,12,100,34,12]

print(paises)
print(numeros)
paises.extend(numeros)
print(paises)

