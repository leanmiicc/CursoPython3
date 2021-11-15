# Se crea la clase persona.
# Se recomienda que tanto la clase como el archivo que contiene la clase tengan el mismo nombre
# y siempre en Mayuscula la primer letra.
# Se usa esta clase solo mencionar la funcionalidad de la palabra reservada "pass"
class Ejemplo_Persona:
    pass # Se agrega la palabra "pass" para indicar que no se procesa nada mas, solo es finalizar la creacion de la clase Persona

# Visualizamos que tipo de dato es Persona
print(type(Ejemplo_Persona))

class Persona:
    # Metodo __init__ se definen los atributos de instacia de objeto.
    # No es una buena practica poner datos por default a los atributos, eso es solo a modo de ejemplo.
    def __init__(self):
        self.nombre = 'Juan'
        self.apellido = 'Perez'
        self.edad = 28

# Creo un variable (persona1) en donde instancio el objeto de la clase Persona()
# Al instanciar el nuevo objeto va a tomar los datos del metodo __init__ a través de argumento self.
persona1 = Persona()
print(f'El nombre es: {persona1.nombre}, el apellido es: {persona1.apellido}, y la edad es: {persona1.edad}')
