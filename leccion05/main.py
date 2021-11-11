print("----------------------------------------------------")
print("Leccion 5.31")
print("---- Sentencia de control IF ----")

condicion = 'False'

if condicion == True:
    print("Condicion verdadera.")
elif condicion == False:
    print("Condicion falsa.")
else:
    print("Condicion no reconocida")

print("----------------------------------------------------")
print("Leccion 5.33")
print("---- Convertir Numero a Texto ----")

"""a = int(input("ingrese un valor entre 1 y 3: "))
numeroTexto = ''

if a == 1:
    numeroTexto = 'Número Uno'
elif a == 2:
    numeroTexto = 'Número Dos'
elif a == 3:
    numeroTexto = 'Número Tres'
else:
    numeroTexto = 'Valor fuera de rango'
print(f'El número ingresado es: {a} - Se lee como: {numeroTexto}')"""

print("----------------------------------------------------")
print("Leccion 5.34")
print("---- Sintaxis simplificada del IF ----")

# Forma normal:
condicion = False

if condicion:
    print(f"La condicion es: {condicion}")
else:
    print("La condicion es Falsa.")

# Forma simplificada:
print(f"La condicion es: {condicion}") if condicion else print("La condicion es Falsa.")

print("----------------------------------------------------")
print("Leccion 5.35")
print("---- Calular estacion segun mes del año. ----")
"""
mes = int(input("Ingrese el mes del año (1-12): "))
estacion = None

if mes == 12 or mes == 1 or mes == 2:
    estacion = 'Verano'
elif mes == 3 or mes == 4 or mes == 5:
    estacion = 'Otoño'
elif mes == 6 or mes == 7 or mes == 8:
    estacion = 'Invierno'
elif mes == 9 or mes == 10 or mes == 11:
    estacion = 'Primavera'
else:
    estacion = 'Mes Incorrecto'

print(f"Para el {mes} la estación es: {estacion}")

"""

print("----------------------------------------------------")
print("Leccion 5.36")
print("---- Ejercicio: Etapas de vida segun edad ----")

"""
edad = int(input("Ingrese su edad: "))
mensaje = None

if 0 <= edad < 10:
    mensaje = 'La infancia es increible...'
elif 10 <= edad < 20:
    mensaje = 'Muchas cambios y mucho estudio...'
elif 20 <= edad < 30:
    mensaje = 'Amor y comienza el trabajo'
else:
    mensaje = 'Etapa de vida no reconocida.'

print(f"Tu edad es: {edad}, {mensaje}")
"""

print("----------------------------------------------------")
print("Leccion 5.37")
print("---- Ejercicio: Calificaciones ----")

calificacion = int(input("Ingrese la calificación: "))
imprimirCalificacion = None

if 9 <= calificacion <= 10:
    imprimirCalificacion = 'Obtuviste una A'
elif 8 <= calificacion < 9:
    imprimirCalificacion = 'Obtuviste una B'
elif 7 <= calificacion < 8:
    imprimirCalificacion = 'Obtuviste una C'
elif 6 <= calificacion < 7:
    imprimirCalificacion = 'Obtuviste una D'
elif 0 <= calificacion < 6:
    imprimirCalificacion = 'Obtuviste una F'
else:
    imprimirCalificacion = 'Valor Desconocido.'

print(imprimirCalificacion)

