import os

# Un modulo es simplemente un archivo con extensión .py que contiene código de python (funciones, clases, variables, etc.).

# Un paquete es una carpeta que contiene varios módulos (archivos .py) y un archivo especial llamado __init__.py, que le indica a Python que esa carpeta debe tratarse como un paquete.

os.system("cls")

def solicitardatos():
    nombre=input("nombre: ")
    telefono=input("telefono: ")

    print(f"el nombre es: {nombre} y su telefono es: {telefono}")

def solicitardatos2():
    nombre=input("nombre: ")
    tel=input("telefono: ")
    return nombre,tel

def solicitardatos3(nombre,telefono):
    nombre=nombre
    telefono=telefono

    print(f"el nombre es: {nombre} y su telefono es: {telefono}")

def solicitardatos4(nombre,teledono):
    nombre=nombre
    telefono=telefono
    return nombre,telefono

def borrarPantalla():
    os.system("cls")

def esperarTecla():
    input("...Oprima una tecla para continuar...")

def saludar(nombre):
    nom = nombre
    return f"Hola, bienvenido {nom}"

