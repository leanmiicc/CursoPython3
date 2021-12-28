# Creé un directorio donde guardo el formato de las lecciones y los titulos, lo import y lo instancio para usarlo.
from Generic.formateoArchivos.tituloEjercicio import tituloEjercicio

# Creo la variable ejercicio, le paso por paremtro la leccion y el titulo al constructor y luego llamo al metedo que tiene el formato.
ejercicio = tituloEjercicio('Leccion 9.63', 'Ejercicio: Calcular el area de un Rectangulo').generarTitulo()

class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea(self):
            return self.base * self.altura

base = int(input('Ingrese la base del rectangulo: '))
altura = int(input('Ingrese la altura del rectangulo: '))

if base <= 0:
    print("No corresponde a una base valida.")
elif altura <= 0:
    print("No corresponde a una altura valida.")
else:
    rectangulo = Rectangulo(base,altura)
    print(f'El área del rectangulo es: {rectangulo.calcularArea()} ')


