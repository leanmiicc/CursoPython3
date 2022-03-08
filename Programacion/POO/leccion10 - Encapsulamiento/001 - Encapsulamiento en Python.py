from Generic.formateoArchivos.tituloEjercicio import tituloEjercicio
from Generic.formateoArchivos.separador import separador

separador()
tituloEjercicio(73, "Encapsulamiento en Python").generarTitulo()

# Los atributos que comiencen con "_" (guión bajo) son atributos encapsulados, con lo cual no se deberia acceder de forma directa,
# ni modificarlos, son solo accesibles/modificables dentro de la misma clase

# Si una variable comienza con "__" (doble guión bajo), que inaccesible desde fuera de la clase

class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalle(self):
        print(f"Persona: {self._nombre}, {self._apellido} - {self._edad} años")

persona1 = Persona("Roberto", "Mejias", 29)
persona1.mostrar_detalle()

separador()
tituloEjercicio(74, "Métodos set y get en Python").generarTitulo()
