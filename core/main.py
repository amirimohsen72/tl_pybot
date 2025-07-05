import telebot
import os

dir = os.path.dirname(os.path.abspath(__file__))
# file_path = os.path.join(dir, "test.txt")


API_TOKEN = os.environ.get("API_TOKEN")
print(API_TOKEN)
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(['action'], func = lambda message:True)
def keyboard_shishee(message):
    markup= telebot.types.InlineKeyboardMarkup()
    button1= telebot.types.InlineKeyboardButton('سایت',url='https://tihoopharma.ir')
    button2= telebot.types.InlineKeyboardButton('کلید2',callback_data='testcall')
    button3= telebot.types.InlineKeyboardButton('کلید3',callback_data='test2')
    markup.add(button1)
    markup.add(button2,button3)
    bot.send_message(message.chat.id,'عملیات را انتخاب کنید',reply_markup=markup)
     
@bot.callback_query_handler(func=lambda call:True)
def testcallfunction(call):
    if call.data == 'testcall' :
        bot.send_message(call.message.chat.id,call.data)
    elif call.data == 'test2' :
        bot.send_message(call.message.chat.id,'ressspns')

# @bot.message_handler(content_types=['voice','document'])
@bot.message_handler()
def send_wellcome(message):
    if message.text == 'start' :
        bot.send_message(message.chat.id,'خوش آمدید')

    elif message.text.startswith('سلام') or message.text.startswith('hi') :
        bot.send_message(message.chat.id,'علیک سلام')

    elif message.text.startswith('file')  :
        # with open('testfile.txt','rb') as file:
        with open('core/testfile.txt','rb') as file:
            bot.send_document(message.chat.id,file)
        print('file')
    else :
        bot.reply_to(message, 'پیام دریافت شد . بعد از بررسی پاسخ خواهیم داد')


bot.infinity_polling()

