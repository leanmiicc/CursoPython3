print("----------------------------------------------------")
print("Leccion 8.46")
print("---- Funciones ----")


# Declaracion de una funcion:
def miFuncion():
    print("hola mundo desde mi funcion...")


# Llamada de una funcion:
miFuncion()

print("----------------------------------------------------")
print("Leccion 8.47")
print("---- Funciones: Paso de Argumentos y Parametros ----")


# Parametros: es lo que se define en la funcion al momento de crearla.
# Argumentos: Son los paramentros que va a recibir dicha función al momento de llamarla.

# Declaracion de una funcion con dos parametros.:
# No es necesario definir que tipo de dato tiene que recibir como parametro.
def miFuncion(nombre, apellido):
    print(f'Mi nombre es: {nombre} {apellido}')


# Llamada de una funcion pasandole Argumentos:
miFuncion('Leandro', 'Micciche')
miFuncion('Gabriela', 'Barilli')

# No es necesario definir que tipo de dato se le manda en los argumentos.
miFuncion(20, 21)

print("----------------------------------------------------")
print("Leccion 8.48")
print("---- Funciones: Return ----")


# Return sirve para devolver/retornar un resultado.
def sumar(a, b):
    return a + b


# Genero una variable para guardarme el dato que genera la funcion sumar.
resultado = sumar(4, 5)
print(f'El resultado de la suma es: {resultado}')

# Otra manera de llamar a una funcion dentro de un print.
print(f'El resultado de la suma es: {sumar(2, 3)}')

print("----------------------------------------------------")
print("Leccion 8.48")
print("---- Funciones: Valores por default de los parametros. ----")


# funcion con valores por default de los parametros.
# def sumar(a:int=0, b:int=0) -> int
def sumar(a=0, b=0) -> int: # -> Indicio de que tipo de dato va a regresar, pero si se retorna un string, no se rompe, ya que los tipos de datos son dinamicos.
    return a + b


# Se muetra la suma de los valores por default.
print(f'El resultado es: {sumar()}')

# paso argumentos:
# Se pisan los valores default por los argumentos que se pasan.
resultado = sumar(10, 20)
print(f'El resultado es: {resultado}')


print("----------------------------------------------------")
print("Leccion 8.49")
print("---- Funciones: Argumentos Variables. ----")

# De esta defino una funcion con parametros variables. Por donde se transforma en una tupla
# def listNames(*args): denominacion del parametro de la documentacion de python.
def listNames(*names):
    for name in names:
        print(f'El nombre es: {name}')

listNames('Leandro', 'Gabriela', 'Mateo', 32, 40, 2)
print('--------- Nueva llamada: ---------')
listNames('Julio', 'Teodora')

print("----------------------------------------------------")
print("Leccion 8.50")
print("---- Ejercicion crear funcion. ----")

"""Crear una función para sumar los valores recibidos de tipo numérico, 
utilizando argumentos variables *args como parámetro de la función y regresar como resultado la suma de todos los valores 
pasados como argumentos."""


def mySum(*numbers):
    add = 0
    for number in numbers:
        add = add + number
    return add

totalSum = mySum(2, 3, 4, 5, 6)
print(f'El resultado total es: {totalSum}')

print("----------------------------------------------------")
print("Leccion 8.50")
print("---- Ejercicion crear funcion. ----")

"""
Crear una función para multiplicar los valores recibidos de tipo numérico, utilizando argumentos 
variables *args como parámetro de la función y regresar como resultado la multiplicación de todos los valores pasados como argumentos.
"""

def myMultiply(*numbers):
    multiply = 1
    for number in numbers:
        multiply *= number
    return multiply

totalSum = myMultiply(2, 3, 4, 5, 6)
print(f'El resultado total es: {totalSum}')

print("----------------------------------------------------")
print("Leccion 8.51")
print("---- Funciones ----")
# funciones variables pasando diccionarios (keys, values):

# Defino una funcion para que reciba un diccionario de parametro
# Documentacion de python:
# def listDiccionario(**kargs):
def listDiccionario(**values):
    for key, values in values.items():
        print(f'La Key es: {key} y el values es: {values}')

# La key no lleva comillas.
listDiccionario(nombre='Leandro', ID=1)

# Orden de parametros en las funciones
# def myFunction(args, *args, **kargs) primero parametros fijos,
# luego parametros varibles del tipo tupla, y por ultimo parametros variables del tipo diccionario.

print("----------------------------------------------------")
print("Leccion 8.52")
print("---- Funciones ----")
# Distintos tipos datos como argumento de una funcion.

# Creo una funcion que recibe como paremetro una lista de nombres
def namesList(names):
    for name in names:
        print(name)

# Creo la lista de nombres
names = ['Leandro', 'Gabriela','Mateo','Juan','Lourdes']

