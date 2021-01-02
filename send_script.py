import telebot
import schedule
from settings import bot_token
import time
from faunahelper import FaunaHelper
from faunadb.client import FaunaClient
from settings import fauna_key



def job(bot, faunahelper):
    students = faunahelper.get_all_sudents()
    for student in students:
        try:
            bot.send_message(student[0], 'Добрый день. Напоминаю, что до конца курса у Вас осталось %s дней. ' % str(student[1]))
        except telebot.apihelper.ApiException:
            bot.send_message(397472277,
                             'Это сообщение не про меня')
            bot.send_message(397472277, 'До конца курса у %s осталось %s дней' % (str(student[0]), str(student[1])))
        faunahelper.decrement_days_by_telegram_id(student[0])


bot = telebot.TeleBot(bot_token)
faunahelper = FaunaHelper(FaunaClient(fauna_key))

schedule.every(10).seconds.do(job, bot, faunahelper)


while True:
    schedule.run_pending()
    time.sleep(1)