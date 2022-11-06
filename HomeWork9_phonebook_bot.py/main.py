from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, ConversationHandler, Filters

import model

bot_token = '5690495817:AAEl1eYizdmrmp09S7xBoIOuC_SpEDBlWzM'
bot = Bot(bot_token)
updater = Updater(bot_token, use_context=True)
dispatcher = updater.dispatcher

add_storage = []

def start(update, context):
    context.bot.send_message(
        update.effective_chat.id,
        f"Привет! Я бот-телефонный справочник!\n"
        f"/watch - Посмотреть контакты\n"
        f"/add - Добавить контакт\n"
        f"/find - Найти контакт\n"
        f"/delete - Удалить контакт\n")

def watch(update, context):  
    data = model.read_csv()
    context.bot.send_message(
        update.effective_chat.id,
        f"{data}")
        
def find(update, context):
    context.bot.send_message(
        update.effective_chat.id,
        f"Введите Фамилию")
    return 1

def find_surname(update, context):
    surname = update.message.text
    res = model.find(surname)
    context.bot.send_message(
        update.effective_chat.id,
        f"{res}")


def add(update, context):
    context.bot.send_message(
        update.effective_chat.id,
        f"Введите имя")
    return 1

def add_name(update, context):
    name = update.message.text
    add_storage.append(name)
    context.bot.send_message(
        update.effective_chat.id,
        f"Введите фамилию")
    return 2


def add_surname(update, context):
    surname = update.message.text
    add_storage.append(surname)
    context.bot.send_message(
        update.effective_chat.id,
        f"Введите номер телефона")
    return 3

def add_phone(update, context):
    phone = update.message.text
    add_storage.append(phone)
    model.add_info(add_storage)
    context.bot.send_message(
        update.effective_chat.id,
        f"Запись добавлена\n Для выхода введите /stop")
    add_storage.clear()

def delete_contact(update, context):
    index_contact = update.message.text
    index_contact = int(index_contact)
    msg = model.del_info(index_contact)
    context.bot.send_message(
        update.effective_chat.id,
        f"информация удалена")
   
def delete(update, context):
    context.bot.send_message(
        update.effective_chat.id,
        f"Введите Index")
    return 1

def stop(update, context):
    update.message.reply_text("Всего доброго!")
    return ConversationHandler.END

add_handler = ConversationHandler(
    entry_points=[CommandHandler('add', add)],
    states={
        1: [MessageHandler(Filters.text & ~Filters.command, add_name)],
        2: [MessageHandler(Filters.text & ~Filters.command, add_surname)],
        3: [MessageHandler(Filters.text & ~Filters.command, add_phone)],
    },
    fallbacks=[CommandHandler('stop', stop)]
)

find_handler = ConversationHandler(
    entry_points=[CommandHandler('find', find)],
    states={
        1: [MessageHandler(Filters.text & ~Filters.command, find_surname)],
        
    },
    fallbacks=[CommandHandler('stop', stop)]
)

delete_handler = ConversationHandler(
    entry_points=[CommandHandler('delete', delete)],
    states={
        1: [MessageHandler(Filters.text & ~Filters.command, delete_contact)],
    },
    fallbacks=[CommandHandler('stop', stop)]
)

start_handler = CommandHandler('start', start)
back_handler = CommandHandler('back', start)
watch_handler = CommandHandler('watch', watch)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(watch_handler)
dispatcher.add_handler(find_handler)
dispatcher.add_handler(add_handler)
dispatcher.add_handler(delete_handler)
updater.start_polling()
updater.idle()