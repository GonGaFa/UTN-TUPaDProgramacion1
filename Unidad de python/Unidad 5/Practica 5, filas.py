#Ejercicio 1

notas = [2,5,10,6,4,7,4,5,2,1]

print("Las notas son: ", notas)

promedio = sum(notas)/len(notas)
print("El promedio es: ", promedio)

#Ejercicio 2

elementos = []

for i in range(5):
    elemento = input("Ingrese una palabra: ")
    while not elemento.isalpha() or elemento in elementos: #Calcula que solo sean letras y no sean repetidas
        print("Usted no ingresó una palabra o la palabra ya se introdujo, intente nuevamente.")
        elemento = input("Ingrese una palabra: ")

    elementos.append(elemento)

print(sorted(elementos)) #Acomoda la lista alfabeticamente

delete = input("¿Desea eliminar algun producto? (Si/No): ").upper()

if delete == "SI":
    print(sorted(elementos))
    producto = input("Ingrese el nombre del producto a eliminar: " )
    elementos.remove(producto)
    
    print("La lista actualizada es: ", elementos)
else:
    print("Perfecto entonces, que tenga un muy buen dia")

contador = []
word = str(input("Ingrese una palabra:"))
contador.append(word)


while len(contador) < 5:
    word = str(input("Ingrese otra palabra:"))
    contador.append(word)

contador.sort()

print(contador)

borra = input("Desea eliminar una palabra? (Si/No): ").upper()

if borra == "SI":
    num_borrado = str(input("Que palabra desea borrar?: "))
    if num_borrado in contador:
        contador.remove(num_borrado)
        print("Palabra borrada", contador)
    else: print("Ese dato no esta en la lista") 
elif borra == "NO":
    print(contador)

#Ejercicio 3

import random

aleatorios = [random.randint(1,100) for _ in range(15)]
print("Números aleatorios: ", aleatorios)
pares = [num for num in aleatorios if num % 2 == 0]
impares = [num for num in aleatorios if num % 2 != 0]
print("Los numeros pares son: ", pares)
print("Y los impares: ", impares)


#Ejercicio 4

datos = [1,3,5,3,7,1,9,5,3]

elim_repe = list(set(datos))

print("La lista quedo asi:",sorted(elim_repe))

#Ejercicio 5

nombres=["Ana","Luis","Carlos","Marta","Lucia","Jorge","Sofia","Diego"]

print("Los nombres son: ", nombres)
input(print("Si deseas agregar un nombre, ingresa 'Agregar', de lo contrario, si deseas quitar alguno ingresa 'remover': "))
if str == "Agregar":
    persona = input("Ingresa el nombre que deseas agregar: ")
    nombres.append(persona)
elif str == "remover":
    persona = input("Ingresa el nombre que deseas eliminar: ")
    nombres.remove(persona)

print("Los nombres son: ", nombres)

#Ejercicio 6

numeros = [1, 2, 3, 4, 5, 6, 7]

numeros = [numeros[-1]] + numeros[:-1]

print(numeros)

#Ejercicio 7

temperaturas = [
    [12, 25],  # Lunes
    [14, 28],  # Martes
    [11, 24],  # Miércoles
    [13, 27],  # Jueves
    [10, 22],  # Viernes
    [15, 30],  # Sábado
    [9, 20]    # Domingo
]

suma_min = sum(dia[0] for dia in temperaturas)
suma_max = sum(dia[1] for dia in temperaturas)

prom_min = suma_min / 7
prom_max = suma_max / 7

amplitudes = [dia[1] - dia[0] for dia in temperaturas]
mayor_amplitud = max(amplitudes)
dia_mayor_amplitud = amplitudes.index(mayor_amplitud) + 1  # +1 porque los días empiezan en 1

# Mostrar resultados
print(f"Promedio de mínimas: {prom_min:.2f}°C")
print(f"Promedio de máximas: {prom_max:.2f}°C")
print(f"Mayor amplitud térmica: {mayor_amplitud}°C (Día {dia_mayor_amplitud})")

#Ejercicio 8

notas = [
    [7, 8, 6],  # Estudiante 1
    [5, 9, 7],  # Estudiante 2
    [8, 6, 9],  # Estudiante 3
    [6, 7, 5],  # Estudiante 4
    [9, 8, 10]  # Estudiante 5
]

print("Promedio por estudiante:")
for i, fila in enumerate(notas, start=1):
    promedio = sum(fila) / len(fila)
    print(f"Estudiante {i}: {promedio:.2f}")

print("\nPromedio por materia:")

materias = len(notas[0])
for j in range(materias):
    suma = sum(notas[i][j] for i in range(len(notas)))
    promedio = suma / len(notas)
    print(f"Materia {j+1}: {promedio:.2f}")

#Ejercicio 9

tablero = [["-" for _ in range(3)] for _ in range(3)]

# Mostrar tablero inicial
for fila in tablero:
    print(" ".join(fila))
print()

# Dos jugadores hacen jugadas
# Ejemplo: 4 jugadas alternadas
turnos = [("X", (0, 0)), ("O", (1, 1)), ("X", (0, 1)), ("O", (2, 2))]

for simbolo, (f, c) in turnos:
    print(f"Juega {simbolo} en fila {f}, columna {c}")
    
    if tablero[f][c] == "-":
        tablero[f][c] = simbolo
    else:
        print("Casilla ocupada, intenta otra vez.")
    
    # Mostrar tablero después de la jugada
    for fila in tablero:
        print(" ".join(fila))
    print()

#Ejercicio 10

ventas = [
    [5, 7, 6, 4, 8, 10, 9],   # Producto 1
    [3, 6, 4, 7, 5, 8, 6],    # Producto 2
    [10, 12, 9, 11, 13, 15, 14], # Producto 3
    [2, 3, 4, 2, 3, 5, 4]     # Producto 4
]

# 1) Total vendido por cada producto (suma por fila)
print("Total por producto:")
for i, fila in enumerate(ventas, start=1):
    total = sum(fila)
    print(f"Producto {i}: {total}")

print()

# 2) Día con mayores ventas totales (suma por columna)
dias = len(ventas[0])
totales_por_dia = [sum(ventas[f][c] for f in range(len(ventas))) for c in range(dias)]
mayor_ventas = max(totales_por_dia)
dia_mayor = totales_por_dia.index(mayor_ventas) + 1  # +1 porque empieza en 1
print(f"Día con mayores ventas totales: Día {dia_mayor} ({mayor_ventas} ventas)")

print()

# 3) Producto más vendido en la semana
totales_por_producto = [sum(fila) for fila in ventas]
mas_vendido = max(totales_por_producto)
producto_mas_vendido = totales_por_producto.index(mas_vendido) + 1
print(f"Producto más vendido en la semana: Producto {producto_mas_vendido} ({mas_vendido} ventas)")
