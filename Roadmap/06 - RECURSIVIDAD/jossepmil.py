# Recursividad es una funcion que se lla a ella misma

def countdown(number: int):
    if number >= 0:
        print(number)
        return countdown(number - 1)

countdown(100)

print(10)

def factorial(number: int) -> int:
    if number < 0:
        return "Tiene que ser positivo"
    elif number == 0:
        return 1
    else:
        return number * factorial(number - 1)
    
input_number = int(input("Ingrese un numero: "))

print(f"el numero factorial {factorial(input_number)}")

#sucesion de Fibonacci

def fibonacci(number: int) -> int:
    if number < 0:
        print("Tiene que ser mayor que Cero")
        return 0
    elif number <= 2:
        return number - 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)



print(fibonacci(5))
