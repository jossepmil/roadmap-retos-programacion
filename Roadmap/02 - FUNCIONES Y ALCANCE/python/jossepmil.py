"""
Funicones definidas por usuario
"""

#funcion simple
def funciones():
    print("Hola python")

funciones()

#funciones con retorno

def return_funciones():
    return "hola"

print(return_funciones())

#funciones con argunmeto
def arg_funcion(nombre):
    print("Hola "+ nombre)

arg_funcion("Leon")


#funciones con numeros variables de argumentos
def varios_argumentos(*nombres):
    for nombre in nombres:
        print(f"Hola , {nombre}!")

varios_argumentos("Emiliano","Juan","anita")

#funcion con un diccionario como parametro
def diccionario(**nombres2):
    for key, value in nombres2.items():
        print(f"Hola , {key} tiene {value}")

diccionario(
    lenguaje="python",
    nombre="Emiliano",
    alias="jossepmil",
    edad=18
 )

#funcion dentro de funcion

def outer_function():
    def inner_function():
        print("funcion interna: Hola desde la funcion interna")
    inner_function()

outer_function()

#funciones de lenguajes (built-in)
print(len("hola"))
print(type(1))
print("Emiliano".upper())

"""
varialbes locales y globales
"""
global_var = "global Python"

print(global_var)

def hello_python():
    local_var = "Hola desde la funcion local"
    print(f"{local_var}, {global_var}")

hello_python()

"""
extra
"""
def print_number(text_1, text_2) -> int:
    count = 0
    for number in range(1,101):
        if number % 3 == 0 and number % 5 == 0:
            print(text_1 + text_2)
        elif number % 3 == 0:
            print(text_1)
        elif number % 5 == 0:
            print(text_2)
        else:
            print(number)
            count += 1
    return count

"""a función imprime todos los números del 1 al 100. Teniendo en cuenta que: """


print(print_number("Fizz", "Buzz"))
