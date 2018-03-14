import telebot
import datetime

from telebot import types

# from telegram import InlineKeyboardButton, InlineKeyboardMarkup

id = '548881516'
bot = telebot.TeleBot("548881516:AAG04_NagirMSOMkKuY145WLAMdPrsmI6NE")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, text='Hi! I`m time-bot Chormie, what do you want to know? '
                               '(Use /help to see all commands)')


@bot.message_handler(commands=['help'])
def send_commands(message):
    bot.reply_to(message, text='use /time to know time right now'
                               'use /data to know current data'
                               'use /choose if you want to use buttons'
                               )

@bot.message_handler(commands=['time'])
def send_welcome(message):
    bot.reply_to(message, datetime.datetime.now().time())


@bot.message_handler(commands=['date'])
def send_welcome(message):
    bot.reply_to(message, datetime.date.today())


markup = types.ReplyKeyboardMarkup(row_width=0.5)
itembtn1 = types.KeyboardButton('/time')
itembtn2 = types.KeyboardButton('/date')

markup.add(itembtn1, itembtn2)

@bot.message_handler(commands='choose')
def choosebtn(message) :
    bot.reply_to(message, "Choose one letter:", reply_markup=markup)


bot.polling(none_stop=True)
