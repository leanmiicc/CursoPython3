from Generic.formateoArchivos.tituloEjercicio import tituloEjercicio

titulo = tituloEjercicio('Leccion 9.64', 'Ejercicio: Calcular el volumen de un cubo').generarTitulo()

class Cubo:
    def __init__(self, ancho, alto, largo):
        self.ancho = ancho
        self.alto = alto
        self.largo = largo

    def calcularVolumen(self):
        return self.ancho * self.alto * self.largo

ancho = int(input('Ingrese el ancho del cubo: '))
alto = int(input('Ingrese el alto del alto: '))
largo = int(input('Ingrese el largo del cubo: '))

if ancho <= 0:
    print('El ancho no es valido')
elif alto <= 0:
    print('EL alto no es valido.')
elif largo <= 0:
    print('El largo no es valido.')
else:
    cubo = Cubo(ancho, alto, largo)
    print(f'El volumen del cubo es: {cubo.calcularVolumen()}')
