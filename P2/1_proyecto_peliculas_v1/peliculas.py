import os

# Crear lista de peliculas
peliculas = []

def borrar_pantalla():
    os.system("cls")

def obtener_1_7(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor in range(1, 8):
                return valor
            else:
                print("Selecciona un número del 1 al 7. Porfavor vuelva a intentar.")
        except ValueError:
            print("Asegurese de ingresar un número entero.")

def mostrar_pelis():
    global peliculas
    for i in range (0, len(peliculas)):
        print(f"{i}.- {peliculas[i]}")

def obtener_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if isinstance(valor, int):
                return valor
            else:
                print("Asegurese de ingresar un número entero.")
        except ValueError:
            print("Asegurese de ingresar un número entero.")


def agregar_peliculas():
    opc = True
    while opc:
        pelicula = input("Ingresa la película que quieras agregar: ")
        global peliculas
        peliculas.append(pelicula)
        opc_2 = True
        while opc_2:
            respuesta = input("¿Desea ingresar otra película? (SI/NO) ").upper().strip()
            if respuesta in ["SI", "NO"]:
                opc_2 = False
            else:
                opc_2 = True
                print("Ingrese \"SI\" o \"NO\"")

        if respuesta == "SI":
            opc = True
        elif respuesta == "NO":
            opc = False

def eliminar_peliculas():
    opc = True
    while opc:
        mostrar_pelis()
        pelicula = obtener_entero("Ingrese el número de la película que desea borrar: ")
        global peliculas
        del peliculas[pelicula]
        opc_2 = True
        while opc_2:
            respuesta = input("¿Desea borrar otra película? (SI/NO) ").upper().strip()
            if respuesta in ["SI", "NO"]:
                opc_2 = False
            else:
                opc_2 = True
                print("Ingrese \"SI\" o \"NO\"")

        if respuesta == "SI":
            opc = True
        elif respuesta == "NO":
            opc = False

def modificar_peliculas():
    opc = True
    while opc:
        mostrar_pelis()
        pelicula = obtener_entero("Ingrese el número de la película que desea modificar: ")
        nueva_peli = input("Ingresa el nuevo nombre de la película: ")
        peliculas[pelicula] = nueva_peli
        opc_2 = True
        while opc_2:
            respuesta = input("¿Desea hacer otra modificación? (SI/NO) ").upper().strip()
            if respuesta in ["SI", "NO"]:
                opc_2 = False
            else:
                opc_2 = True
                print("Ingrese \"SI\" o \"NO\"")

        if respuesta == "SI":
            opc = True
        elif respuesta == "NO":
            opc = False


def consultar_pelis():
    modificar_peliculas()

def Buscar_película():
    global peliculas
    peliculas_low = [peli.lower() for peli in peliculas]
    pelicula = input("Ingrese el nombre de la película a buscar: ").lower().strip()
    contador = 0
    for i in peliculas_low:
        if pelicula in peliculas_low:
            contador+=1

    if contador > 0:
        if contador == 1:
            print(f"Sí, si tienes \"{pelicula.title()}\" en tu colección (1 vez)")
        else:
            print(f"Sí, si tienes \"{pelicula.title()}\" en tu colección ({contador} veces)")
    else:
        print(f"No, no tienes \"{pelicula.title()}\" en tu colección")

