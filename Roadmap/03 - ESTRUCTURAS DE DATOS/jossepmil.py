
#Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.

#listas sirve para guardar datos y ordenarlos
my_list = ["brais","Black","Visionos","wolfy"]
print(my_list)
my_list.append("jossepmil") #insercion de un elemento en la lista
print(my_list)
my_list.remove("Visionos") #eliminacion de un elemento de la lista
print(my_list)
my_list[1] = "Cuervillo"
print(my_list)
my_list.sort() #ordenamiento de la lista
print(my_list)
my_list.reverse() #inversión de la lista
print(my_list)
my_list.pop() #eliminar el último elemento de la lista
print(my_list)
my_list.clear() #limpiar la lista
print(my_list)
my_list = ["brais","Black","Visionos","wolfy"]
my_list.insert(1,"Cuervillo") #insercion de un elemento en la posición indicada
print(my_list)

#tuplas sirve para guardar datos y ordenarlos
my_tuplas = ("Brais","Black","Visionos","wolfy","Jossepmil","25")	
print(my_tuplas[1]) #accesor a un elemento de la tupla
print(my_tuplas[3])
print(my_tuplas[2])
print(my_tuplas[4])
my_tuplas = tuple(sorted(my_tuplas)) #ordenamiento de la tupla
print(my_tuplas)
print(type(my_tuplas))

#sets sirve para guardar datos y eliminar duplicados, es una estructura desronedad
my_set = {"Brais","Black","Visionos","wolfy","Jossepmil","25"}	
print(my_set)
print(type(my_set))
#insercion de un elemento en la posición indicada
my_set.add("jossepmil@gmail.com") #insercion de un elemento en la posición indicada
my_set.add("jossepmil@icloud.com") #insercion de un elemento en la posición indicada
my_set.add("jossepmil@gmail.com") #insercion de un elemento en la posición indicada
print(my_set)
my_set.remove("Jossepmil") #eliminar el ultimo elemento
print(my_set)
my_set = set(sorted(my_set))
print(my_set)

#diccionarios sirve para guardar datos y ordenarlos
my_dict: dict = {
    "name":"Emiliano",
    "surname":"Tejo",
    "alias":"@jossepmil",
    "age":38,
  }

print(my_dict["name"]) #accesor a un elemento de la tupla
print(my_dict["alias"])
print(my_dict.keys()) #accesor a los elementos de la tupla
print(my_dict.values()) #accesor a los valores de la tupla
print(my_dict)
my_dict["mail"]="jossepmil@gmail.com" #insercion de un elemento en la posición indicada
print(my_dict)
my_dict = sorted(my_dict.items()) #ordenar los elementos del diccionario
print(my_dict)
print(type(my_dict))

"""extra agenda"""

def my_agenda(): #funcion para crear una agenda

    agenda = {} #creacion de un diccionario vacio

    while True: #ciclo infinito

        print("") #limpiar la pantalla
        print("1. Buscar contacto por nombre.")
        print("2. Insertar contacto.")
        print("3. Actualizar contacto.")
        print("4. Eliminar contacto.")
        print("5. Salir.")

        option = input("\nselecciona una opcion: ") #

        match option:
            case "1":
                name = input("\nIngresa el nombre a buscar: ")
                if name in agenda:
                    print(f"El numero del telefono de {name} es {agenda[name]}.")
                else:
                    print(f"El contacto {name} no se encuentra en la agenda.")
            case "2":
                name = input("\nIngresa el nombre: ")
                phone = input("\nIngresa el telefono: ")
                if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
                    agenda[name] = phone #insercion de un elemento en la posición indicada
                else:
                    print("El telefono debe ser numerico y tener 11 digitos.")
                agenda[name] = phone
            case "3":
                name = input("\nIngresa el nombre a actualizar: ")
                if name in agenda:
                    phone = input("\nIngresa el nuevo telefono: ")
                    if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
                        agenda[name] = phone
                        print(f"Se actualizó el telefono de {name} con éxito.")
                    else:
                        print("El telefono debe ser numerico y tener 11 digitos.")
            case "4":
                name = input("\nIngresa el nombre a eliminar: ")
                if name in agenda:
                    del agenda[name]
                else:
                    print(f"El contacto {name} no se encuentra en la agenda.")
            case "5":
                print("Saliendo de la agenda")
                brake #salir del ciclo while
            case _:
                print("opcion no valida. Elige ina opcion del 1 al 5.")


my_agenda()
