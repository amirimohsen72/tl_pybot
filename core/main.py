import telebot
import os


API_TOKEN = os.environ.get("API_TOKEN")
print(API_TOKEN)
bot = telebot.TeleBot(API_TOKEN)



bot.infinity_polling()

