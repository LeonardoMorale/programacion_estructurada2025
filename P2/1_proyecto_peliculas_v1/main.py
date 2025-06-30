import peliculas as pelis

'''
Crear un proyecto que permita gestionar (administrar) películas, colocar un menú de opciones para agregar, eliminar, modificar y consultar películas.

Notas:
1.- Utilizar funciones y mandar llamar desde otro archivo.
2.- Utilizar listas para almacenar los nombres de películas.
'''

# Limpiar Pantalla
pelis.borrar_pantalla()

# Menú principal
# Inicialización de variable para ciclo while
opc = True
while opc:
    print("--------------------------------\n".center(120))
    print("PELÍCULAS\n".center(120))
    print("--------------------------------\n".center(120))
    print("1.- Agregar películas".center(120))
    print("2.- Eliminar películas".center(120))
    print("3.- Modificar películas".center(120))
    print("4.- Consultar películas".center(120))
    print("5.- Buscar películas".center(120))
    print("6.- Vacíar películas".center(120))
    print("7.- Salir\n".center(120))
    print("--------------------------------\n".center(120))
    respuesta = pelis.obtener_1_7("    Seleccione una opción: ")

    match respuesta:
        case 1:
            pelis.agregar_peliculas()
        case 2:
            pelis.eliminar_peliculas()
        case 3:
            pelis.modificar_peliculas()
        case 4:
            pelis.consultar_pelis()
        case 5:
            pelis.Buscar_película()
        case 6:
            print("6")
        case 7:
            opc = False

