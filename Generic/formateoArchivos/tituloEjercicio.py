class tituloEjercicio:

    def __init__(self, numeroLeccion, titulo):
        self.numeroLeccion = numeroLeccion
        self.titulo = titulo

    def generarTitulo(self):
        print(f'---- {self.numeroLeccion} ----')
        print(f"---- {self.titulo} ----")