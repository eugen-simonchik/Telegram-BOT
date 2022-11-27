import requests
from bs4 import BeautifulSoup
import re
import telebot
from telebot import types

bot = telebot.TeleBot('')


def infoclub(urlka):
    str_info = ''
    url_result = urlka
    page_result = requests.get(url_result)
    page_result.encoding = 'windows-1251'
    soup_result = BeautifulSoup(page_result.text, 'lxml')
    table_result = soup_result.find('div', class_="block")
    info_mc = []
    for i in table_result.find_all('p'):
        title2 = i.text
        info_mc.append(title2)
    tablica = [i for i in info_mc[0::1]]
    for i in range(len(tablica)):
        tablica[i] = re.sub('/n', ' ', tablica[i])
    str_info = '.'.join(tablica)
    return str_info


liverpoolfc = 'http://fapl.ru/teams/4/'
arsenalfc = 'http://fapl.ru/teams/1/'
astonvillafc = 'http://fapl.ru/teams/6/'
bormuntfc = 'http://fapl.ru/teams/41/'
braitonfc = 'http://fapl.ru/teams/43/'
bretfordfc = 'http://fapl.ru/teams/45/'
westhemfc = 'http://fapl.ru/teams/8/'
wulwerhemptonfc = 'http://fapl.ru/teams/30/'
cristalpalacefc = 'http://fapl.ru/teams/38/'
lesterfc = 'http://fapl.ru/teams/39/'
lidsfc = 'http://fapl.ru/teams/44/'
mancityfc = 'http://fapl.ru/teams/12/'
manunitedfc = 'http://fapl.ru/teams/11/'
nottingemfc = 'http://fapl.ru/teams/46/'
newcastlefc = 'http://fapl.ru/teams/14/'
saungemtonfc = 'http://fapl.ru/teams/36/'
tottenhemfc = 'http://fapl.ru/teams/9/'
fulhemfc = 'http://fapl.ru/teams/20/'
chelseafc = 'http://fapl.ru/teams/2/'
evertonfc = 'http://fapl.ru/teams/21/'

url = 'http://fapl.ru/fixtures/'
page = requests.get(url)
page.encoding = 'windows-1251'
soup = BeautifulSoup(page.text, 'lxml')
table1 = soup.find('table', class_="positions matches")
headers = []
for i in table1.find_all('tr'):
    title = i.text
    headers.append(title)
matchi = [i for i in headers[0::1]]
for i in range(len(matchi)):
    matchi[i] = re.sub('\n', ' ', matchi[i])
str_matchi = '\n'.join(matchi)

url1 = 'http://fapl.ru/table/'
page1 = requests.get(url1)
page1.encoding = 'windows-1251'
soup1 = BeautifulSoup(page1.text, 'lxml')
table2 = soup1.find('table', class_="positions")
headers1 = []
for i in table2.find_all('tr'):
    title1 = i.text
    headers1.append(title1)
tablica = [i for i in headers1[0:20:1]]
for i in range(len(tablica)):
    tablica[i] = re.sub('\n', ' ', tablica[i])
tablica_final = '\n'.join(map(str, tablica))

url2 = 'http://fapl.ru/topscorers/'
page2 = requests.get(url2)
page2.encoding = 'windows-1251'
soup2 = BeautifulSoup(page2.text, 'lxml')
table3 = soup2.find('table', class_='positions matches')
headers2 = []
for i in table3.find_all('td'):
    title2 = i.text
    headers2.append(title2)
bombo = [i for i in headers2[0:20:1]]
for i in range(len(bombo)):
    bombo[i] = re.sub('\n', ' ', bombo[i])
bombo_final = '\n'.join(map(str, bombo))

url_result = 'http://fapl.ru/results/'
page_result = requests.get(url_result)
page_result.encoding = 'windows-1251'
soup_result = BeautifulSoup(page_result.text, 'lxml')
table_result = soup_result.find('table', class_="positions matches")
resultats = []
for i in table_result.find_all('tr'):
    title = i.text
    resultats.append(title)
result_m = [i for i in resultats[0:15:1]]
for i in range(len(result_m)):
    result_m[i] = re.sub('\n', ' ', result_m[i])
