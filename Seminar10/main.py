import logging
import random

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters

reply_keyboard = [['/play', '/info', '/close']]
stop_keyboard = [['/stop']]

markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
stop_markup = ReplyKeyboardMarkup(stop_keyboard, one_time_keyboard=False)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

TOKEN = '5752718030:AAEBGLw2EdizW2nMPoKnSCUCvYTG4baDFpc'

candy = 0
def start(update, context):
    update.message.reply_text(
        "Привет! Давай играть!",
        reply_markup=markup
    )

def play(update, context):
    update.message.reply_text('Введите колличество конфет в игре', reply_markup=stop_markup)
    return 1

def play_get_candy(update, context):
    global candy
    candy = int(update.message.text)
    update.message.reply_text('Сколько кофент вы возьмете?')
    return 2

def player_1(update, context):
    global candy
    try:
        candy -= int(update.message.text)
        update.message.reply_text(f'Конфет осталось: {candy}')
        if candy>28:
            temp = random.randint(1,28)
            candy -= temp
            update.message.reply_text(f'Бот взял {temp} конфет. Конфет осталось: {candy}')
            if candy>28:
                update.message.reply_text('Сколько кофент вы возьмете?')
            else:
                update.message.reply_text(f'Вы победили 🦞', reply_markup=markup)
                context.bot.send_document(chat_id=update.effective_chat.id, document='https://liubavyshka.ru/_ph/80/2/868450491.gif?1667846726')
                return ConversationHandler.END
            return 2
        else:
            update.message.reply_text('Победил бот', reply_markup=markup)
            return ConversationHandler.END
    except ValueError:
        update.message.reply_text('Введите число')
        return 2

def stop(update, context):
    update.message.reply_text("Всего доброго!", reply_markup=markup)
    return ConversationHandler.END

def info(update, context):
    update.message.reply_text(
        "Правила игры")

def close(update, context):
    update.message.reply_text(
        "Спасибо за игру!",
    reply_markup=ReplyKeyboardRemove())


play_handler = ConversationHandler(
        entry_points=[CommandHandler('play', play)],

        # Состояние внутри диалога.
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, play_get_candy)],
            2: [MessageHandler(Filters.text & ~Filters.command, player_1)],
        },

        # Точка прерывания диалога. В данном случае — команда /stop.
        fallbacks=[CommandHandler('stop', stop)]
    )


def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(play_handler)
    dp.add_handler(CommandHandler("info", info))
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("close", close))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()