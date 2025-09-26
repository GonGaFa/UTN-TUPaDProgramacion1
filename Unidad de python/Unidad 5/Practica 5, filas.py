"Pedir a usuario que indique de cuantas variables va a ser la función."
"Pedir a usuario que escriba la función booleana."
"Validar que la función (string) contenga realmente la cantidad de variables indicada. Acá es útil remover todo lo que no sea una letra."
"Validar que las operaciones booleanas sean válidas (solo se permite ^, v, ~, => y <=>)."
"Si está todo ok, se da feedback al usuario de que se está analizando la función. Caso contrario, que vuelva a escribir la función."

def user_input():
    cant_varibles = int(input("Ingrese cuantas varibles va a usar"))
    variables=[]
    while len(var) < cant_varibles:
        var= str(input(f"Ingrese las variables #{len(var)+1}: ")) #Comprueba que las variables ingresadas sean el mismo numero que pidio
        if var.isalpha() and var not in variables:
            variables.append(var) #Comprueba que las variables sean letras y no se repitan
        else:
            print("Error, ingrese una variable válida o que no se encuentre ya mencionada")
    return user_input(cant_varibles, variables)

def validacion_de_funciones(funcion, variables):
    operadores = ['^', 'v', '~', '=>', '<=>'] #operadores permitidos
    fun_bool = input(str("Escriba la función booleana, usando los siguientes operadores: ^, v, ~, =>, <=>: ")) #(a^b) v (~c), por ejemplo
    
    