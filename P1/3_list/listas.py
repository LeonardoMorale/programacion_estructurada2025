import os 
'''
# Ejemplo 1 Crear una lista de numeros e imprimir el contenido

numeros = [1,2,3,4,5,6,7,8,9,10]

print(numeros)

for i in numeros:
    print(i)

for i in range (0, len(numeros)):
    print(numeros[i])

os.system("cls")

# Ejemplo 2 Crear una lista de palabras y posteriormente buscar la coincidencia de una palabra

palbras = ["árbol", "tronco", "madera", "palos", "hacha", "antorcha"]

palabra_buscar = input("Dame la palabra a buscar: ")

# 1er forma
encontro = False
for i in range (0, len(palbras)):
    if palbras[i] == palabra_buscar:
        encontro = True

if encontro:
    print("Si encontro la palabra")
else:
    print("No encontró la palabra")

# 2da forma
if palabra_buscar in palbras:
    print(f"Si encontré la palabra: {palabra_buscar}")

os.system("cls")

# Ejemplo 3 Añadir elementos a la lista

numeros2 = []
print(numeros2)

opc = True
while opc:
    numero = float(input("Dame un numero entero o decimal: "))
    numeros2.append(numero)
    resp = input("¿Deseas agregar otro número?").lower()
    if resp == "si":
        opc = True
    else:
        opc = False
'''

os.system("cls")

# Ejemplo 4 Crear una lista multidimensional que sea una agenda

agenda = [
           ["Carlos", "618912837"],
           ["Alberto", "48327322"],
           ["Martin", "874326724"]
           ]

print(agenda)

for i in agenda:
    print(i)

print("---------------")
#
#    for r in range(0,3):
#        for c in range(0,2):
#            print(agenda[r][c])

cadena = ""
for r in range(0,3):
    for c in range(0,2):
        cadena+=f"{agenda[r][c]},"
    cadena+="\n"
print(cadena)