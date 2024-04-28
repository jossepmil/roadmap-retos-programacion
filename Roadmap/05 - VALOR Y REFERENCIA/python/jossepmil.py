"""
Valor y referencia
"""

# Tipos de dato por valor

my_int_a = 10
my_int_b = my_int_a
my_int_b = 20
# my_int_a = 30
print(my_int_a)
print(my_int_b)

# Tipos de dato por referencia

my_list_a = [10, 20]
my_list_b = my_list_a
my_list_b.append(30)
print(my_list_a)
print(my_list_b)

# Funciones con datos por valor


def my_int_func(my_int: int):
    my_int = 20
    print(my_int)


my_int_c = 10
my_int_func(my_int_c)
print(my_int_c)

# Funciones con datos por referencia


def my_list_func(my_list: list):
    my_list.append(30)

    my_list_d = my_list
    my_list_d.append(40)

    print(my_list)
    print(my_list_d)


my_list_c = [10, 20]
my_list_func(my_list_c)
print(my_list_c)

"""
Extra
"""

# Por valor


def value(value_a: int, value_b: int) -> tuple:
    temp = value_a # Temporaria para almacenar el valor de la variable original
    value_a = value_b # Cambiar el valor de la variable original por el del parametro
    value_b = temp # Cambiar el valor de la variable temporal por el del parametro
    return (value_a, value_b)



my_int_d = 10
my_int_e = 20
my_int_f, my_int_g = value(my_int_d, my_int_e)
print(f"{my_int_d}, {my_int_e}")
print(f"{my_int_f}, {my_int_g}")

# Por referencia


def ref(value_a: list, value_b: list) -> tuple:
    temp = value_a
    value_a = value_b 
    value_b = temp 
    value_b.append(50)
    value_a.append(50) 
    return (value_a, value_b)

my_list_e = [10, 20]
my_list_d = [30, 40]
my_list_f, my_list_g = ref(my_list_d, my_list_e)
print(f"{my_list_d}, {my_list_e}")
print(f"{my_list_f}, {my_list_g}")
