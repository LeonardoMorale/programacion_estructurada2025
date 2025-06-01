import modulos

modulos.borrarPantalla()

# 1er utilizar los modulos

print(modulos.saludar("Leonardo"))

# 2nda forma de utilizar modulos

from modulos import saludar, borrarPantalla

borrarPantalla()
print(saludar("Daniel Contreras Renecio"))

nombre = input("Ingrese el nombre del contacto")
telefono = input("Ingrese su número de teléfono con clave lada: ")

nom, tel = modulos.solicitarDatos4(nombre, telefono)
print(f"\tNombre Completo: {nom} teléfono: {tel}")
