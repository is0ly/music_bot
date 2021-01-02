import telebot
from settings import bot_token
from faunahelper import FaunaHelper
from faunadb.client import FaunaClient
from settings import fauna_key


#def greeting(name):
#    requests.get('https://api.telegram.org/bot%s/sendMessage' % bot_token,
#                 params={'chat_id': 397472277, 'text': f'Hi, {name}'})

bot = telebot.TeleBot(bot_token)
faunahelper = FaunaHelper(FaunaClient(fauna_key))


@bot.message_handler(commands=['getdays'])
def getdays(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "До конца курса осталось %s" % str(faunahelper.get_days_by_telegram_id(chat_id) + 1))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   bot.polling(none_stop=True)

