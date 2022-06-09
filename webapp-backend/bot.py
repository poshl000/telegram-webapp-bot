import uuid
import telebot
from telebot import types, TeleBot
import database.repository as repository
import datetime
import components.product as product
import config.app as app

bot = telebot.TeleBot(app.telegram_key(), parse_mode=None)

def open_shop_keyboard():
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    Catalog = types.KeyboardButton('🛒 STOREFRONT 🌐', web_app=types.WebAppInfo(url='https://cyberseeds.io/tgwebapp/index.html'))
    keyboard.add(Catalog)
    return keyboard

@bot.message_handler(commands=['contact'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Contact us: @echo123")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, " 🌱 Welcome to the shop")
    bot.send_message(message.chat.id, " 🛒 OPEN STOREFRONT 🌐 TO MAKE ORDER ↓", reply_markup=open_shop_keyboard())

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    o = repository.get_last_order_sum(message.chat.id, message.text)
    if(o):
        bot.send_message(message.chat.id, "OK\!\SEND {}$ to card `4111 1111 1111 1111`\nWe await for the payment :\-\)".format(o), parse_mode='MarkdownV2')
    else:
        bot.send_message(message.chat.id, " 🛒 OPEN STOREFRONT 🌐 TO MAKE ORDER ↓", reply_markup=open_shop_keyboard())

# handle webapp order
@bot.message_handler(content_types=['web_app_data'])
def echo_yall(message):
    repository.create_order(message.chat.id, message.from_user.username, message.web_app_data.data, uuid.uuid4(), datetime.datetime.now())

    bot.send_message(message.chat.id, "Thank you for the order!")
    bot.send_message(message.chat.id, "Send deivery details in format:\n\n`City, Street, Appartments, Phone number`\nDelivery costs {}$".format(product.get_delivery_price()), parse_mode='MarkdownV2')

bot.infinity_polling()
