from paquete1 import modulos

print(modulos.saludar("Daniel Contreras Ruano"))

modulos.borrarPantalla()
nom, tel = modulos.solicitardatos2()
print(f"\n\t.:: Agenda Telefonica::.\n\tNombre: {nom}\n\tTelefono: {tel}")

modulos.esperarTecla()