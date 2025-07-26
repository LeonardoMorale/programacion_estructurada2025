'''
Crear un proyecto que permita gestionar (administrar) peliculas, colocar un menú de opciones para agregar, eliminar, modificar y consultar peliculas

NOTAS: 
1.- Utilizar funciones y mandar llamar desde otro archivo
2.- Utilizar diccionarios para almacenar los siguientes atributos: (nombre, categoria, clasificación, género, idioma) de las peliculas.
3.- Utilizar e implementar una base de datos para gestionar las películas.
'''

import peliculas


opcion=True
while opcion:
    peliculas.borrarPantalla()
    print("\n\t\t\t..::: CINEPOLIS CLON :::... \n\t\t..::: Sistema de Gestión de Peliculas :::...\n\t\t 1.- Crear  \n\t\t 2.- Borrar \n\t\t 3.- Mostrar \n\t\t 4.- Modificar \n\t\t 5.- Buscar \n\t\t 6.- SALIR ")
    opcion=input("\n\t\t Elige una opción: ").upper()

    match opcion:
        case "1":
            peliculas.crearPeliculas()
            peliculas.esperarTecla()
        case "2":
            peliculas.borrarPeliculas()
            peliculas.esperarTecla()  
        case "3":
            peliculas.mostrarPeliculas()
            peliculas.esperarTecla()     
        case "4":
            peliculas.modificarPeliculas()
            peliculas.esperarTecla()
        case "5":
            peliculas.buscarPeliculas()
            peliculas.esperarTecla()
        case "6":
            opcion=False
            peliculas.borrarPantalla()
            print("\n\tTerminaste la ejecucion del SW")
        case _: 
            input("\n\tOpción invalida vuelva a intentarlo ... por favor")

