print("----------------------------------------------------")
print("Leccion 6.38")
print("---- Ciclo While ----")

# condicion = True
#
# while condicion:
#     print("Ejecutando ciclo While")
#
# else:
#     print("Fin del ciclo While")

"""
contador = 0

while contador < 3:
    print(contador)
    contador += 1
else:
    print("Fin ciclo While...")
"""

print("----------------------------------------------------")
print("Leccion 6.39")
print("---- Ejercicio: Imprimir numero naturales del 0 al 10 ----")

"""
contador = 0

while contador <= 10:
    print(contador)
    contador += 1
else:
    print("Fin del ciclo While...")
"""

print("----------------------------------------------------")
print("Leccion 6.40")
print("---- Ejercicio: Imprimir numero naturales del 5 al 1 de forma descendente ----")

contador = 5

while contador >= 1:
    print(contador)
    contador -= 1
else:
    print("Fin del ciclo While...")

print("----------------------------------------------------")
print("Leccion 6.40")
print("---- Ciclo For each ----")

cadena = 'Hola'

for letra in cadena:
    print(letra)
else:
    print('Fin del ciclo For Each...')

print("----------------------------------------------------")
print("Leccion 6.41")
print("---- Ciclo For each + Break ----")

cadena = 'Holanda'

for letra in cadena:
    if letra == 'a':
        print(f'Letra encontrada: {letra}')
        break
else:
    print('Fin del ciclo For Each...')

print("----------------------------------------------------")
print("Leccion 6.41")
print("---- Ciclo For each + Continue ----")

# for i in range(10):
#     if i % 2 == 0:
#         print(f'Valor: {i}')

for i in range(10):
    if i % 2 != 0:
        continue # --> Si se cumple la condicion, no se ejecuta nada debajo del IF y continua con la siguiente iteracion.
    print(f'Valor: {i}')


