import os
import mysql.connector
from mysql.connector import Error

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def esperar_tecla():
    input("Oprima ENTER para continuar: ")

def menu_principal():
    print("\t\t\U0001F4BB ..::: Sistema de Gestión de Agenda de Contactos \U0001F4BB:::..\n")
    print("\t\t\t \U00000031\U000020E3 Crear")
    print("\t\t\t \U00000032\U000020E3 Borrar")
    print("\t\t\t \U00000033\U000020E3 Mostrar")
    print("\t\t\t \U00000034\U000020E3 Modificar")
    print("\t\t\t \U00000035\U000020E3 Buscar")
    print("\t\t\t \U00000036\U000020E3 SALIR\n")
    opcion = int(input("\t\t\t\U0001F449 Elige una opción (1-6): "))
    return opcion

def conectar():
    try:
        conexion = mysql.connector.connect(
        host = "127.0.0.1",
        user = "root",
        password = "",
        database = "bd_agenda"
    )
        return conexion
    except Error as e:
        print(f"El error que sucedió es: {e}")
        return None

def crearContacto():
    limpiar_pantalla()
    conexionBD = conectar()
    if conexionBD != None:
        print("\n\t\t.::Crear Contactos::.")
        nombre = input("Nombre del contacto: ").upper().strip()
        tel = input("Teléfono del contacto: ").upper().strip()
        email = input("E-mail del contacto: ").upper().strip()

        try:
            cursor = conexionBD.cursor()
            sql = "insert into contactos (contacto, teléfono, email) values (%s, %s, %s)"
            val = (nombre, tel, email)

            cursor.execute(sql, val)
            conexionBD.commit()
            print("\n\t\t ::: \u2705 !LA OPERACION SE REALIZO CON EXITO! :::")
        except Error as e:
            print("Error al intentar insertar un registro en la BD")

def mostrarCcontactos():
    limpiar_pantalla()
    conexionBD = conectar()
    if conexionBD != None:
        print("\n\t\t .:: Mostrar Contactos::.")
        cursor = conexionBD.cursor()
        sql = "select * from contactos"
        cursor.execute(sql)
        registros = cursor.fetchall()
        if registros:
            print("\n\t Mostrar contactos")
            print(f"{'ID':<10}{'contacto':<15}{'teléfono':<15}{'email':<15}")
            print(f"-"*50)
            for fila in registros:
                print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}")
                print(f"-"*50)
        else:
            print("\t .:: No hay contactos en el sistema ::.")

def buscarContactos():
    limpiar_pantalla()
    conexionBD = conectar()
    if conexionBD != None:
        print("\n\t\t.::Buscar Contactos::.")
        cursor = conexionBD.cursor()
        nombre = input("Dame el contacto a buscar: ").upper().strip()
        sql = "select * from contactos where contacto=%s"
        val = (nombre,)
        cursor.execute(sql, val)
        registros = cursor.fetchall()
        if registros:
            print("\n\t Buscar contactos")
            print(f"{'ID':<10}{'contacto':<15}{'teléfono':<15}{'email':<15}")
            print(f"-"*50)
            for fila in registros:
                print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}")
                print(f"-"*50)
        else:
            print("\t .:: No hay contactos en el sistema ::.")

def borrarContacto():
    limpiar_pantalla()
    conexionBD = conectar()
    if conexionBD != None:
        print("\n\t\t.::Borrar Contacto::.")
        cursor = conexionBD.cursor()
        nombre = input("Dame el nombre del contacto a borrar: ")
        sql = "Select * from contactos where contacto=%s"
        val = (nombre,)
        cursor.execute(sql, val)
        registros = cursor.fetchall()
        if registros:
            resp = input(f"¿Deseas borrar el contacto: {nombre}? (Si/No): ").lower().strip()
            if resp == "si":
                sql = "delete from contactos where contacto=%s"
                val = (nombre,)
                cursor.execute(sql, val)
                conexionBD.commit()
                print("\n\t\t ::: \u2705 !LA OPERACION SE REALIZO CON EXITO! :::")
        else:
            print("\t .:: No hay contactos en el sistema ::.")

def modificar_contacto():
    limpiar_pantalla()
    conexionBD = conectar()
    if conexionBD != None:
      print("\n\t .:: Modificar Contacto")
      cursor = conexionBD.cursor()
      sql = "select * from contactos"
      cursor.execute(sql)
      registros = cursor.fetchall()
      if registros:
         print("\n\t Modificar contacto")
         print(f"{'ID':<10}{'contacto':<15}{'Teléfono':<15}{'Email':<15}")
         print(f"-"*50)
         for fila in registros:
            print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}")
            print(f"-"*50)
      else:
         print("\t .:: No hay contactos en el sistema ::.")
    id_modificar = input("Por ID seleccione el contacto a modificar: ").upper().strip()
    sql = "select * from contactos where id=%s"
    val = (id_modificar,)
    cursor.execute(sql, val)
    registros = cursor.fetchall()
    if registros:
      resp = input(f"¿Deseas modificar un contacto con id: {id_modificar}? (Si/No): ").lower().strip()
      if resp == "si":
         nombre = input("Nombre del contacto: ")
         h_1 = input("Teléfono: ")
         h_2 = input("E-mail: ")
         sql = "update contactos set contacto=%s, teléfono=%s, email=%s where id=%s"
         val = (nombre, h_1, h_2, id_modificar)
         cursor.execute(sql, val)
         conexionBD.commit()
         print("\n\t\t ::: \u2705 !LA OPERACION SE REALIZO CON EXITO! :::")
