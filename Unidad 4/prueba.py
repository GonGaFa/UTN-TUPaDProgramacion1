#Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. 
# Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

num8 = int(input(print("Ingrese un numero: ")))
num_inverso = 0

while num8 > 0:
    ult_num = num8 % 10       
    num_inverso = num_inverso * 10 + ult_num
    num8 //= 10                 

print("Número invertido:", num_inverso)
