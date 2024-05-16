
class Usuario:
    def __init__(self, correo, edad, region):
        self.correo = correo
        self.edad = edad
        self.region = region

    def contestar_encuesta(self, encuesta, respuestas):
        encuesta.respuestas.append(respuestas)