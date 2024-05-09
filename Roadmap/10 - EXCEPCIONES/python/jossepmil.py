"""ejercicio"""

try:
    print(10/1)
    my_list = [1,2,3]
    print(my_list[4])


except Exception as e:
    print(f"Se ha producido un error:{e} ({type(e).__name__})")


"""extra"""


class StrTypeError(Exception):
    pass


def process_params(parameters: list):

    if len(parameters) < 3:
        raise IndexError()
    elif parameters[1] == 0:
        raise ZeroDivisionError()
    elif type(parameters[2]) == str:
        raise StrTypeError("El tercer elemento no puede ser una cadena de texto.")
    
    print(parameters[2])
    print(parameters[0]/parameters[1])
    print(parameters[2] + 5)
    
try:
    process_params([1,2,3,3])
except IndexError as e:
    print("El numero de la lista debe ser mayor a 2")
except ZeroDivisionError as e:
    print("El numero de la lista debe ser diferente de 0")
except StrTypeError as e:
    print(f"{e}")
except Exception as e:
    print(f"Se ha producido un error inesperado:{e} ({type(e).__name__})")
else:
    print("Todo ha ido bien")
finally:
    print("el programa finaliza")
