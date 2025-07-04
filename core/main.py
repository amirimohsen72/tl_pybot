import telebot
import os


API_TOKEN = os.environ.get("API_TOKEN")
print(API_TOKEN)
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(['command1','command2'])
@bot.message_handler()
def send_wellcome(message):
    if message.text == 'start' :
        print(1111)


bot.infinity_polling()

