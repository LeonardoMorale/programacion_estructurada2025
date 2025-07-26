import mysql.connector
from mysql.connector import Error

#peliculas=[]

#dict u objeto para almacenar los atributos (nombre, categoria, clasificacion, género, idioma)

#peliculas={
#          "nombre":"",
#          "categoria":"",
#          "clasificacion":"",
#          "genero":"",
#          "idioma":""
#}

pelicula={}

def borrarPantalla():
  import os  
  os.system("cls")

def esperarTecla():
  input("Oprima cualquier tecla para continuar ...")  

def conectar():
  try:
      conexion = mysql.connector.connect(
      host = "127.0.0.1",
      user = "root",
      password = "",
      database = "bd_peliculas"
    )
      return conexion
  except Error as e:
    print(f"El error que sucedió es: {e}")
    return None

def crearPeliculas():
  borrarPantalla()
  conexionBD = conectar()
  if conexionBD != None:
    print("\n\t.:: Alta de Peliculas ::. \n")
    pelicula.update({"nombre":input("Ingresa el nombre: ").upper().strip()})
    pelicula.update({"categoria":input("Ingresa el categoria: ").upper().strip()})
    pelicula.update({"clasificacion":input("Ingresa el clasificacion: ").upper().strip()})
    pelicula.update({"genero":input("Ingresa el genero: ").upper().strip()})
    pelicula.update({"idioma":input("Ingresa el idioma: ").upper().strip()})


    ###### Agregar Registro a la BD ######
    try: 
      cursor = conexionBD.cursor()

      sql = "insert into peliculas (nombre, categoria, clasificacion, genero, idioma) values (%s, %s, %s, %s, %s)"
      val = (pelicula['nombre'], pelicula['categoria'], pelicula['clasificacion'], pelicula['genero'], pelicula['idioma'])

      cursor.execute(sql, val)
      conexionBD.commit()
      print("\n\t\t ::: \u2705 !LA OPERACION SE REALIZO CON EXITO! :::")
    except Error as e:
      print("Error al intentar insertar un registro en la BD")

def mostrarPeliculas():
  borrarPantalla()
  conexionBD = conectar()
  if conexionBD != None:
    print("\n\t.:: Consulta o Mostrar la pelicula ")
    cursor = conexionBD.cursor()
    sql = "SELECT * FROM peliculas"
    cursor.execute(sql)
    registros = cursor.fetchall()
    if registros:
      print("\n\tMostrar peliculas")
      print(f"{'ID':<10}{'nombre':<15}{'categoria':<15}{'clasificacion':<15}{'genero':<15}{'idioma':<15}")
      print(f"-"*80)
      for fila in registros:
        print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}{fila[5]:<15}")
        print(f"-"*80)
    else:
      print("\t .:: No hay peliculas en el sistema ::.")

def buscarPeliculas():
  borrarPantalla()
  conexionBD = conectar()
  if conexionBD != None:
    print("\n\t.:: Buscar una pelicula ")
    cursor = conexionBD.cursor()
    nombre = input("Dame el nombre de la pelicula a buscar: ").upper().strip()
    sql = "SELECT * from peliculas where nombre=%s"
    val = (nombre,)
    cursor.execute(sql, val)
    registros = cursor.fetchall()
    if registros:
      print("\n\tMostrar peliculas")
      print(f"{'ID':<10}{'nombre':<15}{'categoria':<15}{'clasificacion':<15}{'genero':<15}{'idioma':<15}")
      print(f"-"*80)
      for fila in registros:
        print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}{fila[5]:<15}")
        print(f"-"*80)
    else:
      print("\t .:: No hay peliculas en el sistema ::.")

def borrarPeliculas():
  borrarPantalla()
  conexionBD = conectar()
  if conexionBD != None:
    print("\n\t.:: Borrar una pelicula ")
    cursor = conexionBD.cursor()
    nombre = input("Dame el nombre de la pelicula a borrar: ").upper().strip()
    sql = "SELECT * from peliculas where nombre=%s"
    val = (nombre,)
    cursor.execute(sql, val)
    registros = cursor.fetchall()
    if registros:
      resp = input(f"¿Deseas borrar la pelicula de {nombre}? (Si/No): ").lower().strip()
      if resp == "si":
        sql = "delete from peliculas where nombre=%s"
        val = (nombre,)
        cursor.execute(sql, val)
        conexionBD.commit()
        print("\n\t\t ::: \u2705 !LA OPERACION SE REALIZO CON EXITO! :::")
    else:
      print("\t .:: No hay peliculas en el sistema ::.")

