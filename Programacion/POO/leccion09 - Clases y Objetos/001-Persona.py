from Generic.formateoArchivos.tituloEjercicio import tituloEjercicio

print("----------------------------------------------------")
print("Leccion 9.58")
print("---- Clases y Objetos en Python ----")
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

print("----------------------------------------------------")
print("Leccion 9.59")
print("---- Clases y Objetos en Python - ver ----")

# Creo una nueva clase para definir el método constructor sin asignarle datos por default a los atributos, sino que le paso argumentos al constructor.

class Persona2:
    def __init__(self, nombre, apellido, edad): # Le agrego argumentos al constructor.
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad


# Pido al usuario los parametros que se le van a pasar a la llamada del objeto.
"""
nombre = input("Ingrese el nombre de la persona: ")
apellido = input('Ingrese el apellido de la persona: ')
edad= int(input('Ingrese la edad de la persona: '))
"""
# Instancio el objeto en la variable persona2 y le paso los parametros que complete antes.
# persona2 = Persona2(nombre, apellido, edad)

# Muetro por pantalla los parametros que pasé.
# print(f'La persona creada se llama: Nombre: {persona2.nombre}, Apellido: {persona2.apellido}, Edad: {persona2.edad}')

# Creo otro objeto de la misma clase Persona2 y le paso los parametros sin pedirlos al usuario:
persona3 = Persona2('Gabriela', 'Barilli', 35)

# Muetro por pantalla los parametros que pasé.
print(f'La persona creada se llama: Nombre: {persona3.nombre}, Apellido: {persona3.apellido}, Edad: {persona3.edad}')

print("----------------------------------------------------")
print("Leccion 9.61")
print("---- Clases y Objetos en Python: Modificar Atributos de un Objeto  ----")

# Creo un nuevo objeto apartir de la clase Persona2: objeto persona4
persona4 = Persona2('Mateo', 'Micciche', 2)
print(f'La persona creada se llama: Nombre: {persona4.nombre}, Apellido: {persona4.apellido}, Edad: {persona4.edad}.')

# Modifico los atributos de nombre, apellido y edad del objeto recien creado persona4:

persona4.nombre = 'Nicolas'
persona4.apellido = 'Micciche'
persona4.edad = 22
print(f'La persona creada se llama: Nombre: {persona4.nombre}, Apellido: {persona4.apellido}, Edad: {persona4.edad}.')

print("----------------------------------------------------")
print("Leccion 9.61")
print("---- Clases y Objetos en Python: Metodo de Instancia en Python  ----")

# Cro una nueva clase:
class Persona3:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # Agrego un metodo de instancia a la clase:
    # Se le llama metodo de instacia ya que estan asociados con los objetos que vamos a crear.
    # Self, solo se utiliza dentro de la definicion de la clase para acceder a los distintos atributos.

    def mostrarDetalles(self):
        print('Utilizo el método mostrarDetalles(): ')
        print(f'Persona: {self.nombre} {self.edad}')

persona1 = Persona3('Mateo', 2)

# En esta caso no es necesario pasarle la referencia ya que como el metodo es llamado desde la instacia del objeto, toma el objeto creado como referencian self
persona1.mostrarDetalles()

# puede agregar un nuevo un nuevo atributo al objeto persona1 de la siguiente manera:
persona1.telefono = '11635323121'
print(f'el telefono de {persona1.nombre} es {persona1.telefono}')

# Tambien se puede llamar al metodo mostrarDetalle invocandolo desde la clase, pero en esta caso hay que pasarle la referencia, se le pasa el objeto persona 1 = Mateo, 2
Persona3.mostrarDetalles(persona1)

# Creacion de un segundo objeto a partir de la clase Persona3:

persona2 = Persona3('Marta', 3)
persona2.mostrarDetalles()

# Si bien se agrego el atributo de telefono en el objeto persona1, no se translada al objeto persona2:
# Error: AttributeError: 'Persona3' object has no attribute 'telefono'
# print(persona2.telefono)


print('Continua en la clase Aritmetica')

titulo = tituloEjercicio('Leccion 9.65', 'Robusteciendo metodo __init__').generarTitulo()

class Persona4:
    def __init__(self, nombre, apellido, edad, *args, **kwargs):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.args = args
        self.kwargs = kwargs

    def mostrarDetalles(self):
        print('Utilizo el método mostrarDetalles(): ')
        print(f'Persona: {self.nombre} - {self.apellido} - {self.edad} - {self.args} - {self.kwargs}')

persona5 = Persona4('Leandro', 'Gonzalez', 25, '15342514', 2, 3, 5, sexo='masculino',ejercicio=True)
persona5.mostrarDetalles()




