"""
Modulo dog_api.py
"""

import socket
import json
import pickle
import urllib.request
import urllib.parse
import os.path


class DogAPI():

    """ Clase DogAPI """

    _URL_IMAGEN = 'https://dog.ceo/api/breeds/image/random'
    _URL_RAZAS = 'https://dog.ceo/api/breeds/list/all'

    def __init__(self):
        pass

    def _hay_conexion(self):
        try:
            socket.create_connection(('www.google.com', 80))
            return True
        except OSError:
            pass
        return False

    def _obtener_url(self, url):
        with urllib.request.urlopen(url) as respuesta:
            for linea in respuesta:
                linea = linea.decode('utf-8')

        return linea

    def _compacta_razas(self, mensaje):
        compactado = []
        for raza, subrazas in mensaje.items():
            if len(subrazas) > 0:
                for subraza in subrazas:
                    compactado.append(raza + '-' + subraza)
            else:
                compactado.append(raza)

        return compactado

    def obtener_imagen(self):
        ruta = ''
        ruta_secciones = []

        objeto_json = json.loads(self._obtener_url(self._URL_IMAGEN))
        estado = objeto_json['status']
        mensaje = objeto_json['message']

        # Parsea el componente <path> del url
        ruta = urllib.parse.urlparse(mensaje)[2]

        # Carga las secciones de la ruta en una lista
        while ruta != '/':
            temp = os.path.split(ruta)
            ruta = temp[0]
            ruta_secciones.append(temp[1])

        return dict(url=mensaje, raza=ruta_secciones[1])

    def actualizar_razas(self):
        razas = []

        objeto_json = json.loads(self._obtener_url(self._URL_RAZAS))
        estado = objeto_json['status']
        mensaje = objeto_json['message']

        # Compacta mensaje y convierte en una lista
        razas = self._compacta_razas(mensaje)

        archivo = open(r'razas.pickle', 'wb')
        pickle.dump(razas, archivo)
        archivo.close()

    def obtener_razas(self):
        razas = []

        archivo = open(r'razas.pickle', 'rb')
        razas = pickle.load(archivo)
        archivo.close()

        return razas
