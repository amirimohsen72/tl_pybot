import telebot
import sqlite3


MAIN_DB = sqlite3.connect('test_db.db', check_same_thread = False)
MAIN_CURSOR = MAIN_DB.cursor()


bot = telebot.TeleBot('6655143587:AAEAvISP-vSPdZtXUlVXqsdKykVkjPmmYdI')

markup = telebot.types.ReplyKeyboardMarkup(True, True)
markup.add('شروع 🚀✅', 'نمایش اطلاعات 📢')


@bot.message_handler(['start'])
def send_welcome(message):
    MAIN_CURSOR.execute("SELECT * FROM users2 WHERE chat_id='" + str(message.chat.id) + "'")
    result = MAIN_CURSOR.fetchone()
    if result:
        bot.send_message(message.chat.id, 'سلام 😎💖', reply_markup = markup)
    else:
        MAIN_CURSOR.execute("INSERT INTO users2 (chat_id, status) VALUES ('" + str(message.chat.id) + "', 'start')")
        MAIN_DB.commit()
        bot.send_message(message.chat.id, 'ثبت نام شدید 😎✅', reply_markup = markup)


@bot.message_handler(func = lambda message: True)
def get_data(message):
    if message.text == 'شروع 🚀✅':
        bot.send_message(message.chat.id, 'نام را وارد کنید', reply_markup = telebot.types.ReplyKeyboardRemove())
        MAIN_CURSOR.execute("UPDATE users2 SET status='name' WHERE chat_id='" + str(message.chat.id) + "'")
        MAIN_DB.commit()
    elif message.text == 'نمایش اطلاعات 📢':
        MAIN_CURSOR.execute("SELECT * FROM users2 WHERE chat_id='" + str(message.chat.id) + "'")
        result = MAIN_CURSOR.fetchone()
        bot.send_message(message.chat.id, f'''
🔰 اطلاعات
    سن شما ```{result[1]}```
    نام شما ```{result[2]}```
    نام خانوادگی شما ```{result[3]}```
⚡🎃
''', parse_mode='Markdown')
    else:
        MAIN_CURSOR.execute("SELECT status FROM users2 WHERE chat_id='" + str(message.chat.id) + "'")
        result = MAIN_CURSOR.fetchone()
        if result:
            if result[0] == 'name':
                bot.send_message(message.chat.id, 'نام خانوادگی رو بده')
                MAIN_CURSOR.execute("UPDATE users2 SET status='last_name', name='" + message.text + "' WHERE chat_id='" + str(message.chat.id) + "'")
                MAIN_DB.commit()
            elif result[0] == 'last_name':
                bot.send_message(message.chat.id, 'سن رو بده')
                MAIN_CURSOR.execute("UPDATE users2 SET status='age', last_name='" + message.text + "' WHERE chat_id='" + str(message.chat.id) + "'")
                MAIN_DB.commit()
            elif result[0] == 'age':
                bot.send_message(message.chat.id, 'سلام 😎💖', reply_markup = markup)
                MAIN_CURSOR.execute("UPDATE users2 SET status='start', age='" + message.text + "' WHERE chat_id='" + str(message.chat.id) + "'")
                MAIN_DB.commit()
        else:
            bot.send_message(message.chat.id, 'برو ثبت نام کن اول')




bot.infinity_polling()