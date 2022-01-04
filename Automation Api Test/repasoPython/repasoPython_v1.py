from Generic.formateoArchivos.tituloEjercicio import tituloEjercicio
from Generic.formateoArchivos.separador import separador

separador = separador()

# Llamo al constructo de titulos de ejercicios:
titulo = tituloEjercicio('1- Automatizacion de Apis','Repaso de Python').generarTitulo()

# Imprimir por consola
separador.separador()
nombre = "Leandro Micciche"
print(f"Hola mi nombre es: {nombre}")


# Arreglos:
separador.separador()
paises = ['Argentina', 'Chile', 'Uruguay', 'Paraguay']
print(f'Mostrar el primer pais: {paises[0]}')

# Muestro todos los paises del array:
separador.separador()
print('Muestro todos los paises de la lista')
n = 1
for pais in paises:
    print(f'{n} - {pais}')
    n = n + 1

# Agrego un pais a la lista y lo muestro:
separador.separador()
paises.append('Bolivia')
print('Muestro todos los paises de la lista')
n = 1
for pais in paises:
    print(f'{n} - {pais}')
    n = n + 1
