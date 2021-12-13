print("----------------------------------------------------")
print("Leccion 9.62")
print("---- Clases y Objetos en Python: Metodo de Instancia en Python  ----")

class Aritmetica:
    # El comentario de abajo es utilizado para realizar documentacion de nuestras clases llamado docString, se utiliza con triple comillas simples o dobles.
    """
    Clase Aritmetica para realizar las operaciones de sumar, restar, ect...

    """

    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def sumar(self):
        return self.number1 + self.number2

    def restar(self):
        return self.number1 - self.number2

    def multiplicar(self):
        return  self.number1 * self.number2

    def dividir(self):
        if self.number2 == 0:
            print('No se puede dividir por 0')
        else:
            return  self.number1 / self.number2


# Creo el obejto aritmetica1
aritmetica1 = Aritmetica(11, 3)

# Muestro y hago la llamada de los metodos de la clase Aritmetica
print(f'El resultado de la suma es: {aritmetica1.sumar()}')
print(f'El resultado de la resta es: {aritmetica1.restar()}')
print(f'El resultado de la multiplicacion es: {aritmetica1.multiplicar()}')
print(f'El resultado de la division es: {aritmetica1.dividir():.2f}') # ":.2f se indica cuantos decimales se quiere mostrar"
