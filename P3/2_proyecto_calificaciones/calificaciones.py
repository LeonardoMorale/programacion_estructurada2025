import os
import mysql.connector
from mysql.connector import Error

def borrarPantalla(): 
  os.system("cls")

def esperarTecla():
  input("\U0001F552 Oprima cualquier tecla para continuar \U0001F552") 

def menu_principal():
    print("\U0001F4C2 ..::: Sistema de Gestión de Calificaciones :::.. \U0001F4C2\n\t\t  1.-  Crear\n\t\t 2.- Borrar\n\t\t 3.- Mostrar\n\t\t 4.-  Modificar\n\t\t 5.- Buscar\n\t\t 6.- SALIR")
    opcion=input("\n\t\t \U0001F449 Elige una opción (1-6): ")
    return opcion

def conectar():
   try:
         conexion = mysql.connector.connect(
         host = "127.0.0.1",
         user = "root",
         password = "",
         database = "bd_calificaciones"
      )
         return conexion
   except Error as e:
      print(f"El error que sucedió es: {e}")
      return None

def crearCalificaciones():
  borrarPantalla()
  conexionBD = conectar()
  if conexionBD != None:
   print("\U0001F4DD Agregar Calificaciones \U0001F4DD")
   nombre = input("Nombre del Alumno: ").upper().strip()
   cal_1 = input("Calificación #1: ")
   cal_2 = input("Calificación #2: ")
   cal_3 = input("Calificación #3: ")

   try:
      cursor = conexionBD.cursor()

      sql = "insert into calificaciones (alumno, calificacion_1, calificacion_2, calificacion_3) values (%s, %s, %s, %s)"
      val = (nombre, cal_1, cal_2, cal_3)

      cursor.execute(sql, val)
      conexionBD.commit()
      print("\n\t\t ::: \u2705 !LA OPERACIÓN SE REALIZO CON ÉXITO! :::")
   except Error as e:
      print("Error al intentar insertar un registro en la BD")
      
def borrarCalificaciones():
   borrarPantalla()
   conexionBD = conectar()
   if conexionBD != None:
      print("\n\t .:: Borrar Calificaciones")
      cursor = conexionBD.cursor()
      sql = "select * from calificaciones"
      cursor.execute(sql)
      registros = cursor.fetchall()
      if registros:
         print("\n\t Mostrar calificaciones")
         print(f"{'ID':<10}{'nombre':<15}{'Calificación 1':<15}{'Calificación 2':<15}{'Calificación 3':<15}")
         print(f"-"*65)
         for fila in registros:
            print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}")
            print(f"-"*65)
      else:
         print("\t .:: No hay calificaciones en el sistema ::.")
   id_eliminar = input("Por ID seleccione el alumno a eliminar: ").upper().strip()
   sql = "select * from calificaciones where id=%s"
   val = (id_eliminar,)
   cursor.execute(sql, val)
   registros = cursor.fetchall()
   if registros:
      resp = input(f"¿Deseas borrar el alumno con id: {id_eliminar}? (Si/No): ").lower().strip()
      if resp == "si":
         sql = "DELETE FROM calificaciones WHERE calificaciones.id = %s"
         val = (id_eliminar,)
         cursor.execute(sql, val)
         conexionBD.commit()
         print("\n\t\t ::: \u2705 !LA OPERACION SE REALIZO CON EXITO! :::")
   
def mostrarCalificaciones():
   borrarPantalla()
   conexionBD = conectar()
   if conexionBD != None:
      print("\n\t .:: Consulta o Mostrar Calificaciones")
      cursor = conexionBD.cursor()
      sql = "select * from calificaciones"
      cursor.execute(sql)
      registros = cursor.fetchall()
      if registros:
         print("\n\t Mostrar calificaciones")
         print(f"{'ID':<10}{'nombre':<15}{'Calificación 1':<15}{'Calificación 2':<15}{'Calificación 3':<15}")
         print(f"-"*65)
         for fila in registros:
            print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}")
            print(f"-"*65)
      else:
         print("\t .:: No hay calificaciones en el sistema ::.")

def modificarCalificaciones():
   borrarPantalla()
   conexionBD = conectar()
   if conexionBD != None:
      print("\n\t .:: Borrar Calificaciones")
      cursor = conexionBD.cursor()
      sql = "select * from calificaciones"
      cursor.execute(sql)
      registros = cursor.fetchall()
      if registros:
         print("\n\t Mostrar calificaciones")
         print(f"{'ID':<10}{'nombre':<15}{'Calificación 1':<15}{'Calificación 2':<15}{'Calificación 3':<15}")
         print(f"-"*65)
         for fila in registros:
            print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}")
            print(f"-"*65)
      else:
         print("\t .:: No hay calificaciones en el sistema ::.")
   id_modificar = input("Por ID seleccione el alumno a modificar: ").upper().strip()
   sql = "select * from calificaciones where id=%s"
   val = (id_modificar,)
   cursor.execute(sql, val)
   registros = cursor.fetchall()
   if registros:
      resp = input(f"¿Deseas modificar al alumno con id: {id_modificar}? (Si/No): ").lower().strip()
      if resp == "si":
         nombre = input("Nombre del alumno: ")
         cal_1 = input("Calificación 1: ")
         cal_2 = input("Calificación 2: ")
         cal_3 = input("Calificación 3: ")
         sql = "update calificaciones set alumno=%s, calificacion_1=%s, calificacion_2=%s, calificacion_3=%s where id=%s"
         val = (nombre, cal_1, cal_2, cal_3, id_modificar)
         cursor.execute(sql, val)
         conexionBD.commit()
         print("\n\t\t ::: \u2705 !LA OPERACION SE REALIZO CON EXITO! :::")

def buscarCalificaciones():
   borrarPantalla()
   conexionBD = conectar()
   if conexionBD != None:
      print("\n\t .:: Buscar Calificaciones")
      cursor = conexionBD.cursor()
      nombre = input("Dame el nombre del alumno a buscar: ").upper().strip()

      sql = "select * from calificaciones where alumno=%s"
      val = (nombre,)
      cursor.execute(sql, val)
      registros = cursor.fetchall()
      if registros:
         print("\n\t Mostrar calificaciones")
         print(f"{'ID':<10}{'nombre':<15}{'Calificación 1':<15}{'Calificación 2':<15}{'Calificación 3':<15}")
         print(f"-"*65)
         for fila in registros:
            print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}")
            print(f"-"*65)
      else:
         print("\t .:: No hay calificaciones en el sistema ::.")
