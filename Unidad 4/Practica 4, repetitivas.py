#Ejercicio 1

for i in range(1, 101):
    print(i)

#Ejercicio 2

numero = (input("Ingrese un número: "))

cantidad = len(numero)

print("El número tiene ", cantidad , " de digitos.")

#ejercicio 3

num1= int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))
max_num = float('-inf')
min_num = float('inf')
suma = 0

if num1 > num2: #El programa determina cual numero es mayor y designa asi un mayor y un menor
    max_num = num1
    min_num = num2 
elif num2 > num1:
    max_num = num2 
    min_num = num1
" "
for i in range (min_num+1, max_num): #Es una sucesion de los pasos

    suma += i

print(suma)

#Ejercicio 4

sum = 0
ERROR = 0
num = int(input(print("Ingrese un numero: ")))

while num != ERROR:
    
    sum += num
    print(sum)

    num = int(input(print("Ingrese otro numero o toque 0 para finalizar: ")))

print("Gracias por participar")

#Ejercicio 5

import random
intentos = 0

print("Bienvenido a la ruleta rusa, intentaremos adivinar un numero del 0 al 9")
num = int(input(print("Por favor, ingrese un numero: ")))

while num != random.randrange(0,9):
    print("Lo siento, intenta de vuelta")
    intentos += 1
    num = int(input(print("Por favor, ingrese un numero: ")))

print ("felicidades, solo te tomo ", intentos, " intentos conseguirlo")

#Ejercicio 6

for i in range(100, -1, -1):
    print(i)

#Ejercicio 7

