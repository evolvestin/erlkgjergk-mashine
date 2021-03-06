# -*- coding: utf-8 -*-

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import telebot
from telebot import types
import urllib3
import re
import requests
import time
from time import sleep
import datetime
from datetime import datetime
import _thread
import random


# ======================================================================================================================
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
tkn = '617835554:AAHTqC39hgIGOSvaGEqrr8wDCGArB5EZwpA'
bot = telebot.TeleBot(tkn)

main = []
togoogle = []
count = 0
idMe = 396978030
idAdmin1 = 396978030
idAdmin2 = 396978030
idChatDevelopment = -1001389343364

NBOT = 'C' + 'h' + 'a' + 't' + 'W' + 'a' + 'r' + 's' + 'B' + 'o' + 't'
# ======================================================================================================================


def g_token(key, list):
    global sheet1
    global sheet2
    global sheet3
    global sheet4
    global sheet5
    if key == 1:
        creds1 = ServiceAccountCredentials.from_json_keyfile_name('person1.json', scope)
        client1 = gspread.authorize(creds1)
        sheet1 = client1.open('Time-mashine').worksheet(list)
    elif key == 2:
        creds2 = ServiceAccountCredentials.from_json_keyfile_name('person2.json', scope)
        client2 = gspread.authorize(creds2)
        sheet2 = client2.open('Time-mashine').worksheet(list)
    elif key == 3:
        creds3 = ServiceAccountCredentials.from_json_keyfile_name('person3.json', scope)
        client3 = gspread.authorize(creds3)
        sheet3 = client3.open('Time-mashine').worksheet(list)
    elif key == 4:
        creds4 = ServiceAccountCredentials.from_json_keyfile_name('person4.json', scope)
        client4 = gspread.authorize(creds4)
        sheet4 = client4.open('Time-mashine').worksheet(list)
    elif key == 5:
        creds5 = ServiceAccountCredentials.from_json_keyfile_name('person5.json', scope)
        client5 = gspread.authorize(creds5)
        sheet5 = client5.open('Time-mashine').worksheet(list)


g_token(1, 'main')
g_names = sheet1.col_values(1)
g_ids = sheet1.col_values(2)
t = []
for j1 in g_names:
    if g_names.index(j1) > 0:
        t.append(j1)
for j2 in t:
    try:
        g_token(1, j2)
        google = sheet1.col_values(1)
    except:
        g_token(5, j2)
        google = sheet5.col_values(1)
    main.append(google)
bot.send_message(idChatDevelopment, '🤤 Запуск')


def rawtime(stamp):
    rtime = []
    weekday = datetime.utcfromtimestamp(int(stamp + 3 * 60 * 60)).strftime('%a')
    if weekday == 'Mon':
        weekday = 'Пн'
    elif weekday == 'Tue':
        weekday = 'Вт'
    elif weekday == 'Wed':
        weekday = 'Ср'
    elif weekday == 'Thu':
        weekday = 'Чт'
    elif weekday == 'Fri':
        weekday = 'Пт'
    elif weekday == 'Sat':
        weekday = 'Сб'
    elif weekday == 'Sun':
        weekday = 'Вс'
    day = datetime.utcfromtimestamp(int(stamp + 3 * 60 * 60)).strftime('%d')
    month = datetime.utcfromtimestamp(int(stamp + 3 * 60 * 60)).strftime('%m')
    year = datetime.utcfromtimestamp(int(stamp + 3 * 60 * 60)).strftime('%Y')
    hours = datetime.utcfromtimestamp(int(stamp + 3 * 60 * 60)).strftime('%H')
    minutes = datetime.utcfromtimestamp(int(stamp)).strftime('%M')
    seconds = datetime.utcfromtimestamp(int(stamp)).strftime('%S')
    rtime.append(weekday)
    rtime.append(day)
    rtime.append(month)
    rtime.append(year)
    rtime.append(hours)
    rtime.append(minutes)
    rtime.append(seconds)
    return rtime


@bot.message_handler(commands=['time'])
def handle_time_command(message):
    time = rawtime(int(datetime.now().timestamp()))
    text = 'Время: ' + str(time[4]) + ':' + str(time[5]) + ':' + str(time[6]) + \
        ' <code>(' + str(time[0]) + ' ' + str(time[1] + '.' + str(time[2]) + '.' + \
        str(time[3])) + ', GMT+3)</code>'
    try:
        bot.send_message(message.chat.id, text, parse_mode='HTML')
    except:
        tempor = 0


