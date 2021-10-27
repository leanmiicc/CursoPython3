print("----------------------------------------------------")
print("Leccion 4.18")
print("---- Operadores en Python ----")
print("---- Suma ----")
operandoA = 10
operandoB = 5
suma = operandoA + operandoB

print('El resultado de la suma es:', suma)
print(f'El resultado suma es: {suma}')

print("----------------------------------------------------")
print("Leccion 4.19")
print("---- Operadores en Python ----")

print("---- Resta ----")
resta = operandoA - operandoB
print(f'El resultado resta es: {resta}')

print("---- Multiplicacion ----")
multiplicacion = operandoA * operandoB
print(f'El resultado multiplicacion es: {multiplicacion}')

print("---- Division: Resultado coma flotante ----")
division = operandoA / operandoB
print(f'El resultado division es: {division}')

print("---- Division: Resultado parte entera ----")
division = operandoA // operandoB
print(f'El resultado division entera es (int): {division}')

print("---- Modulo ----")
modulo = operandoA % operandoB
print(f'El resultado modulo es: {modulo}')

print("---- Exponente ----")
exponente = operandoA ** operandoB
print(f'El resultado exponente es: {exponente}')

print("----------------------------------------------------")
print("tarea")
print("---- Calculo de area y perimetro de un rectangulo ----")

##alto = int(input("Proporciona el alto: "))
##ancho = int(input("Proporciona el ancho: "))
##area = alto * ancho
##perimetro = (alto + ancho) * 2

##print(f'Area: {area}')
##print(f'Perímetro: {perimetro}')

print("----------------------------------------------------")
print("Leccion 4.20")
print("---- Operadores de asignacion en Python ----")

miVariable = 10
print(miVariable)

# Reasignacion de variable
miVariable = miVariable + 1
print(miVariable)

# Incremento con reasignación:
miVariable += 1
print(miVariable)

miVariable -= 2
# miVariable = miVariable - 2
print(miVariable)

miVariable *= 3
print(miVariable)

miVariable /= 2
print(miVariable)

print("----------------------------------------------------")
print("Leccion 4.21")
print("---- Operadores de comparación en Python ----")

a = 4
b = 5
resultado = a == b
print(f'Resultado de == A y B es: {resultado}')

resultado = a != b
print(f'Resultado de != A y B es: {resultado}')

resultado = a > b
print(f'Resultado de > A y B es: {resultado}')

resultado = a >= b
print(f'Resultado de >= A y B es: {resultado}')

resultado = a < b
print(f'Resultado de < A y B es: {resultado}')

resultado = a <= b
print(f'Resultado de <= A y B es: {resultado}')

print("----------------------------------------------------")
print("Leccion 4.21")
print("---- Ejercicio de numero impar o par ----")
"""
a = int(input("Ingrese un numero: "))
if a % 2 == 0:
    print(f'El numero {a} es par')
else:
    print(f'El numero {a} es impar')
"""

print("----------------------------------------------------")
print("Leccion 4.22")
print("---- Ejercicio de Mayor de edad ----")
"""
edadAdulta = 18
edad = int(input("Ingrese su edad: "))

if edad >= edadAdulta:
    print(f'La persona tiene {edad} años de edad y es adulta.')
else:
    print(f'La persona tiene {edad} años de edad y es menor.')
"""
print("----------------------------------------------------")
print("Leccion 4.23")
print("---- Operadores lógicos: ----")
"""
a = False
b = False
resultado = a and b
print(f'{a} y {b}. utilizando el operador AND: {resultado}')

resultado = a or b
print(f'{a} y {b}. Utilizando el operador OR: {resultado}')

resultado = not a
print(f'{a}. Utilizando el operador NOT: {resultado}')
"""
print("----------------------------------------------------")
print("Leccion 4.23")
print("---- Ejercicio: Valor dentro de Rango ----")
""""
inicio = int(input("Ingrese el inicio del Rango: "))
fin = int(input("Ingrese el fin del Rango: "))
valor = int(input("Ingrese un valor numerico a verificar dentro del rango: "))
dentroRango = valor >= inicio and valor <= fin # Expresion de tipo Boolean
#dentroRango = inicio <= valor <= fin

if dentroRango == True:
    print(f'El numero {valor}, se encuentra dentro del rango ({inicio},{fin}) informado.')
else:
"""

print("----------------------------------------------------")
print("Leccion 4.24")
print("---- Ejercicio: Operador Or - Asistir Juego----")

vacaciones = False
diaDescanso = False
asistirJuego = vacaciones or diaDescanso

if asistirJuego:
    print('El padre puede asistir al juego de su hijo.')
else:
    print('El padre no puede asistir al juego de su hijo.')
