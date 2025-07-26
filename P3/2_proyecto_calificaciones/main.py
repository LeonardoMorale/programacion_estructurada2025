'''
Crear un proyecto que permita gestionar (administrar) calificaciones, colocar un menú de opciones para agregar, mostrar y calcular promedio.

NOTAS: 
1.- Utilizar funciones y mandar llamar desde otro archivo
2.- Utilizar list (bidimensionales) para almacenar: 
'''

import calificaciones

def main():
    opcion=True

    while opcion:
        calificaciones.borrarPantalla()
        opcion = calificaciones.menu_principal()

        match opcion:
            case "1":
                calificaciones.crearCalificaciones()
                calificaciones.esperarTecla()
            case "2":
                calificaciones.borrarCalificaciones()
                calificaciones.esperarTecla()
            case "3":
                calificaciones.mostrarCalificaciones()
                calificaciones.esperarTecla()
            case "4":
                calificaciones.modificarCalificaciones()
                calificaciones.esperarTecla()
            case "5":
                calificaciones.buscarCalificaciones()
                calificaciones.esperarTecla()
            case "6":
                opcion = False
                calificaciones.borrarPantalla()
                print("Terminaste la ejecución del SW")
            case _: 
                opcion = True
                input("\n\tOpción invalida vuelva a intentarlo ... por favor")

if __name__ == "__main__":
    main()