# Llamo a la funcion y le paso como argumento la lista de nombre.
namesList(names)

# Llamo a la funcion solo pasandole un argumento.
# En esta caso va a iterar cada uno de los caracteres de la cadena "Julio"
print("------ Lista de caracteres... ------ ")
namesList('Julio')

# Llamo a la funcion pasandole un tipo de dato INT
print("------ Tipo de dato INT... ------ ")
# namesList(10) # Error: TypeError: 'int' object is not iterable

# En el caso de que se quiera mostrar valor numericos, habra que convetilos en un tupla, agregando () parentesis:
print("------ Numero en tupla... ------ ")
namesList((10, 11, 12, 13))

# Si los datos los pongo en [] el argunmento se transforma en un lista.
namesList([10, 11, 12, 13])

print("----------------------------------------------------")
print("Leccion 8.52")
print("---- Funciones ----")
# Funciones Recursivas: es una funcion que se llama asi misma para finalizar una tarea.
"""
Calculo de un numero factorial:
5! = 5 * 4 * 3 * 2 * 1
5! = 5 * 4 * 3 * 2
5! = 5 * 4 * 6
5! = 5 * 24
5! = 120
"""

def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number-1)

number = 5
result = factorial(number)
print(f'El factorial de {number} es: {result}')


print("----------------------------------------------------")
print("Leccion 8.53")
print("---- Funciones Recursivas Ejercicio ----")
"""
Imprimir numeros de 5 a 1 de manera descendente usando funciones recursivas. Puede ser cualquier valor positivo, ejemplo, si pasamos el valor de 5, 
debe imprimir: 5 4 3 2 1 Si se pasa el valor de 3, debe imprimir: 3 2 1 Si se pasan valores negativos no imprime nada
"""

def descendingNumber(number):
    if number >= 1:
        print(number)
        descendingNumber(number - 1)

number = 6
descendingNumber(number)

print("----------------------------------------------------")
print("Leccion 8.53")
print("---- Ejercicio funciones. ----")

"""
Crear una función para calcular el total de un pago incluyendo un impuesto aplicado.
La función se llama calcular_total()
La función recibe dos parámetros:
1. pago_sin_impuesto
2. impuesto (Ej. Valor de 10, significa 10% de impuesto, Valor de 16 significa el 16% de impuesto)
La función debe regresar el total del pago incluyendo el porcentaje de impuesto proporcionado.
Ej. Si llamamos a la función calcular_total(1000, 16) debe retornar el valor 1,160.0
Los valores los debe proporcionar el usuario y se procesados con la función input, convirtiendolos a tipo float.
"""
# funcion de calulo total
def calcular_total(pago_sin_impuesto, impuesto):
    return pago_sin_impuesto + ((impuesto/100) * pago_sin_impuesto)

# Ingresa los datos el usuarios:
pago_sin_impuesto = float(input('Ingrese el valor de su pago sin impuestos: '))
impuesto = float(input('Ingrese el impuesto del pago: '))

# Llamada de funcion y print de resultado.
pago_con_impuesto = calcular_total(pago_sin_impuesto, impuesto)
print(f'El pago con impuesto es: {pago_con_impuesto}')

print("----------------------------------------------------")
print("Leccion 8.54")
print("---- Ejercicio funciones. ----")

"""
Realizar dos funciones para convertir de grados celsius a fahrenheit y viceversa.
Función 1. Recibir un parámetro llamado celcius y regresar el valor equivalente a fahrenheit
La función se llama: celsius_fahrenheit(celsius) 
La fórmula para convertir de celsius a fahrenheit es: celsius * 9/5 + 32 
Función 2. Recibir un parámetro llamado fahrenheit y regresar el valor equivalente a celsius:
fahrenheit_celsius(fahrenheit)         
La fórmula para convertir de fahrenheit a celsius es:  (fahrenheit-32) * 5/9
Los valores los debe proporcionar el usuario, utilizando la función input y convirtiendolo a tipo float.
Deben hacer al menos dos pruebas, una donde conviertan de grados celcius a grados fahrenheit,
y otra donde conviertan de grados fahrenheit a grados celsius y mandar a imprimir los resultados.
"""

# Definicion de funciones:
def celsius_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_celsius(fahrenheit):
    return (fahrenheit-32) * 5/9

# Ingreso de datos:
gradosCelsius = float(input('Ingrese los grados en Celsius para transformarlos en Fahrenheit: '))
gradosFahrenheit = float(input('Ingrese los grados en Fahrenheit para transformarlos en Celsius: '))

# Imprimo los resultado
print(f'Los grados {gradosCelsius}°C son en fahrenheit: {celsius_fahrenheit(gradosCelsius)}°F')
print(f'Los grados {gradosFahrenheit}°F son en celsius: {fahrenheit_celsius(gradosFahrenheit)}°C')