num3 = int(input(print("Ingrese un numero: ")))
suma1 = 0
min_num1 = 0

if 0 > num3: #El programa determina cual numero es mayor y designa asi un mayor y un menor
    print("Usted ha elegido un numero no positivo, elija otro por favor")

elif num3 > 0:
    max_num1 = num3
    min_num1 = 0
    
for i in range (min_num1, max_num1): #Es una sucesion de los pasos

    suma1 += i

print(suma1)
