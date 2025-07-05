# tl_pybot
telegram bot


to access bot api:
https://api.telegram.org/bot<token>/METHOD_NAME


docoument for read in docs folder.

 auth:
 telebot.TeleBot('API_TOKEN_String')

 message handler(get) and send messega (send):
 @bot.message_handler()
def send_wellcome(message):
    if message.text == 'start' :
        bot.send_message(message.chat.id,'خوش آمدید')

