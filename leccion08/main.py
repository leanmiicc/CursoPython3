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
# def myFunction(args, *args, **kargs) primero parametros fijos, luego parametros varibles del tipo tupla, y por ultimo parametros variables del tipo diccionario.
