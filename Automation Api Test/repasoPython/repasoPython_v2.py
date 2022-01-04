import re
import datetime

text = 'Esta ejemplo es para manejar una cadena de caracteres'

# --------------------------------------------------------------------------------------------
# Metodo Findall
# findall = buscar sobre una expresion regular
matching = re.findall('ejemplo', text)

# puedo buscar por varias string
matching2 = re.findall('ejemplo|cadena|caracteres', text)

# parametro IGNORECASE: ignora el case(mayuscula, minuscula) de la palabra que busca
matching3 = re.findall('EJEMPLO', text, re.IGNORECASE)
# El print devuelve un array de caracteres
print(matching)
print(matching2)
print(matching3)

# --------------------------------------------------------------------------------------------
# Método search: muestra si se encontró la palabra, y la posición (desde/hasta)
search = re.search('cadena', text, re.IGNORECASE)
print(search)

# Ejemplos de usos del metodo search:
# Se muestra un mensaje si se encuentra o no la palabra.
if search:
    print('Se encontro la palabra buscada')
else:
    print('No se encontró la palabra buscada')

# Cambio el str que encuetro por otro, si no lo encuentro muestro el original
if search:
    print('Se encontro la palabra buscada')
    text = re.sub('ejemplo', 'muestra', text, re.IGNORECASE)
    print('Encontré el str.')
    print(text)
else:
    print('No se encontró la palabra buscada')
    print(text)

# --------------------------------------------------------------------------------------------
# Método Split: divide el str en base a la cadena encontrada.
# Este método devuelve un array con objetos en base al corte realizado.

split = re.split(' ', text, re.IGNORECASE)
print(split)

# Ejemplo de uso:

for result in split:
    print(result)

# --------------------------------------------------------------------------------------------
Escenario = {}

response = 'La respuesta es OK - Id:200'

# devuelve el resultado despues de Id:
patronDeBusqueda = r'(?<=:)\w+'

result = re.findall(str(patronDeBusqueda), response, re.IGNORECASE)

print(result)

Escenario['resultadoBusqueda'] = str(result[0])

print(f"El resultado de la búsqueda es: {Escenario['resultadoBusqueda']}")

# --------------------------------------------------------------------------------------------

