"""
Modulo podio.py
"""


class Podio():

    """ Clase Podio """

    puntajes = []

    def __init__(self):
        for i in range(10):
            puntaje = dict(nombre='', puntos=0)
            self.puntajes.append(puntaje)

    def cargar_puntaje(self, nombre, puntos):
        for posicion, puntaje in enumerate(self.puntajes):
            if puntos >= puntaje['puntos']:
                self.puntajes.insert(posicion, dict(
                    nombre=nombre, puntos=puntos))
                self.puntajes.pop()
                break

    def desplegar(self):
        for puntaje in self.puntajes:
            print('Nombre: ' + puntaje['nombre'] +
                  ' Puntos: ' + str(puntaje['puntos']))
