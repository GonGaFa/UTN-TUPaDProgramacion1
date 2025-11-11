#Ejercicio 1

def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()


#Ejercicio 2

def saludar_usuario(nombre):
    print(f"Hola {nombre_usuario}!")

nombre_usuario = input("Introduce tu nombre: ")

saludar_usuario(nombre_usuario)


#Ejercicio 3

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre_usr = input("Introduce tu nombre de pila: ")
apellido_usr = input("Introduce tu primer apellido: ")
edad_usr = input("Introduce tu edad: ")
residencia_usr = input("Introduce tu lugar de residencia: ")

informacion_personal(nombre_usr, apellido_usr, edad_usr, residencia_usr)


#Ejercicio 4

def calcular_area_circulo(radio):
    return 3.14 * (radio ** 2)

def calcular_perimetro_circulo(radio):
    return (3.14 * 2) * radio

radio = float(input("Escribe el radio del círculo: "))

print(f"El área del círculo es {calcular_area_circulo(radio)}")
print(f"El perímetro del círculo es {calcular_perimetro_circulo(radio)}")


#Ejercicio 5

def segundos_a_horas(segundos):
    return segundos/3600

segundos_usr = int(input("Escriba la cantidad de segundos: "))

print(f"{segundos_usr} equivalen a {segundos_a_horas(segundos_usr)} horas")


#Ejercicio 6

def tabla_de_multiplicar(numero):
    for i in range(11):
        producto = i * numero
        print (f"{numero} x {i} = {producto}")

numero_usr = int(input("Escriba el número del que desea saber la tabla de multiplicar: "))

tabla_de_multiplicar(numero_usr)


#Ejercicio 7

def operaciones_basicas(a, b):
    print(f"{a} + {b} es = {a + b}")
    print(f"{a} - {b} es = {a - b}")
    print(f"{a} x {b} es = {a * b}")
    print(f"{a} / {b} es = {a / b}")

numA = int(input("Escribe el primer número: "))
numB = int(input("Escribe el segundo número: "))    

operaciones_basicas(numA, numB)


#Ejercicio 8

def calcular_imc(peso, altura):
    return peso / (altura ** 2) 

altura = float(input("Escribe tu altura expresada en metros (por ejemplo 1.75): "))
peso = float(input("Escribe tu peso expresado en kilogramos (por ejemplo 80): "))

print(f"Tu IMC es {round(calcular_imc(peso, altura),2)}")


#Ejercicio 9

def celsius_a_fahrenheit(celsius):
    return (celsius * (9/5)) + 32

celsius = int(input("Escriba la cantidad de grados celcius que desea convertir a fahrenheit: "))

print(f"{celsius}°C equivalen a {celsius_a_fahrenheit(celsius)}°F")


#Ejercicio 10

def calcular_promedio(a, b, c):
    return (a + b + c) / 3

aNum = int(input("Escriba el primer número: "))
bNum = int(input("Escriba el segundo número: "))
cNum = int(input("Escriba el tercer número: "))

print(f"El promedio entre {aNum}, {bNum} y {cNum} es {round(calcular_promedio(aNum,bNum,cNum),2)}")