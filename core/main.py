import telebot
import os
import sqlite3

MAIN_DB = sqlite3.connect('test_db.db',check_same_thread=False)
MAIN_CURSOR = MAIN_DB.cursor()

dir = os.path.dirname(os.path.abspath(__file__))
# file_path = os.path.join(dir, "test.txt")


API_TOKEN = os.environ.get("API_TOKEN")
print(API_TOKEN)
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(['start'], func = lambda message:True)
def keyboard_keyword(message):
    MAIN_CURSOR.execute("select * from users where chat_id = '"+ str(message.chat.id) +"'")
    result = MAIN_CURSOR.fetchone()
    if result :
        msg = "سلام . عملیات را انتخاب کنید"
    else:
        MAIN_CURSOR.execute("insert into users (chat_id , status) values ('"+ str(message.chat.id) + "','start')")
        MAIN_DB.commit()
        msg = 'ثبت نام موفق . چه کمکی ازم بر میاد ؟'
    # markup= telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4,input_field_placeholder='از دکمه کیورد شورتکات انتخاب نمایید', one_time_keyboard=True).add('تست1')
    markup= telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4,input_field_placeholder='از دکمه کیورد شورتکات انتخاب نمایید', one_time_keyboard=True)
    markup.add('حذف کیوورد')
    markup.add('mahsol1','نمایش اطلاعات من')
    bot.send_message(message.chat.id,msg,reply_markup=markup)

@bot.message_handler(['action'], func = lambda message:True)
def keyboard_shishee(message):
    markup= telebot.types.InlineKeyboardMarkup()
    button1= telebot.types.InlineKeyboardButton('سایت',url='https://tihoopharma.ir')
    button2= telebot.types.InlineKeyboardButton('کلید2',callback_data='testcall')
    button3= telebot.types.InlineKeyboardButton('تکمیل نام',callback_data='name_update')
    markup.add(button1)
    markup.add(button2,button3)
    bot.send_message(message.chat.id,'عملیات را انتخاب کنید',reply_markup=markup)
     
@bot.callback_query_handler(func=lambda call:True)
def testcallfunction(call):
    if call.data == 'testcall' :
        bot.send_message(call.message.chat.id,call.data)
    elif call.data == 'name_update' :
        MAIN_CURSOR.execute("update users set  name ='amir' , status='name' where chat_id='"+ str( call.message.chat.id) + "'")
        MAIN_DB.commit()
        bot.send_message(call.message.chat.id,'status name')

# @bot.message_handler(content_types=['voice','document'])
@bot.message_handler()
def send_wellcome(message):
    if message.text == 'start' :
        bot.send_message(message.chat.id,'خوش آمدید')

    elif message.text.startswith('سلام') or message.text.startswith('hi') :
        bot.send_message(message.chat.id,'علیک سلام')

    elif message.text == 'حذف کیوورد'  :
        bot.send_message(message.chat.id,'شروع مجدد', reply_markup=telebot.types.ReplyKeyboardRemove())

    elif message.text == 'نمایش اطلاعات من'  :
        MAIN_CURSOR.execute("select * from users where chat_id='"+str(message.chat.id)+"'")
        user = MAIN_CURSOR.fetchone()
        jsdc = str(user[2] + ' ' + ' status :' + user[4])
        bot.send_message(message.chat.id,jsdc)

    elif message.text.startswith('file')  :
        # with open('testfile.txt','rb') as file:
        with open('core/testfile.txt','rb') as file:
            bot.send_document(message.chat.id,file)
        print('file')
    else :
        bot.reply_to(message, 'پیام دریافت شد . بعد از بررسی پاسخ خواهیم داد')


bot.infinity_polling()

