
def borrarPantalla():
  import os  
  os.system("cls")

def esperarTecla():
  input("\U0001F552 Oprima cualquier tecla para continuar \U0001F552") 

def menu_principal():
    print("\U0001F4C2 ..::: Sistema de Gestión de Calificaciones :::.. \U0001F4C2\n\t\t  1️⃣  Agregar\n\t\t  2️⃣  Mostrar\n\t\t  3️⃣  Calcular Promedio\n\t\t  5️⃣  SALIR")
    opcion=input("\n\t\t \U0001F449 Elige una opción (1-5): ")
    return opcion

def agregar_calificaciones(lista):
  borrarPantalla()
  print("\U0001F4DD Agregar Calificaciones \U0001F4DD")
  nombre = input("\U0001F464 Nombre del Alumno: ").upper().strip()
  calificaciones = []
  for i in range (1,4):
    continua = True
    while continua:
        try:
            cal = float(input(f"\U0001F58B Calififcación {i}: "))
            if cal >= 0 and cal <= 10:
                calificaciones.append(cal)
                continua = False
            else: 
                print("Ingrese un número valido")
        except ValueError:
            print("Ingresa un valor númerico \U0001F522")
  lista.append([nombre] + calificaciones)
      
def mostrar_calificaciones(lista):
  borrarPantalla()
  print("\U0001F5D2 Mostrar Calificaciones")
  if len(lista)>0:
     print(f"{'\U0001F464 Nombre':<15}{'\U0001F4D2 Calf. 1':<10}{'\U0001F4D5 Calf. 2':<10}{'\U0001F4D7 Calf.3':<10}")
     print(f"{'-'*40}")
     for fila in lista:
        print(f"{fila[0]:<15}{fila[1]:<10}{fila[2]:<10}{fila[3]:<10}")
     print(f"{'-'*40}")
     print(f"")
  else:
     print("\U0001F532 No hay calificaciones registradas en el sisteam")

def calcular_promedios(lista):
  borrarPantalla()
  print("\U0001F9EE Calcular Promedio \U0001F9EE")
  if len(lista) > 0:
     print(f"{'\U0001F464 Alumno':<15}{'\U0001F9EE Promedio':<10}")
     print(f"{'-'*25}")
     promedio_grupal = 0
     for fila in lista:
        nombre = fila[0]
        promedio = sum(fila[1:])/3
        print(f"{nombre:<15}{promedio:.2f}")
        promedio_grupal = promedio_grupal + promedio
     print(f"{'-'*25}")
     promedio_grupal = promedio_grupal / len(lista)
     print(f"\U0001F465 El promedio grupal es: {promedio_grupal}")
  else:
     print("\U0001F532 No hay calificaciones registrados en el sisteam")
