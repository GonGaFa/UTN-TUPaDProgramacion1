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

print("La suma es: ", suma)

#Ejercicio 4

sum = 0
ERROR = 0
num4 = int(input(print("Ingrese un numero: ")))

while num4 != ERROR:
    
    sum += num4
    print(sum)

    num4 = int(input(print("Ingrese otro numero o toque 0 para finalizar: ")))

print("Gracias por participar")

#Ejercicio 5

import random
intentos = 0

print("Bienvenido a la ruleta rusa, intentaremos adivinar un numero del 0 al 9")
num5 = int(input(print("Por favor, ingrese un numero: ")))

while num5 != random.randrange(0,9):
    print("Lo siento, intenta de vuelta")
    intentos += 1
    num5 = int(input(print("Por favor, ingrese un numero: ")))

print ("felicidades, solo te tomo ", intentos, " intentos conseguirlo")

#Ejercicio 6

for i in range(100, -1, -1):
    print(i)

#Ejercicio 7

num3 = int(input("Ingrese un numero: "))
suma1 = 0
min_num1 = 0
if 0 > num3: #El programa determina cual numero es mayor y designa asi un mayor y un menor
    print("Usted ha elegido un numero no positivo, elija otro por favor")

elif num2 > 0:
    max_num1 = num3
    min_num1 = 0
    
for i in range (min_num1, max_num1): #Es una sucesion de los pasos

    suma1 += i

print(suma1)

#Ejercicio 8

num_impar = 0
num_par = 0
contador = 0
num6 = int(input(print("Ingrese un numero")))

while contador != 10: #Cambiar el diferencial de contador a 100

    if num6 % 2 == 0:
        num_par += 1
    elif num6 % 2 != 0:
        num_impar += 1
    contador += 1
    num6 = int(input(print("Ingrese otro numero: ")))

print ("La cantidad de numero pares ingresados es de ", num_par, ". La cantidad de numeros impares es de ", num_impar)


#Ejercicio 9

contador = 0
num7 =int(input(print("Ingrese un numero")))
media = 0
suma = 0
while contador != 5: #Cambiar diferencual a 100

    suma += num7
    num7 = int(input(print("Ingrese otro numero: ")))
    contador += 1

media = suma/contador

print ("La cantidad de numero pares ingresados es de la media entre los numeros es de ", media)

#Ejercicio 10

num8 = int(input(print("Ingrese un numero: ")))
num_inverso = 0

while num8 > 0:
    ult_num = num8 % 10       
    num_inverso = num_inverso * 10 + ult_num
    num8 //= 10                 

print("Número invertido:", num_inverso)
