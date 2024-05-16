
class Pregunta:
    def __init__(self, enunciado, ayuda=None, requerida=False, alternativas=[]):
        self.enunciado = enunciado
        self.ayuda = ayuda
        self.requerida = requerida
        self.alternativas = alternativas

    def mostrar(self):
        return self.enunciado, self.ayuda, self.alternativas