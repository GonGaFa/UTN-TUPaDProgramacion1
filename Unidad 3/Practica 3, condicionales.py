#Ejercicio1

edad1 = int(input("Ingrese su edad "))

if (edad1 >= 18 and edad1 <= 120) :
    print("Eres mayor")
elif (edad1 <= 0 ):
    print("O eres inexistente o recien naciste")
elif (edad1 >= 120):
    print("Me gustaria tener tus genes")
else:
    print("Eres menor")

#Ejercicio 2

nota1 = int(input("ingrese su nota "))

if (nota1>= 6 and nota1 <=10):
    print("Su nota es aprobado")
elif (nota1 >=0 and nota1<6):
    print("Su nota es desaprobado")
else: print("Error al cargar la nota")

#Ejercicio 3

par = int(input("Ingrese un numero: "))

if par%2 == 0:
    print("Su numero es par")
else: print("Por favor ingrese un numero par")

#Ejercicio 4

edad2 = int(input("Ingrese una edad: "))

if (edad2 >= 0 and edad2<=12):
    print("Eres un niño")
elif (edad2 > 12 and edad2 <= 18):
    print("Eres un adolecente")
elif(edad2>= 18 and edad2<=30):
    print("Eres un adulto joven")
elif (edad2>30):
    print("Eres un adulto mayor")
else: print("La edad no es correcta")

#Ejercicio 5

contra = (input("Ingrese una contraseña de 8 a 14 caracteres: "))

if (len(contra)>=8 and len(contra)<=14):
    print("Ha ingresado una contraseña correcta")
else: print("Ingrese una contraseña entre 8 y 14 caracteres")

#Ejercicio 6
from statistics import mode, median, mean

import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

(print(numeros_aleatorios))

if mean(numeros_aleatorios) > median(numeros_aleatorios) and median(numeros_aleatorios) > mode(numeros_aleatorios):
    print("Existe un sesgo positivo")

elif mean(numeros_aleatorios) < median(numeros_aleatorios) and median(numeros_aleatorios) < mode(numeros_aleatorios):
    print("Existe un sesgo negativo")

elif mean(numeros_aleatorios) == median(numeros_aleatorios) and median(numeros_aleatorios) == mode(numeros_aleatorios):
    print("No hay un sesgo")

#Ejercicio 7

palabra = input("Ingrese una palabra: ")

L = palabra[-1].lower()

if L in "aeiou":
    print(palabra, "!")
else:
    print(palabra)

#Ejercicio 8

nombre = input("Ingrese su nombre: ")

opcion = int(input("Ingrese 1 si quiere que su nombre este en mayus, 2 si quiere que su nombre sea en minusculas o 3 si quiere que su nombre empiece con mayuscula"))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())   

#Ejercicio 9

magnitud = float(input("ingrese el tipo de magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve")
elif magnitud >= 3 and magnitud <4:
    print("Leve")
elif magnitud >= 4 and magnitud <5:
    print("Moderado")
elif magnitud >= 5 and magnitud <6:
    print("Fuerte")
elif magnitud >= 6 and magnitud <7:
    print("Muy fuerte")
elif magnitud >= 7:
    print("Extramo")
else: print("Error al procesar la magnitud, pruebe de vuelta")

#Ejercicio 10

