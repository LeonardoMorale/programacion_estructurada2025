import os

peliculas=[]

def borrarPantalla():
  os.system("cls")

def esperarTecla():
  print("Oprima cualquier tecla para continuar ...")
  input()  

def agregarPeliculas():
  borrarPantalla()
  print(".:: Alta de Peliculas ::. ")
  peliculas.append(input("Ingresa el nombre: ").upper().strip())
  input("La operacion se realizó con exito")

def consultarPeliculas():
  borrarPantalla()
  print(".:: Consultar Peliculas ::.")
  if len(peliculas)>0:
    for i in range(0,len(peliculas)):
        print(f"{i+1}: {peliculas[i]}")
  else:
    print("No hay peliculas")
  esperarTecla()

def vaciarPeliculas():
    borrarPantalla()
    print("Borrar todas las peliculas del sistema")
    resp=input("Deseas borrar todas las peliculas?").upper
    if resp == "SI":
       peliculas.clear()
       input("La operacion se realizó con exito")

def buscarPeliculas():
    borrarPantalla()
    print("Buscar peliculas")
    pelicula_buscar=input("Ingrese el nombre de la pelicula\n").upper().strip()
    encontro=0
    if not (pelicula_buscar in peliculas):
       print("No se encuentra la pelicula a buscar")

    else:
        for i in range(0,len(peliculas)):
          if pelicula_buscar == peliculas[i]:
            print(f"La pelicula {pelicula_buscar} si la tenemos y esta en la casilla {i}")
            encontro+=1        
        
        print(f"Tenemos {encontro} pelicula(s) con este titulo")
        
    esperarTecla()

def eliminar_peliculas():
   borrarPantalla()
   print(".::Borrar películas::.")
   pelicula_a_borrar = input("Ingrese el nombre de la película que desea buscar: ")
   opc = True
   contador = 0
   while opc:
    for i in range(0, len(peliculas)):
        if pelicula_a_borrar in peliculas[i]:
            respusta = input(print("¿Deseas quitar o borrar la película del sistema (SI/NO) "))
            if respusta =="SI":
                del peliculas[i]
                print(f"La película que se borro es: {peliculas[i]} y estaba en la casilla {i}")
                print()
                print(":::LA OPERACIÓN SE REALIZO CON ÉXITO:::")
                contador+=1
            else:
               opc = False
               print(f"Se borró {contador} película(s) con este título")
               esperarTecla()
