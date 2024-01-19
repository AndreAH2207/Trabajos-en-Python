'''
Escribir un programa que permita gestionar la base de datos de clientes de una
empresa. Los clientes se guardarán en un diccionario en el que la clave de cada
cliente será su DNI, y el valor será otro diccionario con los datos del cliente
(nombre, dirección, teléfono, correo, VIP), donde VIP(preferente) tendrá el
valor True si se trata de un cliente VIP.

El programa debe preguntar al usuario por una opción del siguiente menú:
(1) Añadir cliente, 
(2) Eliminar cliente, 
(3) Mostrar cliente,
(4) Listar todos los clientes, 
(5) Listar clientes VIP, 
(6) Terminar.

En función de la opción elegida el programa tendrá que hacer lo siguiente:
Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo
a la base de datos.
Preguntar por el DNI del cliente y eliminar sus datos de la base de datos.
Preguntar por el DNI del cliente y mostrar sus datos.
Mostrar lista de todos los clientes de la base datos con su DNI y nombre.
Mostrar la lista de clientes VIP de la base de datos con su DNI y nombre.
Terminar el programa 

'''

clientes = {}

def ingresarCliente():
    DNI = input("Ingrese DNI: ")
    nombre = input("Ingrese nombre: ")
    direccion = input("Ingrese direccion: ")
    telefono = input("Ingrese telefono: ")
    correo = input("Ingrese Correo: ")
    preferente = input("Ingrese Preferente: ")
    
    cliente = {"nombre": nombre, "direccion": direccion, "telefono": telefono,
               "correo": correo, "preferente": preferente}
               
    clientes[DNI] = cliente

def eliminarCliente(DNI):
    del clientes[DNI]

def mostrarCliente(DNI):
    if DNI in clientes:
        print(clientes[DNI])
    else:
        print("Cliente no encontrado.")

def listarClientes():
    print("*** Listado de Clientes *****")
    for DNI, cliente in clientes.items():
        print("DNI:", DNI)
        for key, value in cliente.items():
            print(key, ":", value)
        print()

def menu():
    while True:
        print("*************************************")
        print("(1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente,"
              "(4) Listar todos los clientes, (5) Listar clientes VIP, (6) Terminar.")
        opcion = int(input("Ingrese opcion:"))

        if opcion == 1:
            ingresarCliente()

        elif opcion == 2:
            DNI = input("Ingrese DNI del cliente a eliminar:")
            eliminarCliente(DNI)

        elif opcion == 3:
            DNI = input("Ingrese DNI del cliente a mostrar:")
            mostrarCliente(DNI)

        elif opcion == 4:
            listarClientes()

        elif opcion == 6:
            break

menu()



