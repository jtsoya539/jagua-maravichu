"""
Manejar un podio con los mejores puntajes.
"""
import pickle


class Podio():
    """
    Manejar un podio con los mejores puntajes.
    """

    puntajes = []

    def __init__(self):
        """
        Construir un podio con 10 puntajes vacios.
        """
        for i in range(10):
            puntaje = dict(nombre='', puntos=0)
            self.puntajes.append(puntaje)

    def actualizar(self):
        """
        Actualizar el archivo .pickle con la lista de puntajes.
        """
        archivo = open(r'podio.pickle', 'wb')
        pickle.dump(self.puntajes, archivo)
        archivo.close()

    def cargar(self):
        """
        Cargar la lista de puntajes desde el archivo .pickle.
        """
        archivo = open(r'podio.pickle', 'rb')
        self.puntajes = pickle.load(archivo)
        archivo.close()

    def ingresar_puntaje(self, nombre, puntos):
        """
        Ingresar un nuevo puntaje al podio.
        """
        for posicion, puntaje in enumerate(self.puntajes):
            if puntos >= puntaje['puntos']:
                self.puntajes.insert(posicion, dict(
                    nombre=nombre, puntos=puntos))
                self.puntajes.pop()
                break

    def desplegar(self):
        """
        Desplegar el podio en la consola.
        """
        for puntaje in self.puntajes:
            print('Nombre: ' + str(puntaje['nombre']).ljust(15) +
                  ' Puntos: ' + ('%.2f' % puntaje['puntos']).rjust(6))

    def to_string(self):
        """
        Retornar una cadena que representa el podio.
        """
        cadena = ''
        for puntaje in self.puntajes:
            cadena = cadena + 'Nombre: ' + \
                str(puntaje['nombre']).ljust(15) + ' Puntos: ' + \
                ('%.2f' % puntaje['puntos']).rjust(6) + '\n'

        return cadena
