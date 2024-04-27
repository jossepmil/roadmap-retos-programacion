#cadenas de caracteres
s1 = "hola"
s2 = "Python"
s3 = "Emiliano Tejo"
#concatenacion
print(s1 + ", " + s2 + "!")

#repeticion
print(s1 * 3)

#Indexacion
print(s1[0]) #primer caracter

#Longitud de la cadena
print(len(s1))

#Reemplazar caracteres
print(s1.replace("hola", "adios"))

#Eliminar caracteres
print(s1.strip())

#Convertir a mayusculas
print(s1.upper())
print(s3.title())

#Convertir a minusculas
print(s1.lower())

#Comparacion de cadenas
print("Python" > "Java") #True

#slicing
print(s1[0:3]) #primer caracter hasta el tercer caracter
print(s1[:4]) #primer caracter hasta el cuarto caracter
print(s1[2:]) #segundo caracter hasta la longitud de la cadena

#buscar caracteres en una cadena
print("Python".find("o")) #devuelve el indice del primer caracter "o"
print("ho" in s1) #True
print("hr" in s2) #False

#Reemplazar caracteres
print(s1.replace("o", "a"))

#division de cadenas
print(s2.split("t"))#devuelve una lista con los elementos separados por el caracter "t"

#concatenar listas
lista = [1, 2, 3]
print(lista + [9]) #devuelve la lista de numeros y un numero

#eliminar espacios de una cadena
print("   hola    ".strip())

#busqueda al principio
print("hola".startswith("h"))

#busqueda al final
print(s1.endswith("a"))

#busquedad de posicion
print(s1.find("o"))
print(s2.index("ho"))
print(s3.rfind("o")) #devuelve el indice del caracter "o" al final
print(s3.rindex("a")) #devuelve el indice del caracter "o" al principio
print(s3.find("Tejo"))
print(s3.lower().find("T"))

#formateo
print("saludo: {}, lenguaje: {}!".format(s1,s2))

#Interpolar
print(f"saludo: {s1}, lenguaje: {s2}!")

#Transformaciones de cadenas
print(list(s3)) #devuelve una lista con los caracteres del string

s4 = [s1, s2, s3, " ", "Emiliano"]
print("-".join(s4)) #devuelve la cadena separada por espacios

#Transformaciones numericas
s5 = "102432432342342"
s5 = int(s5) #transforma el string a un numero entero
print(s5) #transforma el string a un numero entero	

s6 = "102432.432342342"
s6 = float(s6) #transforma el string a un numero decimal
print(s6) #transforma el string a un numero decimal

#Transformaciones booleanas
s7 = "True"
s8 = bool(s7) #transforma el string a un valor booleano
print(s8)

#comparaciones varias
print(s1.isalpha())
print(s2.isdigit())
print(s3.isalnum())
print("nano".isnumeric())

"""desafio"""

def es_palindromo(cadena):
    if cadena == cadena[::-1]:
        return (f"si es palindromo {cadena}")
    else:
        return False

es_palindromo = es_palindromo("radar")#llamada a la funcion
print(es_palindromo)

#anagramas
def anagrama(cadena,cadena2):
    if sorted(cadena) == sorted(cadena2):
        return (f"si son anagramas {cadena} y {cadena2}")
    else:
        return (f"Noooooo son anagramas {cadena} y {cadena2}")

anagrama = anagrama("roma","amor")#llamada a la funcion
print(anagrama)

#isogramas.
def isograma(cadena3):
    if len(cadena3) == len(set(cadena3)):
        return (f"si es un isograma {cadena3}")
    else:
        return (f"Noo es un isograma {cadena3}")
    
isograma = isograma("Ana")#llamada a la funcion
isograma = isograma.lower()
print(isograma)
