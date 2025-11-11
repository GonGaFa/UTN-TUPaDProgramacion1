#Ejercicio 1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)


#Ejercicio 2

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)


#Ejercicio 3

lista_frutas = []

for fruta in precios_frutas:
    lista_frutas.append(fruta)


#Ejercicio 4

contactos = {}

for contacto in range(5):
    contacto = input("Escriba el nombre del contacto ").lower()
    contactos[contacto] = input("Escriba el número del contacto ")


print(contactos[input("Escriba el nombre del contacto que desea consultar su número ").lower()])


#Ejercicio 5

frase = input("Escriba una frase: ").lower()

palabras = frase.split( )

palabras_unicas = set(palabras)

recuento = {}

for palabra in palabras:
    recuento[palabra] = palabras.count(palabra)

print(recuento)


#Ejercicio 6
alumnos = {}

for alumno in range(3):
    alumno = input("Escribe el nombre del alumno ").lower()
    alumnos[alumno] = tuple(float(input(f"Escribe la nota {i + 1} del alumno {alumno}: ")) for i in range(3)) 

for alumno in alumnos:
    print(f"El promedio de {alumno} es {sum(alumnos[alumno]) / len(alumnos[alumno])}")


#Ejercicio 7
parcial_1 = {1,2,3,4,5}
parcial_2 = {1,2,6,7,8,9}

print(f"Ambos parciales: {parcial_1 & parcial_2}")
print(f"Solo uno: {parcial_1 ^ parcial_2 }")
print(f"Al menos uno: {parcial_1 | parcial_2}")


#Ejercicio 8

diccionario = {
    "Manzanas": 15,
    "Bananas": 20,
    "Peras": 29
}

producto_usuario = input("Ingrese el nombre del producto del cual desea realizar una consulta: ")

if producto_usuario in diccionario:
    input_usuario = input(f"El stock del producto ingresado es: {diccionario[producto_usuario]} ¿Desea añadir stock? s/n: ").lower()
    if input_usuario == "s":
        diccionario[producto_usuario] += int(input("Ingrese la cantidad de unidades que desea agregar: "))
    else:
        pass
else:
    input_usuario = input("El producto no existe en la base de datos ¿Desea agregarlo? s/n: ").lower()
    if input_usuario == "s":
        diccionario[producto_usuario] = int(input("Ingrese la cantidad de unidades del producto: "))
    else:
       pass
    

#Ejercicio 9

agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de inglés",
    ("miércoles", "17:00"): "Pilates",
    ("jueves", "20:00"): "Juntada",
    ("viernes", "21:00"): "Asado",
}

dia = input("Ingresa un día que quieras consultar en tu agenda: ").lower()
hora = input("Ingresa el horario en formato 24hs (por ejemplo: 17:00): ")

if (dia, hora) in agenda:
    print(f"El {dia} a las {hora} tenés {agenda[(dia, hora)]}")
else:
    flag = input(f"No tienes nada pactado el {dia} a las {hora}, ¿Deseas agregar un nuevo evento? s/n: ")
    if flag == "s":
        evento = input(f"Escribe el evento que deseas agregar para el {dia} a las {hora}: ")
        agenda[((dia, hora))] = evento
    else:
        pass

print(agenda)



#Ejercicio 10

original = {"Argentina": "Buenos Aires",
            "Chile": "Santiago",
            "España": "Madrid"}

invertido = {}

for clave, valor in original.items():
    invertido[valor] = clave

print(invertido)