def modificarPeliculas():
  borrarPantalla()
  conexionBD = conectar()
  if conexionBD != None:
    print("\n\t.:: Modificar una pelicula ")
    cursor = conexionBD.cursor()
    nombre = input("Dame el nombre de la pelicula a modificar: ").upper().strip()
    sql = "SELECT * from peliculas where nombre=%s"
    val = (nombre,)
    cursor.execute(sql, val)
    registros = cursor.fetchall()
    if registros:
      resp = input(f"¿Deseas modificar la pelicula {nombre}? (Si/No): ").lower().strip()
      if resp == "si":
        pelicula['nombre'] = input("Ingresa el nombre: ").upper().strip()
        pelicula['categoria'] = input("Ingresa el categoria: ").upper().strip()
        pelicula['clasificacion'] = input("Ingresa el clasificacion: ").upper().strip()
        pelicula['genero'] = input("Ingresa el genero: ").upper().strip()
        pelicula['idioma'] = input("Ingresa el idioma: ").upper().strip()
        sql = "update peliculas set nombre=%s, categoria=%s, clasificacion=%s, genero=%s, idioma=%s where nombre=%s"
        val = (pelicula["nombre"], pelicula["categoria"], pelicula["clasificacion"], pelicula["genero"], pelicula["idioma"], nombre)
        cursor.execute(sql, val)
        conexionBD.commit()
        print("\n\t\t ::: \u2705 !LA OPERACION SE REALIZO CON EXITO! :::")
    else:
      print("\t .:: No hay peliculas en el sistema ::.")

#def consultarPeliculas():
#  borrarPantalla()
#  print("\n\t.:: Consultar Peliculas ::.")
#  if len(peliculas)>0:
#      for i in range(0,len(peliculas)):
#        print(f"{i+1}.- {peliculas[i]}")
#  else:
#    print("\t ..:: NO HAY PELICULAS EN EL SISTEMA ::.")

#def vaciarPeliculas():
#  borrarPantalla()
#  print("\n\t .:: Borrar o quitar TODAS las peliculas ::.")
#  resp=input("¿Deseas quitar o borrar TODAS las peliculas del sistema? (Si/No)").lower()
#  if resp=="si":
#    peliculas.clear()
#    input("\n\t\t ::: !LA OPERACION SE REALIZO CON EXITO! :::")

#def buscarPeliculas():
#  borrarPantalla()
#  print("\n\t .:: Buscar peliculas ::.")
#  pelicula_buscar=input("Ingrese el nombre de la pelicula a buscar: ").upper().strip()
#  encontro=0
#  if not(pelicula_buscar in peliculas):
#    print("\n\t\t ¡No se encuentra la pelicula a buscar!")
#  else:
#    for i in range(0,len(peliculas)):
#      if pelicula_buscar==peliculas[i]:
#        print(f"La película {pelicula_buscar} si la tenemos y esta en la casilla: {i+1}")
#        encontro+=1
#    if encontro>0:
#      print(f"\n Tenemos {encontro} pelicula(s) con este titulo")
#      input("\n\t\t ::: !LA OPERACION SE REALIZO CON EXITO! :::")

#def eliminarPeliculas():
#   borrarPantalla()
#   print("\n\t.:: Borrar Películas ::.\n")
#   pelicula_buscar=input("Ingrese el nombre de la pelicula que desea buscar: ").upper().strip()
#   encontro=0
#   if not(pelicula_buscar in peliculas): 
#      print("\n\t\t ¡No se encuentra la pelicula a buscar!")   
#   else: 
#      resp="si"  
#      while pelicula_buscar in peliculas and resp=="si":
#          resp=input("¿Deseas quitar o borrar la pelicula del sistema (Si/No)?").lower()
#          if resp=="si":
#            posicion=peliculas.index(pelicula_buscar)
#            print(f"\nLa pelicula que se borro es: {pelicula_buscar} y estaba en la casilla: {posicion+1}")
#            peliculas.remove(pelicula_buscar) 
#            encontro+=1
#            print("\n\t\t::: ¡LA OPERACION SE REALIZO CON ÉXITO! :::")
#      print(f"Se borro {encontro} pelicula(s) con este titulo")


