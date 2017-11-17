"""
Modulo main.py
"""
import random
from dog_api import DogAPI


def main():

    print('=========================================================')
    print('==                   Jagua Maravichu                   ==')
    print('=========================================================')
    razas = []
    opciones = []

    api = DogAPI()

    # api.actualizar_razas()
    razas = api.obtener_razas()

    while True:
        jugar = input("Jugar? (S/N): ")
        if jugar in ('N', 'n'):
            return False

        if not api._hay_conexion():
            print('No hay conexion a Internet :(')
            return False

        imagen = api.obtener_imagen()
        print(imagen['url'])

        print('¿Qué raza es?')

        opciones = random.choices(razas, k=2)
        opciones.append(imagen['raza'])
        random.shuffle(opciones)

        for indice, opcion in enumerate(opciones):
            print(str(indice) + ') ' + opcion)

        respuesta = int(input("Ingrese su respuesta: "))

        if respuesta == opciones.index(imagen['raza']):
            print('Correcto!! Usted sabe mucho sobre razas caninas :D')
        else:
            print('Incorrecto. Usted debe tomar un curso sobre razas caninas D:')

        opciones.clear()


if __name__ == '__main__':
    main()
