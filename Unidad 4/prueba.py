#Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario

num2 = int(input("Ingrese un numero: "))
suma = 0

if 0 > num2: #El programa determina cual numero es mayor y designa asi un mayor y un menor
    max_num = 0
    min_num = num2 
elif num2 > 0:
    max_num = num2 
    min_num = 0
" "
for i in range (min_num, max_num): #Es una sucesion de los pasos

    suma += i

print(suma)