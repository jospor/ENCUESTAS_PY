
class Encuesta:
    def __init__(self, nombre, preguntas=[], respuestas=[]):
        self.nombre = nombre
        self.preguntas = preguntas
        self.respuestas = respuestas

    def mostrar(self):
        return self.nombre, self.preguntas

class EncuestaLimitadaEdad(Encuesta):
    def __init__(self, nombre, edad_minima, edad_maxima, preguntas=[], respuestas=[]):
        super().__init__(nombre, preguntas, respuestas)
        self.edad_minima = edad_minima
        self.edad_maxima = edad_maxima

class EncuestaLimitadaRegion(Encuesta):
    def __init__(self, nombre, regiones, preguntas=[], respuestas=[]):
        super().__init__(nombre, preguntas, respuestas)
        self.regiones = regiones