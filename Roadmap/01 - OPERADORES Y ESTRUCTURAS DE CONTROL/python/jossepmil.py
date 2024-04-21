#ejemplos aritmeticos
suma = 2 + 5
resta = 10 - 3
multiplicacion = 4 * 6
division = 8 / 2

print(suma, resta, multiplicacion, division)

if division > 5:
    print("La division es mayor a 5")
else:
    print("La division no es mayor a 5")

if resta > 5:
        print("La resta es mayor a 5")
else:
    print("La resta no es mayor a 5")


if suma > 10:
        print("La suma es mayor a 10")
else:
    print("La suma no es mayor a 10")

if multiplicacion >= 18:
        print("El producto es igual a 18")      


for i in range(10, 56):
    if i % 2 == 0:
        print("El numero es par")
    elif i == 16 or i % 3!= 0:
        print("El numero no es el 16 ni múltiplo de 3")
    else:
        print(i)
