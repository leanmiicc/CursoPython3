print("----------------------------------------------------")
print("Leccion 7.41")
print("---- Listas - Parte 1: ----")

# Definicion de una Lista
nombres = ['Juan', 'Karla', 'Ricardo', 'Maria']

# Imprimir la lista
print(nombres)

# Imprimir el primer elemento de la lista
print(nombres[0])
print(nombres[1])

# Imprimer los elementos de manera inversa
print(nombres[-1])
print(nombres[-2])

print("----------------------------------------------------")
print("Leccion 7.42")
print("---- Listas - Parte 2: ----")

# Imprimer un rango de elementos
print(nombres[0:2])  # El indice 2 no se incluye en la lista que se recupera

# Imprimir desde el inico de la lista hasta el numero anterior del indice indicado:
print(nombres[:3])

# Imprimir desde el indice indicado hasta el final:
print(nombres[0:])  # En esta caso si se incluye el indice 0.

# Cambiar un valor:
nombres[2] = 'Mario'
print(nombres)

# Iterar la lista
for nombre in nombres:
    print(nombre)
else:
    print("No existen mas nombres en la lista...")

print("----------------------------------------------------")
print("Leccion 7.43")
print("---- Listas - Parte 3: ----")

# Preguntar el largo de una lista:
print(len(nombres))

# Agregar Elementos en la lista:
nombres.append('Marta')
print(nombres)

# Insertar un elemento en un indice en especifico:
nombres.insert(1, 'Ramiro')  # Se inserta en la posicion 1 y el resto se mueve hacia la derecha un indice.
print(nombres)

# Remover un elemento de la lista por valor:
nombres.remove('Maria')
print(nombres)

# Remover el ultimo valor agregado:
nombres.pop()  # Elimina el ultimo valor agregado con un .append
print(nombres)

# Eliminar un elemento en un indice indicado:
del nombres[0]
print(nombres)

# Limpiar toda la lista:
nombres.clear()
print(nombres)

# Borrar de memoria la lista creada
"""del nombres
print(nombres)"""

print("----------------------------------------------------")
print("Leccion 7.43")
print("---- Ejercicio: Iterar un rango de 0 a 10 e imprimir números divisibles entre 3 ----")

for i in range(10):
    if i % 3 == 0:
        print(i)

print("----------------------------------------------------")
print("Leccion 7.43")
print("---- Tuplas ----")
# Tupla: no se puede agregar elementos, eliminarlos o cambiarlos, a esto se le llama inmutable.

frutas = ('naranja', 'banana', 'frutilla')
print(frutas)

# Largo de una tupla
print(len(frutas))

# Acceder a un elemento:
print(frutas[0])

# Acceder de forma inversa a un elemento:
print(frutas[-1])

# Acceder a un rango de valores:
print(frutas[0:2])  # El indice 2 no se incluye en la tupla que se recupera
print(
    frutas[0:1])  # Como se recupera solo un valor se le agrega una como (,) al final porque sino seria del tipo string.

print("----------------------------------------------------")
print("Leccion 7.44")
print("---- Tuplas - Segunda parte ----")

# Recorrer los elementos de una tupla
for fruta in frutas:
    print(fruta)

# Recorrer los elementos de una tupla sin falto de linea:
for fruta in frutas:
    print(fruta, end=' ')

# Cambiar valor de tupla
# frutas[0] = 'Damasco'
# print(frutas)

# Pasos para cambiar elementos de uan tupla
# No es una buena practica, si se va a modificar elegir un tipo de dato Lista.
# Primero: convierto la tupla en una lista
frutasLista = list(frutas)

# Segundo: Modifico el valor que quiero.
frutasLista[0] = 'Damasco'

# Tercero: Vuelvo a convertir la lista en una tupla
fruta = tuple(frutasLista)

# Cuarto: Imprimo la tupla modificada.
print('\n', frutas)

# Eliminar la tupla por completo
del frutas
# print(frutas) # Error: NameError: name 'frutas' is not defined. Did you mean: 'fruta'?

