import agenda

def main ():
    opcion = True
    agenda_contactos = {

    }

    while opcion:
        agenda.limpiar_pantalla()
        opcion = agenda.menu_principal()

        match opcion:
            case 1:
                agenda.limpiar_pantalla()
                agenda.agregar_contacto(agenda_contactos)
                agenda.esperar_tecla()
            case 2:
                agenda.limpiar_pantalla()
                agenda.mostrar_contactos(agenda_contactos)
                agenda.esperar_tecla()
            case 3:
                agenda.limpiar_pantalla()
                agenda.buscar_contactos(agenda_contactos)
                agenda.esperar_tecla()
            case 4:
                agenda.limpiar_pantalla()
                print("Terminaste la ejecución del SW")
                opcion = False
            case 5:
                pass
            case 6:
                pass
            case _:
                pass

main()