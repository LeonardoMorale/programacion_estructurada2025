import agenda

def main ():
    opcion = True

    while opcion:
        agenda.limpiar_pantalla()
        opcion = agenda.menu_principal()

        match opcion:
            case 1:
                agenda.crearContacto()
                agenda.esperar_tecla()
            case 2:
                agenda.borrarContacto()
                agenda.esperar_tecla()
            case 3:
                agenda.mostrarCcontactos()
                agenda.esperar_tecla()
            case 4:
                agenda.modificar_contacto()
                agenda.esperar_tecla()
            case 5:
                agenda.buscarContactos()
                agenda.limpiar_pantalla()
            case 6:
                agenda.limpiar_pantalla()
                opcion = False
                print("Terminaste la ejecución del SW")
            case _:
                pass

main()