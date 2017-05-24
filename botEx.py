from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,ConversationHandler)

import logging

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Bienvenido, nuevo usuario. \nEste bot se encarga de notificar y procesar los cobros de peaje y parqueo del sistema automatizado.")
    bot.send_message(chat_id=update.message.chat_id, text="Para iniciar, ingrese su # de placa para que pueda ser ingresado en el sistema.")
    placa = getPlaca(bot, update)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
logger = logging.getLogger(__name__)

updater = Updater(token="367979567:AAG9MlxEjb1dontUthBCvtTrIsxLLEP8DrU")
dispatcher = updater.dispatcher
start_handler = CommandHandler('start',start)
dispatcher.add_handler(start_handler)

updater.start_polling()


def getPlaca(bot, update):
    user = update.message.from_user
    logger.info("License of %s: %s" % (user.first_name, update.message.text))
    placa = int(message.text)
    update.message.reply_text('Todo listo. Ahora recibiras una notificacion cada vez que haya un cobro pendiente.',
                              reply_markup=ReplyKeyboardRemove())

    return placa
