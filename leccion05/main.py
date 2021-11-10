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
print("Leccion 5.33")
print("---- Sintaxis simplificada del IF ----")

# Forma normal:
condicion = False

if condicion:
    print(f"La condicion es: {condicion}")
else:
    print("La condicion es Falsa.")

# Forma simplificada:
print(f"La condicion es: {condicion}") if condicion else print("La condicion es Falsa.")
