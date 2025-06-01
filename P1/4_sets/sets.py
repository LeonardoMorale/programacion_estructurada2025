'''
Es un tipo de dato para tener una colección de valores pero no tiene ni indice ni orden.

Set es una colección desordenada, inmutable y no indexada.
No hay miembros duplicados.
'''
import os
os.system("cls")

personas = {"Ramiro", "Coche", "Lupe"}
print(personas)
personas.add("Peje")
print(personas)
personas.pop()
print(personas)
personas.clear()
print(personas)

varios = {3.12, 3, True, "Hola"}
print(varios)


# Crear un programa que solicite los emails de los alumnos de la UTD almacenar en una lista y posteriormente mostrar en pantalla los mails sin duplicados
opc = "si"
emails = []
while opc=="si":
    emails.append(input("Dame el email: "))
    opc = input("¿Deseas solicitar otro email (si/no): ").lower()

# Imprimir los emails sin duplicados 

print(emails)
