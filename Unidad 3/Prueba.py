#Ejercicio 10

hemisferio = input("Ingrese que hemisferio vive (N/S): ").upper()

mes = input("Ingrese en que mes se encuentra(E,F,M,A,M,Jn,Jl,A,S,O,N,D): ").upper()

dia = int(input("Ingrese que dia del mes es:"))

if hemisferio == "N":
    if (mes == "D" and dia >= 21) or (mes == "E" and dia <=31) or (mes == "F" and dia <=31) or (mes == "M" and dia < 21):
        print("Usted se encuentra en invierno")
    elif (mes == "M" and dia >= 21) or (mes == "A" and dia <=31) or (mes == "M" and dia <=31) or (mes == "Jn" and dia < 21):
        print ("Usted se encuentra en primavera")
    elif (mes == "Jn" and dia >= 21) or (mes == "Jl" and dia <=31) or (mes == "A" and dia <=31) or (mes == "S" and dia <= 21):
        print("Usted se encuentra en verano")
    elif (mes == "S" and dia >= 21) or (mes == "O" and dia <=31) or (mes == "N" and dia <=31) or (mes == "D" and dia <= 21):
        print("Usted se encuentra en otoño")

elif hemisferio == "S":
        if (mes == "D" and dia >= 21) or (mes == "E" and dia <=31) or (mes == "F" and dia <= 31) or (mes == "M" and dia < 21):
            print("Usted se encuentra en verano")
        elif (mes == "M" and dia >= 21) or (mes == "A" <= 31) or (mes == "M" <= 31) or (mes == "Jn" and dia < 21):
            print ("Usted se encuentra en otoño")
        elif (mes == "Jn" and dia >= 21) or (mes == "Jl" <= 31) or (mes == "A"<= 31) or (mes == "S" and dia <= 21):
            print("Usted se encuentra en invierno")
        elif (mes == "S" and dia >= 21) or (mes == "O" <= 31) or (mes == "N" <= 31) or (mes == "D" and dia <= 21):
            print("Usted se encuentra en primavera")

else: print("Error al pronosticar su estacion, fijese por la ventana")