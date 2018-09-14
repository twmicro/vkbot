import vk_api
import time
import sys, traceback
import datetime
vk = vk_api.VkApi(token='c87370d527dea2ce349039c44a68f1901996ebdef8ae617c275c9c01e9adb64b0ccffd46f60cf5f6f4e49')
vk._auth_token()

values = {'out':0, 'count':100, 'time_offset':60, 'group_id':160615635}
def write_msg(user_id, s):
    vk.method('messages.send', {'user_id':user_id, 'message':s})

def now_wd():
        return datetime.datetime.now().weekday() + 1
def wd_string():
    days = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
    return days[now_wd() - 1]
def now_mth():
    months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
    return months[datetime.datetime.now().month - 1]
while True:
    try:
        response = vk.method('messages.getConversations', values)
        #if response['items']:
        #values['last_message_id'] = response['items'][0]['id']
        for item in response['items']:

            if item['last_message']['text']=="Привет!":
                answer = 'И вам привет!'
            elif item['last_message']['text'] == "Время":
                time = datetime.datetime.time(datetime.datetime.now())
                answer = str(time.hour) + ':' + str(time.minute)
            elif item['last_message']['text'] == "День":
                answer = 'Cегодня ' + wd_string()
            elif item['last_message']['text'] == "День по счету":
                answer = 'Cегодня ' + str(now_wd()) + ' день недели'
            elif item['last_message']['text'] == "Месяц":
                answer = now_mth()
            elif item['last_message']['text'] == "Пока":
                answer = 'Пока'
            elif item['last_message']['text'] == "Как дела?":
                answer = 'Хорошо'

            else:
                answer = 'Не понял :)'
            write_msg(item['last_message']['from_id'], answer)
            #print(item['last_message']['from_id'])
            print(datetime.datetime.now(),'from id {} sent message = {} we answered = {}'.
            format(item['last_message']['from_id'],item['last_message']['text'],answer))
        time.sleep(0.5)
    except:
        pass