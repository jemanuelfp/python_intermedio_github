from Humano import Humano

class Mujer(Humano):
    def __init__(self, nombre, color_cabello,nacionalidad):
        super().__init__(nombre, color_cabello, nacionalidad)
        self.genero = 'Femenino'


class Hombre(Humano):
    def __init__(self, nombre, color_cabello,nacionalidad):
        super().__init__(nombre, color_cabello, nacionalidad)
        self.genero = 'Masculino'

