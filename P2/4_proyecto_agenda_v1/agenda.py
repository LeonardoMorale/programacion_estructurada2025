import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def esperar_tecla():
    input("Oprima ENTER para continuar: ")

def menu_principal():
    print("\t\t\U0001F4BB ..::: Sistema de Gestión de Agenda de Contactos \U0001F4BB:::..\n")
    print("\t\t\t \U00000031\U000020E3 Agregar contacto")
    print("\t\t\t \U00000032\U000020E3 Mostrar todos los contactos")
    print("\t\t\t \U00000033\U000020E3 Buscar contacto por nombre")
    print("\t\t\t \U00000034\U000020E3 Modificar contacto")
    print("\t\t\t \U00000035\U000020E3 Eliminar contacto")
    print("\t\t\t \U00000036\U000020E3 SALIR\n")
    opcion = int(input("\t\t\t\U0001F449 Elige una opción (1-6): "))
    return opcion

def agregar_contacto(agenda):
    print("\n\t\t.::Agregar Contactos::.")
    nombre = input("Nombre del contacto: ").upper().strip()
    if nombre in agenda:
        print("\n\t\t El contacto ya existe")
    else:
        tel = input("Teléfono: ").strip()
        email = input("E-mail: ").lower().strip()
        # Agregar el atributo "nombre" al diccionario con los valores de tel y email en una lista
        agenda[nombre] = [tel, email]
        print("\n\t\tAcción realizada con éxito")

def mostrar_contactos(agenda):
    print("\n\t\t .:: Mostrar Contactos::.")
    if not agenda:
        print("\n\t\t No existen contáctos en la Agenda ...")
    else:
        for nombre, datos in agenda.items():
            print(f"\n\t{'Nombre: '}{nombre}\n\t\t{'Teléfono: '}{datos[0]}\n\t\t{'E-mail: '}{datos[1]}")

def buscar_contactos(agenda):
    print("\n\t\t.::Buscar Contactos::.")
    if not agenda:
        print("\n\t\t No existen contactos en la Agenda ...")
        return

    nombre = input("Nombre del contacto a buscar: ").upper().strip()
    if nombre in agenda:
        datos = agenda[nombre]
        print(f"\n\t{'Nombre: '}{nombre}\n\t\t{'Teléfono: '}{datos[0]}\n\t\t{'E-mail: '}{datos[1]}")
    else:
        print(f"\n\t\t El contacto '{nombre}' no se encontró.")

def modificar_contacto(agenda):
    print("\n\t\t.::Modificar Contacto::.")
    if not agenda:
        print("\n\t\t No existen contactos en la Agenda para modificar...")
        return

    nombre = input("Nombre del contacto a modificar: ").upper().strip()
    if nombre in agenda:
        print(f"\n\t\tModificando contacto: {nombre}")
        nuevo_tel = input("Nuevo teléfono (dejar en blanco para no cambiar): ").strip()
        nuevo_email = input("Nuevo E-mail (dejar en blanco para no cambiar): ").lower().strip()

        if nuevo_tel:
            agenda[nombre][0] = nuevo_tel
        if nuevo_email:
            agenda[nombre][1] = nuevo_email
        print("\n\t\tContacto modificado con éxito.")
    else:
        print(f"\n\t\t El contacto '{nombre}' no se encontró.")

def eliminar_contacto(agenda):
    print("\n\t\t.::Eliminar Contacto::.")
    if not agenda:
        print("\n\t\t No existen contactos en la Agenda para eliminar...")
        return

    nombre = input("Nombre del contacto a eliminar: ").upper().strip()
    if nombre in agenda:
        confirmacion = input(f"¿Estás seguro de que quieres eliminar a '{nombre}'? (s/n): ").lower().strip()
        if confirmacion == 's':
            del agenda[nombre]
            print("\n\t\tContacto eliminado con éxito.")
        else:
            print("\n\t\tEliminación cancelada.")
    else:
        print(f"\n\t\t El contacto '{nombre}' no se encontró.")

