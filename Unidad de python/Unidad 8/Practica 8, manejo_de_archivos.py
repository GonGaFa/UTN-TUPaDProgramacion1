#Ejercicio 1

with open ("productos.txt", "w") as archivo:
    archivo.write("libro,50000.0,5\n")
    archivo.write("lapicera,200.0,40\n")
    archivo.write("lapiz,250.0,50\n")


#Ejercicio 2


with open ("productos.txt", "r") as archivo:
    lineas = archivo.readlines()
    for linea in lineas:
        producto = linea.strip().split(",")
        print(f"Producto: {producto[0]} | Precio: {producto[1]} | Cantidad: {producto[2]}")


#Ejercicio 3

flag = "t"

with open ("productos.txt", "r") as archivo:
    lineas = archivo.readlines()
    for linea in lineas:
        producto = linea.strip().split(",")
        print(f"Producto: {producto[0]} | Precio: {producto[1]} | Cantidad: {producto[2]}")

while flag:
    with open ("productos.txt", "a") as archivo:
        producto_usuario = input("Ingrese un nuevo producto: ").lower()
        precio_usuario = float(input("Ingrese el precio del producto: "))
        cantidad_usuario = input("Ingrese la cantidad de unidades del producto: ")
        archivo.write(f"{producto_usuario},{precio_usuario},{cantidad_usuario}\n")
        flag = input("Ingrese 't' si desea continuar agregando productos, presione cualquier otra tecla para salir: ")
        



#Ejercicio 4

productos = []

with open ("productos.txt", "r") as archivo:
    lineas = archivo.readlines()
    for linea in lineas:
        producto = linea.strip().split(",")
        productos.append({"nombre": producto[0], "precio": producto[1], "cantidad": producto[2]})

for p in productos:
    print(p)


#Ejercicio 5

input_usuario = input("Por favor, escriba el producto del cual desea conocer su stock: ")

for diccionario in productos:
    if input_usuario in diccionario["nombre"]:
        print(f"Producto: {diccionario["nombre"]} | Precio: {diccionario["precio"]} | Cantidad: {diccionario["cantidad"]}")
    else:
        ValueError


#Ejercicio 6

with open("productos.txt", "w") as archivo:
    for diccionario in productos:
        archivo.write(f"{diccionario["nombre"]},{diccionario["precio"]},{diccionario["cantidad"]}\n")