import telebot
import os


API_TOKEN = os.environ.get("API_TOKEN")
print(API_TOKEN)
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(['command1','command2'])
@bot.message_handler()
def send_wellcome(message):
    if message.text == 'start' :
        bot.send_message(message.chat.id,'خوش آمدید')
        print(1111)
    elif message.text.startswith('سلام') or message.text.startswith('hi') :
        bot.send_message(message.chat.id,'علیک سلام')
        print(1111)
    else :
        bot.send_message(message.chat.id, 'پیام دریافت شد . بعد از بررسی پاسخ خواهیم داد')


bot.infinity_polling()