result_matches = '\n'.join(result_m)


@bot.message_handler(commands=['start'])
def start(message):
    kb = types.InlineKeyboardMarkup()
    kb_matchi = types.InlineKeyboardButton(text='📆Матчи', callback_data='matchi')
    kb_tablica = types.InlineKeyboardButton(text='🏆Таблица', callback_data='tablica')
    kb_bombo = types.InlineKeyboardButton(text='⚽️Бомбардиры', callback_data='bombo')
    kb_result = types.InlineKeyboardButton(text='🔥Результаты', callback_data='resultaty')
    kb_clubs = types.InlineKeyboardButton(text='🏟Клубы', callback_data='clubs')
    kb_news = types.InlineKeyboardButton(text='🗞Новости', callback_data='news')
    kb.add(kb_matchi, kb_tablica, kb_bombo, kb_result, kb_news, kb_clubs)
    bot.send_message(message.chat.id,
                     'Здравствуй,ценитель футбола⚽️. Я-инфо бот об Английской премьер лиге!🔥 Выбери пункт,который тебе интересен!😏',
                     reply_markup=kb)


@bot.callback_query_handler(func=lambda call: True)
def call_back(call):
    if call.data == 'matchi':
        bot.send_message(call.message.chat.id, f'{str_matchi}')
    elif call.data == 'tablica':
        bot.send_message(call.message.chat.id, f'{tablica_final}')
    elif call.data == 'bombo':
        bot.send_message(call.message.chat.id, f'{bombo_final}')
    elif call.data == 'resultaty':
        bot.send_message(call.message.chat.id, f'{result_matches}')
    elif call.data == 'news':
        bot.send_message(call.message.chat.id, 'http://fapl.ru/news/')
    if call.data == 'clubs':
        kb_info_club = types.InlineKeyboardMarkup()
        kb_info_ars = types.InlineKeyboardButton(text='🏴󠁧󠁢󠁥󠁮󠁧󠁿Арсенал', callback_data='ars')
        kb_info_av = types.InlineKeyboardButton(text='🏴󠁧󠁢󠁥󠁮󠁧󠁿Астон Вилла', callback_data='av')
        kb_info_bor = types.InlineKeyboardButton(text='🏴󠁧󠁢󠁥󠁮󠁧󠁿Бормунт', callback_data='bor')
        kb_info_brai = types.InlineKeyboardButton(text='🏴󠁧󠁢󠁥󠁮󠁧󠁿Брайтон', callback_data='brai')
        kb_info_bret = types.InlineKeyboardButton(text='🏴󠁧󠁢󠁥󠁮󠁧󠁿Бретфорт', callback_data='bret')
        kb_info_west = types.InlineKeyboardButton(text='🏴󠁧󠁢󠁥󠁮󠁧󠁿ВестХем', callback_data='west')
        kb_info_wulf = types.InlineKeyboardButton(text='🏴󠁧󠁢󠁥󠁮󠁧󠁿Вульверхемтон', callback_data='wulf')
        kb_info_crist = types.InlineKeyboardButton(text='🏴󠁧󠁢󠁥󠁮󠁧󠁿Клисталл Пелас', callback_data='crist')
        kb_info_lest = types.InlineKeyboardButton(text='🏴󠁧󠁢󠁥󠁮󠁧󠁿Лестер', callback_data='lest')
        kb_info_liv = types.InlineKeyboardButton(text='🏴󠁧󠁢󠁥󠁮󠁧󠁿Ливерпуль', callback_data='liv')
        kb_info_lids = types.InlineKeyboardButton(text='🏴󠁧󠁢󠁥󠁮󠁧󠁿Лидс', callback_data='lids')
        kb_info_ms = types.InlineKeyboardButton(text='🏴󠁧󠁢󠁥󠁮󠁧󠁿Ман.Сити', callback_data='ms')
        kb_info_mu = types.InlineKeyboardButton(text='🏴󠁧󠁢󠁥󠁮󠁧󠁿Ман.Юнайтед', callback_data='mu')
        kb_info_not = types.InlineKeyboardButton(text='🏴󠁧󠁢󠁥󠁮󠁧󠁿Ноттингем', callback_data='not')
        kb_info_new = types.InlineKeyboardButton(text='🏴󠁧󠁢󠁥󠁮󠁧󠁿Ньюкасл', callback_data='new')
        kb_info_sau = types.InlineKeyboardButton(text='🏴󠁧󠁢󠁥󠁮󠁧󠁿Саунтгемнтон', callback_data='sau')
        kb_info_tot = types.InlineKeyboardButton(text='🏴󠁧󠁢󠁥󠁮󠁧󠁿Тоттенхем', callback_data='tot')
        kb_info_ful = types.InlineKeyboardButton(text='🏴󠁧󠁢󠁥󠁮󠁧󠁿Фулхэм', callback_data='ful')
        kb_info_chel = types.InlineKeyboardButton(text='🏴󠁧󠁢󠁥󠁮󠁧󠁿Челси', callback_data='chel')
        kb_info_ever = types.InlineKeyboardButton(text='🏴󠁧󠁢󠁥󠁮󠁧󠁿Эвертон', callback_data='ever')
        kb_info_club.add(kb_info_liv, kb_info_ars, kb_info_av, kb_info_bor, kb_info_brai, kb_info_bret, kb_info_west,
                         kb_info_wulf, kb_info_crist, kb_info_lest, kb_info_lids, kb_info_ms, kb_info_mu, kb_info_not,
                         kb_info_new, kb_info_sau, kb_info_tot, kb_info_ful, kb_info_ever, kb_info_chel)
        bot.send_message(call.message.chat.id, 'Выбери клуб,о котором хочешь узнать?', reply_markup=kb_info_club)
    elif call.data == 'liv':
        bot.send_message(call.message.chat.id, f'{infoclub(liverpoolfc)}')
    elif call.data == 'ars':
        bot.send_message(call.message.chat.id, f'{infoclub(arsenalfc)}')
    elif call.data == 'av':
        bot.send_message(call.message.chat.id, f'{infoclub(astonvillafc)}')
    elif call.data == 'bor':
        bot.send_message(call.message.chat.id, f'{infoclub(bormuntfc)}')
    elif call.data == 'brai':
        bot.send_message(call.message.chat.id, f'{infoclub(braitonfc)}')
    elif call.data == 'bret':
        bot.send_message(call.message.chat.id, f'{infoclub(bretfordfc)}')
    elif call.data == 'west':
        bot.send_message(call.message.chat.id, f'{infoclub(westhemfc)}')
    elif call.data == 'wulf':
        bot.send_message(call.message.chat.id, f'{infoclub(wulwerhemptonfc)}')
    elif call.data == 'crist':
        bot.send_message(call.message.chat.id, f'{infoclub(cristalpalacefc)}')
    elif call.data == 'lest':
        bot.send_message(call.message.chat.id, f'{infoclub(lesterfc)}')
    elif call.data == 'lids':
        bot.send_message(call.message.chat.id, f'{infoclub(lidsfc)}')
    elif call.data == 'ms':
        bot.send_message(call.message.chat.id, f'{infoclub(mancityfc)}')
    elif call.data == 'mu':
        bot.send_message(call.message.chat.id, f'{infoclub(manunitedfc)}')
    elif call.data == 'not':
        bot.send_message(call.message.chat.id, f'{infoclub(nottingemfc)}')
    elif call.data == 'new':
        bot.send_message(call.message.chat.id, f'{infoclub(newcastlefc)}')
    elif call.data == 'sau':
        bot.send_message(call.message.chat.id, f'{infoclub(saungemtonfc)}')
    elif call.data == 'tot':
        bot.send_message(call.message.chat.id, f'{infoclub(tottenhemfc)}')
    elif call.data == 'ful':
        bot.send_message(call.message.chat.id, f'{infoclub(fulhemfc)}')
    elif call.data == 'chel':
        bot.send_message(call.message.chat.id, f'{infoclub(chelseafc)}')
    elif call.data == 'ever':
        bot.send_message(call.message.chat.id, f'{infoclub(evertonfc)}')


bot.polling(none_stop=True)
