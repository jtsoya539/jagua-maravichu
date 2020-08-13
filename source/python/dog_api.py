"""
Realizar la conexion con Dog API.
"""

import json
import os.path
import pickle
import socket
import urllib.parse
import urllib.request


class DogAPI():
    """
    Realizar la conexion con Dog API.
    """

    _URL_IMAGEN = 'https://dog.ceo/api/breeds/image/random'
    _URL_RAZAS = 'https://dog.ceo/api/breeds/list/all'

    def __init__(self):
        pass

    def _obtener_url(self, url):
        """
        Obtener respuesta a una solicitud HTTP a partir de una URL.
        """
        with urllib.request.urlopen(url) as respuesta:
            return respuesta.read().decode('utf-8')

    def _listar_razas(self, objeto_json):
        """
        Convertir JSON de todas las razas y subrazas en una unica lista
        """
        lista = []
        for raza, subrazas in objeto_json.items():
            if len(subrazas) > 0:
                for subraza in subrazas:
                    lista.append(raza + '-' + subraza)
            else:
                lista.append(raza)

        return lista

    def hay_conexion(self):
        """
        Comprobar si hay conexion a Internet.
        Retornar True si hay conexion, False si no hay conexion.
        """
        try:
            socket.create_connection(('www.google.com', 80))
            return True
        except OSError:
            pass
        return False

    def obtener_imagen(self):
        """
        Obtener una imagen al azar de entre todas las razas.
        Retornar un diccionario con los valores url y raza.
        """
        ruta = ''
        ruta_secciones = []

        objeto_json = json.loads(self._obtener_url(self._URL_IMAGEN))
        estado = objeto_json['status']
        mensaje = objeto_json['message']

        # Parsear el componente <path> del URL
        ruta = urllib.parse.urlparse(mensaje)[2]

        # Cargar las secciones de la ruta en una lista
        while ruta != '/':
            temp = os.path.split(ruta)
            ruta = temp[0]
            ruta_secciones.append(temp[1])

        return dict(url=mensaje, raza=ruta_secciones[1])

    def actualizar_razas(self):
        """
        Actualizar el archivo .pickle con la lista de todas las razas.
        """
        razas = []

        objeto_json = json.loads(self._obtener_url(self._URL_RAZAS))
        estado = objeto_json['status']
        mensaje = objeto_json['message']

        # Convierte JSON de todas las razas y subrazas en una unica lista
        razas = self._listar_razas(mensaje)

        archivo = open(r'razas.pickle', 'wb')
        pickle.dump(razas, archivo)
        archivo.close()

    def obtener_razas(self):
        """
        Obtener una lista de todas las razas desde el archivo .pickle.
        """
        razas = []

        archivo = open(r'razas.pickle', 'rb')
        razas = pickle.load(archivo)
        archivo.close()

        return razas
