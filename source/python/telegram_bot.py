"""
Modulo telegram_bot.py
"""
import logging
import random
import telegram
import emoji
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import CallbackQueryHandler
from telegram.ext import Filters
from dog_api import DogAPI
from podio import Podio


def main():
    API_TOKEN = '466722132:AAG-i_NBJB25CyLdXUocW_B-gIIl81dQosM'
    bot = telegram.Bot(token=API_TOKEN)
    updater = Updater(token=API_TOKEN)
    dispatcher = updater.dispatcher

    razas = []
    opciones = []

    api = DogAPI()
    podio = Podio()

    # api.actualizar_razas()
    razas = api.obtener_razas()
    podio.cargar()

    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    def start(bot, update):
        bot.send_message(chat_id=update.message.chat_id,
                         text="Hola! Soy Jagua Maravichu Bot")

    def jugar(bot, update):
        imagen = api.obtener_imagen()
        bot.send_photo(chat_id=update.message.chat_id, photo=imagen['url'])
        bot.send_message(chat_id=update.message.chat_id,
                         text="¿Qué raza es?")
        opciones = random.choices(razas, k=2)
        opciones.append(imagen['raza'])
        random.shuffle(opciones)

        teclado = []
        for opcion in opciones:
            correcto = 'N'
            if opcion == imagen['raza']:
                correcto = 'S'

            teclado.append([telegram.InlineKeyboardButton(
                text=opcion.replace('-', ' ').title(), callback_data=correcto)])

        reply_markup = telegram.InlineKeyboardMarkup(teclado)
        bot.send_message(chat_id=update.message.chat_id,
                         text="Elegí tu respuesta",
                         reply_markup=reply_markup)

        telegram.ReplyKeyboardRemove()

    def respuesta(bot, update):
        mensaje = emoji.emojize(
            'Incorrecto. Tenés que tomar un curso sobre razas caninas :thumbsdown:', use_aliases=True)
        if update.callback_query.data == 'S':
            mensaje = emoji.emojize(
                'Correcto!! :tada: :tada: Sabés mucho sobre razas caninas :clap: :clap:', use_aliases=True)

        bot.answer_callback_query(update.callback_query.id, text=mensaje)
        bot.send_message(chat_id=update.callback_query.message.chat_id,
                         text=mensaje)

    def unknown(bot, update):
        bot.send_message(chat_id=update.message.chat_id,
                         text="Disculpame, no entiendo ese comando")

    start_handler = CommandHandler('start', start)
    jugar_handler = CommandHandler('jugar', jugar)
    respuesta_handler = CallbackQueryHandler(respuesta)
    unknown_handler = MessageHandler(Filters.command, unknown)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(jugar_handler)
    dispatcher.add_handler(respuesta_handler)
    dispatcher.add_handler(unknown_handler)

    updater.start_polling()
    # updater.idle()


if __name__ == '__main__':
    main()
