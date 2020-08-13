"""
Iniciar la aplicacion.
"""
import io
import random
import tkinter as tk
import urllib.request

from PIL import Image, ImageTk

from dog_api import DogAPI
from podio import Podio


class Aplicacion(tk.Frame):
    """
    Manejar la aplicacion y sus pantallas.
    """

    def __init__(self, master=None):
        """
        Construir la aplicacion.
        """
        super().__init__(master)

        self.api = DogAPI()
        self.podio = Podio()

        self.podio.cargar()
        self.razas = self.api.obtener_razas()

        self.iniciar_partida()
        self.pantalla_inicial()

    def iniciar_partida(self):
        """
        Iniciar valores para una partida nueva.
        """
        self.nombre = ''
        self.intentos = 0
        self.correctas = 0
        self.incorrectas = 0

    def limpiar_pantalla(self):
        """
        Limpiar la pantalla de la aplicacion.
        """
        for widget in self.master.winfo_children():
            widget.destroy()

    def pantalla_inicial(self):
        """
        Cargar la pantalla inicial.
        """
        self.limpiar_pantalla()

        logo = Image.open('logo.jpg', 'r')
        logo_tk = ImageTk.PhotoImage(logo)

        etiqueta1 = tk.Label(self.master, image=logo_tk)
        etiqueta1.image = logo_tk
        etiqueta1.pack()

        tk.Label(self.master, text='¡Bienvenido/a a Jagua Maravichu!').pack()
        tk.Label(self.master, text='Jagua Maravichu es un juego sencillo que prueba tu conocimiento sobre razas caninas.').pack()
        tk.Button(self.master, text='Jugar',
                  command=self.pantalla_nombre).pack()

    def pantalla_nombre(self):
        """
        Cargar la pantalla de ingreso de nombre.
        """
        self.limpiar_pantalla()

        tk.Label(self.master, text='¿Cuál es tu nombre?').pack()

        nombre = tk.StringVar(self.master, value='Escribí tu nombre acá')

        entrada = tk.Entry(self.master, textvariable=nombre)
        entrada.pack()

        def confirmar():
            self.nombre = nombre.get()
            self.pantalla_intentos()

        tk.Button(self.master, text='Confirmar', command=confirmar).pack()

        entrada.focus_set()
        entrada.selection_adjust(tk.END)
        entrada.bind("<Return>", (lambda event: confirmar()))

    def pantalla_intentos(self):
        """
        Cargar la pantalla de ingreso de intentos.
        """
        self.limpiar_pantalla()

        tk.Label(self.master, text='¡Hola ' + self.nombre + '!').pack()
        tk.Label(self.master, text='¿Cuántas adivinanzas querés hacer?').pack()

        intentos = tk.IntVar(self.master, value=0)

        entrada = tk.Entry(self.master, textvariable=intentos)
        entrada.pack()

        def confirmar():
            self.intentos = intentos.get()
            if self.intentos >= 1:
                self.pantalla_adivinanza(1)
            else:
                self.pantalla_inicial()

        tk.Button(self.master, text='Confirmar', command=confirmar).pack()

        entrada.focus_set()
        entrada.selection_adjust(tk.END)
        entrada.bind("<Return>", (lambda event: confirmar()))

    def pantalla_adivinanza(self, intento):
        """
        Cargar la pantalla de la adivinanza.
        """
        self.limpiar_pantalla()

        if not self.api.hay_conexion():
            tk.Label(self.master, text='No hay conexión a Internet </3').pack()
            tk.Button(self.master, text='Intentar de nuevo',
                      command=self.pantalla_inicial).pack()
            return

        tk.Label(self.master, text='Pregunta No. ' + str(intento)).pack()
        tk.Label(self.master, text='¿Qué raza es?').pack()

        raza = self.api.obtener_imagen()

        raza_raw = urllib.request.urlopen(raza['url']).read()

        imagen = Image.open(io.BytesIO(raza_raw))
        imagen_tk = ImageTk.PhotoImage(imagen)

        etiqueta1 = tk.Label(self.master, image=imagen_tk)
        etiqueta1.image = imagen_tk
        etiqueta1.pack()

        # tk.Label(self.master, text=raza['url']).pack()

        opciones = random.choices(self.razas, k=2)
        while raza['raza'] in opciones:
            opciones = random.choices(self.razas, k=2)

        opciones.append(raza['raza'])
        random.shuffle(opciones)

        respuesta = tk.IntVar(self.master, value=99)

        etiqueta2 = tk.Label(self.master, text='')

        grupo = tk.LabelFrame(
            self.master, text='Elegí tu respuesta', padx=10, pady=10)
        grupo.pack()

        def continuar():
            if intento < self.intentos:
                self.pantalla_adivinanza(intento + 1)
            else:
                self.pantalla_puntuaciones()

        def responder():
            if respuesta.get() == opciones.index(raza['raza']):
                etiqueta2['text'] = '¡Correcto!\n' + \
                    'Sabés mucho sobre razas caninas :D'
                self.correctas = self.correctas + 1
            else:
                etiqueta2['text'] = 'Incorrecto.\n' + \
                    'Tenés que tomar un curso sobre razas caninas :(\n' + \
                    'La respuesta correcta era ' + \
                    raza['raza'].replace('-', ' ').title() + '.'
                self.incorrectas = self.incorrectas + 1

            grupo.destroy()
            etiqueta2.pack()
            tk.Button(self.master, text='Continuar', command=continuar).pack()

            opciones.clear()

        for indice, opcion in enumerate(opciones):
            tk.Radiobutton(grupo, text=opcion.replace('-', ' ').title(), value=indice,
                           variable=respuesta, command=responder, indicatoron=0, width=40).pack(anchor='center')

    def pantalla_puntuaciones(self):
        """
        Cargar la pantalla de puntuaciones.
        """
        self.limpiar_pantalla()

        if self.intentos > 0:
            puntos = round(((self.correctas / self.intentos) * 100), 2)

        tk.Label(self.master, text=self.nombre +
                 ', tu puntaje final es: ' + str(puntos)).pack()

        self.podio.ingresar_puntaje(self.nombre, puntos)

        tk.Label(self.master, text=' Puntuaciones '.center(50, '=')).pack()
        tk.Label(self.master, text=self.podio.to_string()).pack()

        tk.Button(self.master, text='Jugar de nuevo',
                  command=self.pantalla_inicial).pack()

        self.podio.actualizar()
        self.iniciar_partida()


def main():
    """
    Iniciar la aplicacion.
    """
    root = tk.Tk()
    aplicacion = Aplicacion(root)
    aplicacion.master.title('Jagua Maravichu')
    aplicacion.master.minsize(1024, 768)
    aplicacion.mainloop()
    # root.destroy()


if __name__ == '__main__':
    main()
