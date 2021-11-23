print("Leccion 3.9")
print("Tipo de datos en Python:")

x = 10
print(x)
print(type(x))

x = "Hola Mundo"
print(x)
print(type(x))

x = True
print(x)
print(type(x))

x: str = "Prueba del hint (:)"
print(x)
print(type(x))

x: float = 10.5
print(x)
print(type(x))

print("----------------------------------------------------")
print("Leccion 3.10")
print("Tipo de datos en Python:")

# Tipo int
x = 10
print(x)
print(type(x))

# Tipo float
x: float = 10.5
print(x)
print(type(x))

# Tipo String
x = "Hola Mundo"
print(x)
print(type(x))

# Tipo Boolean
x = True
print(x)
print(type(x))

print("----------------------------------------------------")
print("Leccion 3.11")
print("Manejo de Strings")

# String
miGrupoFavorito = "Nightwish"
comentario = " the best metal symphonic rock band"
print(miGrupoFavorito)
print("Mi grupo favorito es: " + miGrupoFavorito + comentario)

print("----------------------------------------------------")
print("Leccion 3.12")
print("Más manejo de Strings")

miGrupoFavorito = "Nightwish"
comentario = "the best metal symphonic rock band"

print("Mi grupo favorito es:", miGrupoFavorito, comentario)

# Concatenacion de string
num1 = "1"
num2 = "2"
print("La contatenacion es:", num1 + num2)

# Suma de Int
num1 = 1
num2 = 2
print("La suma es:", num1 + num2)

print("----------------------------------------------------")
print("Leccion 3.13")
print("Tipo de dato Boolean:")

miVariableVerdadera = True
print(miVariableVerdadera)

miVariableFalsa = False
print(miVariableFalsa)

comparacionTrue = 3 > 2
print("La comparacion de 3 > 2 es:", comparacionTrue)

comparacionFalse = 1 > 2
print("La comparacion de 1 > 2 es:", comparacionFalse)

print("Comparativa verdadera:")
if comparacionTrue:
    print("El resultado es verdadero")
else:
    print("El resultado es falso")

print("Comparativa falsa")
if comparacionFalse:
    print("El resultado es verdadero")
else:
    print("El resultado es falso")

print("----------------------------------------------------")
print("Leccion 3.14")
print("Funcion Input: ")

#resultado = input("Ingrese un valor para visualizar: ")
#print("El valor informado es:", resultado)
print("Fin del programa")

print("----------------------------------------------------")
print("Leccion 3.15")
print("Convercion de la entrada de Datos: ")

##num1 = int(input("Ingresa el primer numero para sumar: "))
##num2 = int(input("Ingresa el segundo numero para sumar: "))
resultado =  num1 + num2
##print("La suma de los numero es:", resultado)

print("----------------------------------------------------")
print("Leccion 3.15")
print("---- Ejercicio de Calificación de día ----")
#Solicitar al usuario que califique su dia del 1 al 10 y luego mostrarlo por pantalla
#solucion:

calificacionDia = int(input("Ingrese como califica su día del 1 al 10: "))

while (calificacionDia > 10 or calificacionDia < 1):
    print("Ha ingresado un numero incorrecto, repita la operación.")
    calificacionDia = int(input("Ingrese como califica su día del 1 al 10: "))

print("Usted califico su día con:", calificacionDia)
