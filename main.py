"""
Modulo main.py
"""
import random

from dog_api import DogAPI
from podio import Podio


def main():

    ancho = 72
    print('=' * ancho)
    print('Jagua Maravichu'.center(ancho))
    print('=' * ancho)
    razas = []
    opciones = []

    api = DogAPI()
    podio = Podio()

    # api.actualizar_razas()
    razas = api.obtener_razas()
    podio.cargar()

    while True:
        jugar = input("¿Querés jugar? (S/N): ")
        if jugar in ('N', 'n'):
            break

        nombre = input('¿Cuál es tu nombre?: ')
        cantidad = int(input('¿Cuántas adivinanzas querés hacer?: '))
        correctas = 0
        incorrectas = 0
        puntos = 0

        for i in range(cantidad):

            if not api._hay_conexion():
                print('No hay conexión a Internet </3')
                break

            print((' Pregunta No. ' +
                   str(i + 1) + ' ').center(ancho, '-'))

            imagen = api.obtener_imagen()
            print(imagen['url'])

            print('¿Qué raza es?')

            opciones = random.choices(razas, k=2)
            opciones.append(imagen['raza'])
            random.shuffle(opciones)

            for indice, opcion in enumerate(opciones):
                print(str(indice) + ') ' + opcion)

            respuesta = int(input("Escribí tu respuesta: "))

            if respuesta == opciones.index(imagen['raza']):
                print('Correcto!! Sabés mucho sobre razas caninas :D')
                correctas = correctas + 1
            else:
                print('Incorrecto. Tenés que tomar un curso sobre razas caninas D:')
                incorrectas = incorrectas + 1

            opciones.clear()

        if cantidad > 0:
            puntos = round(((correctas / cantidad) * 100), 2)

        print(nombre + ', tu puntaje final es: ' + str(puntos))
        podio.cargar_puntaje(nombre, puntos)

        print(' Puntuaciones '.center(ancho, '='))
        podio.desplegar()

    podio._actualizar()
    print('Chauuu!! Nos vemos pronto woof woof')


if __name__ == '__main__':
    main()