print("----------------------------------------------------")
print("Leccion 7.44")
print("---- Ejercicio: ----")
# Dada la siguiente tupla, crear una lista que sólo incluya los números menor que 5 utilizando un ciclo for: tupla = (13, 1, 8, 3, 2, 5, 8)

numbers = (13, 1, 8, 3, 2, 5, 8)
newNumbersList = []

for number in numbers:
    if number < 5:
        newNumbersList.append(number)
else:
    print(f"La lista final es: {newNumbersList}")

print("----------------------------------------------------")
print("Leccion 7.44")
print("---- Coleccion de datos 'Set': ----")
# Set: No mantienen un orden (sin indice a diferencia de las listas y de las tuplas), tampo se permite editar los elementos, pero si se pueden agregar y eliminar.

planetas = {'Marte', 'Venus', 'Jupiter'}
print(planetas)  # Ejecutar varias veces el codigo para ver el cambio de orden.

# Conocer el largo del set:
print(len(planetas))

# Verificar si un elemento esta presente:
print('Marte' in planetas)
print('Tierra' in planetas)

# Agregar mas elementos:
planetas.add('Tierra')
print(planetas)

# Verificacion de elementos duplicados:
planetas.add('Tierra')
print(planetas)  # Se vuelve a imprimir el set sin agregar de nuevo el planeta Tierra.

# Eliminar elementos :
"""planetas.remove('tierra')
print(planetas) # KeyError: 'tierra' es key sensitive."""

planetas.remove('Tierra')
print(planetas)

# Eliminar elemento con "discard" sin error si no se encuentra elemento:
planetas.discard('Urano')
print(planetas)  # Se verifica que no se elimina el elemento Urano porque no existe y tampoco da error el codigo.

# Limpiar los elementos del set.
planetas.clear()
print(planetas)

# Eliminar la variable de planetas:
del planetas
# print(planetas) # Error: NameError: name 'planetas' is not defined

print("----------------------------------------------------")
print("Leccion 7.45")
print("---- Coleccion de datos 'Diccionario': - Primera Parte ----")

# Es una coleccion de datos de llave - valor (Key - value), sin indice, para recuperar los elementos se usan las keys.
# Definición:

diccionario = {
    # KEY : VALUE
    'SR': 'Senior',
    'SSR': 'SemiSenior',
    'JR': 'Junior'
}
print(diccionario)

# Cantidad de Elementos:
print(len(diccionario))

# Acceder a un elemento del diccionario mediante key:
print(diccionario['SR'])

# Acceder mediante key con el metodo GET:
print(diccionario.get('SSR'))

# Modificar Elementos
diccionario['SSR'] = 'semi-senior'
print(diccionario)

print("----------------------------------------------------")
print("Leccion 7.45")
print("---- Coleccion de datos 'Diccionario': - Segunda Parte ----")

# Recorrer el diccionario mostrando la Key (que es la primera parte del elemento:
for key in diccionario:
    print(key)

# Recorrer el diccionario mostrando la key y el value:
for key, value in diccionario.items():
    print(key, value)

# Recorrer el diccionario mostrando solo las keys con un método:
for key in diccionario.keys():
    print(key)

# Recorrer el diccionario mostrnado solo los values con un método:
for value in diccionario.values():
    print(value)

# Validar que exista un elemento:
print('SR' in diccionario) # Devuelve TRUE porque existe
print('sr' in diccionario) # Devuelve false porque es key sensitive y con lo cual no existe.

# Agregar un elemento:
diccionario['TR'] = 'Trainee'
print(diccionario)

# No se pueden agregar key duplicadas, si se repite se reemplaza el value por el nuevo.

# Remover un elemeto del diccionario:
diccionario.pop('TR')
print(diccionario)

# Limpiar los elementos de un diccionario:
diccionario.clear()
print(diccionario)

# Eliminar la variable del diccionar por completo
del diccionario
# print(diccionario) # Error: NameError: name 'diccionario' is not defined



