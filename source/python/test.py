from podio import Podio


def main():

    print('========================================================')
    print('==                        Test                        ==')
    print('========================================================')

    podio = Podio()

    podio.cargar()
    podio.desplegar()
    podio.cargar_puntaje('jtsoya539', 37)
    #podio.cargar_puntaje('catnip', 120)
    #podio.cargar_puntaje('ameza', 100)

    podio._actualizar()

    podio.desplegar()


if __name__ == '__main__':
    main()