@bot.message_handler(commands=['id'])
def handle_id_command(message):
    text = 'Твой ID: <code>' + str(message.from_user.id) + '</code>\n'
    if message.chat.id < 0:
        text = text + 'Group ID: <code>' + str(message.chat.id) + '</code>'
    try:
        bot.send_message(message.chat.id, text, parse_mode='HTML')
    except:
        tempor = 0


@bot.message_handler(commands=['start'])
def handle_start_command(message):
    global main
    if message.from_user.username:
        username = str(message.from_user.username)
        text = ''
        new_text = ''
        if str(message.from_user.id) not in g_ids:
            hi = '<i>Сонно смотрит на бумаги..</i> Тебя нет в моих списках, подожди немного.'
            try:
                bot.send_message(message.from_user.id, hi, parse_mode='HTML')
            except:
                tempor = 0
            row = ['@' + str(username), message.from_user.id]
            try:
                g_token(5, 'main')
                sheet5.insert_row(row, len(main) + 2)
                creds5 = ServiceAccountCredentials.from_json_keyfile_name('person1.json', scope)
                client5 = gspread.authorize(creds5)
                spreadsheet = client5.open('Time-mashine')
                spreadsheet.add_worksheet(title=row[0], rows='1', cols='2')
                main.append([])
                new_text = '. Ты теперь под наблюдением, закидывай все корованы, что у тебя есть (старые тоже).'
                text = ' [Добавлен в базу]'
            except:
                new_text = '. Что-то пошло не так, напиши @evolvestin'
                text = ' [Не смог добавить]'
        bot.send_message(idChatDevelopment, '@' + username + ' ID: ' + str(message.from_user.id) + text)
        try:
            bot.send_message(message.from_user.id, 'Привет 😛' + new_text)
        except:
            tempor = 0
    else:
        try:
            bot.send_message(message.from_user.id, 'Привет 😒. У тебя нет юзера, приходи позже.')
        except:
            tempor = 0


@bot.message_handler(content_types=["new_chat_members"])
def get_new_member(message):
    if message.chat.title:
        title = str(message.chat.title) + ' ('
    else:
        title = ' ('
    user_id = str(message.from_user.id)
    chat_id = str(message.chat.id)
    if message.from_user.username:
        chat_user = '@' + str(message.from_user.username) + ' / '
    else:
        if message.from_user.first_name:
            firstname = str(message.from_user.first_name)
        else:
            firstname = ''
        if message.from_user.last_name:
            lastname = str(message.from_user.last_name) + ' '
        else:
            lastname = ''
        chat_user = firstname + ' ' + lastname

    if message.new_chat_member:
        if message.new_chat_member.username == 'korovan_time_bot':
            bot.send_message(idChatDevelopment,
                             chat_user + user_id + ': Добавил бота в чат: ' + title + chat_id + ')')


