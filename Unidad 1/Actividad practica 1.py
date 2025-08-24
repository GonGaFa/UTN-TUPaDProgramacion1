#Actividad 1

#Ejercicio 1

print("Hola mundo")

#Ejercicio 2

nombre1 = input ("Ingrese un nombre")

print(f"Bienvenido {nombre1}!")

#Ejercicio 3

nombre2 = input("Ingrese su nombre")
apellido = input("Ingrese su apellido")
edad = int(input("Ingrese su edad"))
residencia = input("Ingrese su lugar de residencia")

print(f"Hola, me llamo {nombre2} {apellido}, tengo {edad}, soy de {residencia}")

#Ejercicio 4

radio = float(input("Ingrese el radio del circulo"))

diametro = float(radio**2)

perimetro = float(diametro* 3.14)

print(f"El radio ingresado tiene {diametro} de diametro y {perimetro} de perimetro")

#Ejercicio 5

segundos = float(input("Ingrese la cantidad de segundo"))

hora = float(segundos/60)

print(f"La hora es {hora}")

#Ejericicio 6

num1 = int(input("Ingrese un numero"))

prim = int(num1*1)
segu = int(num1*2)
ter = int(num1*3)
cuar = int(num1*4)
quin = int(num1*5)
sext = int(num1*6)
sep = int(num1*7)
oct = int(num1*8)
nov = int(num1*9)
deci = int(num1*10)

print(f"La tabla del numero es la siguiente x1= {prim}, x2= {segu}, x3= {ter}, x4= {cuar}, x5= {quin}, x7= {sext}, x8= {sep=}, x9= {nov}, x10= {deci}")

#Ejericio 7

num2 = int(input("Ingrese un numero"))
num3 = int(input("Ingrese otro numero"))
multi1 = int(num2*num3)
div1 = float(num2/num3)
sum1 = int(num2+num3)
rest1 = int(num2-num3)

print(f"La suma de los numero es {sum1}, la resta es {rest1}, la multiplicacion es {multi1} y la division es {div1}")


#Ejercicio 8

altura = int(input("Ingrese su altura"))
peso = int(input("Ingrese su peso"))

imc = float(altura/(peso**2))

print(f"Su IMC es igual a {imc}")

#Ejercicio 9

cel = float(input("Ingrese la temperatura en celcius"))
far = float(((9/5)*cel) + 32)

print(f"La temperatura en Farenheint es de {far}")

#Ejercicio10

num4 = int(input("Ingrese un numero"))
num5 = int(input("Ingrese un segundo numero"))
num6 = int(input("Ingrese el ultimo"))

prom = (num4+num5+num6)/3

print(f"El promero de los 3 numeros es de {prom}")