@bot.message_handler(func=lambda message: message.text)
def repeat_all_messages(message):
    global check
    global togoogle
    if message.forward_date is not None and message.forward_from:
        if str(message.forward_from.username) == NBOT:
            search = re.search('.*Он пытается.*', message.text)
            if search:
                if str(message.from_user.id) in g_ids:
                    time = rawtime(message.forward_date)
                    row = str(time[1]) + '.' + str(time[2]) + '.' + str(time[3]) + ' ' + \
                        str(time[4]) + ':' + str(time[5]) + ':' + str(time[6]) + '#' + str(message.forward_date)
                    if main:
                        if row in main[g_ids.index(str(message.from_user.id)) - 1]:
                            text = '😒 Повторяемся значит? Я всё помню.'
                            if message.chat.id < 0:
                                try:
                                    bot.send_message(message.from_user.id, text, parse_mode='HTML')
                                except:
                                    try:
                                        bot.send_message(message.chat.id, text, parse_mode='HTML')
                                    except:
                                        tempor = 0
                            else:
                                try:
                                    bot.send_message(message.from_user.id, text,
                                                 reply_to_message_id=message.message_id, parse_mode='HTML')
                                except:
                                    try:
                                        bot.send_message(message.from_user.id, text, parse_mode='HTML')
                                    except:
                                        tempor = 0

                        else:
                            togoogle.append(str(g_names[g_ids.index(str(message.from_user.id))]) + '|' + str(row))
                            times = rawtime(int(message.forward_date) + 57600)
                            if (int(datetime.now().timestamp()) - message.forward_date) < (24 * 60 * 60):
                                text = '🤤 <b>Принято</b>\nПо моим подсчетам, следующий твой корован будет, ' \
                                       'примерно <i>' + str(times[1]) + '.' + str(times[2]) + '.' + str(times[3]) + \
                                       ' ' + str(times[4]) + ':' + str(times[5]) + ':' + str(times[6]) + '</i>'
                            else:
                                text = '🤤 <b>Принято</b>'
                            try:
                                bot.send_message(message.from_user.id, text, parse_mode='HTML')
                            except:
                                try:
                                    bot.send_message(message.chat.id, text, reply_to_message_id=message.message_id)
                                except:
                                    tempor = 0
                else:
                    try:
                        text = 'Тебя нет в моей базе, напиши кому-нибудь, чтобы тебя добавили 🤤'
                        bot.send_message(message.chat.id, text, reply_to_message_id=message.message_id)
                    except:
                        temp = 0
    elif message.reply_to_message and message.chat.id < 0:
        if message.text.lower() == 'пин' and message.from_user.id == idMe:
            try:
                bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
            except:
                bot.send_message(message.chat.id, 'Не получается пинить')


def updater():
    while True:
        try:
            global main
            global g_names
            global g_ids
            global count
            global togoogle
            sleep(count)
            count = 3
            temp_google = []
            if togoogle:
                temp_google = togoogle
                togoogle = []
            g_token(2, 'main')
            g_names = sheet2.col_values(1)
            g_ids = sheet2.col_values(2)
            temp_array = []
            for e in g_names:
                if g_names.index(e) > 0:
                    temp_array.append(e)
            if len(temp_array) != len(main):
                main = []
                for i in temp_array:
                    try:
                        g_token(2, i)
                        google = sheet2.col_values(1)
                    except:
                        g_token(5, i)
                        google = sheet5.col_values(1)
                    main.append(google)
                    count = count + 1
            if temp_google:
                for m in temp_google:
                    splited1 = m.split('|')
                    splited2 = splited1[1].split('#')
                    check = 1
                    if main[g_names.index(splited1[0]) - 1]:
                        last = main[g_names.index(splited1[0]) - 1][len(main[g_names.index(splited1[0]) - 1]) - 1].split('#')
                        if int(splited2[1]) < int(last[1]):
                            try:
                                g_token(3, splited1[0])
                                sheet3.insert_row([splited1[1]], len(main[g_names.index(splited1[0]) - 1]) + check)
                            except:
                                g_token(4, splited1[0])
                                sheet4.insert_row([splited1[1]], len(main[g_names.index(splited1[0]) - 1]) + check)
                            count = count + 1
                            main[g_names.index(splited1[0]) - 1].insert(len(main[g_names.index(splited1[0]) - 1]), splited1[1])
                        else:
                            for z in main[g_names.index(splited1[0]) - 1]:
                                splited3 = z.split('#')
                                if int(splited2[1]) > int(splited3[1]):
                                    try:
                                        g_token(3, splited1[0])
                                        sheet3.insert_row([splited1[1]], main[g_names.index(splited1[0]) - 1].index(z) + check)
                                    except:
                                        g_token(4, splited1[0])
                                        sheet4.insert_row([splited1[1]], main[g_names.index(splited1[0]) - 1].index(z) + check)
                                    check = check + 1
                                    count = count + 1
                                    main[g_names.index(
                                        splited1[0]) - 1].insert(main[g_names.index(splited1[0]) - 1].index(z), splited1[1])
                                    break
                    else:
                        try:
                            g_token(3, splited1[0])
                            sheet3.insert_row([splited1[1]], check)
                        except:
                            g_token(4, splited1[0])
                            sheet4.insert_row([splited1[1]], check)
                        count = count + 1
                        main[g_names.index(splited1[0]) - 1].insert(0, splited1[1])

        except Exception as e:
            sleep(0.9)


def telepol():
    try:
        bot.polling(none_stop=True, timeout=60)
    except:
        bot.stop_polling()
        sleep(0.5)
        telepol()


if __name__ == '__main__':
    _thread.start_new_thread(updater, ())
    telepol()
