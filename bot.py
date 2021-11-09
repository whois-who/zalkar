import telebot
import random
import os, sys, codecs
import aiogram
from telebot import types
TOKEN = '2068799269:AAFscpbtZzvFehgzn6au83gv7iWRABGsrUo'
bot = telebot.TeleBot(TOKEN)

JoinedFile = open("users.txt", "r")
JoinedUsers = set()
for line in JoinedFile:
    JoinedUsers.add(line.strip())
JoinedFile.close()



@bot.message_handler(commands=['special'])
def mess(message):
    for user in JoinedUsers:
        bot.send_message(user, message.text[message.text.find(' '):])

@bot.message_handler(commands=['start'])
def welcome(message):
    if not str(message.chat.id) in JoinedUsers:
        JoinedFile = open("users.txt", "a")
        JoinedFile.write(str(message.chat.id) + "\n")
        JoinedUsers.add(message.chat.id)

        
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("О нас")
    item2 = types.KeyboardButton("Программы")
    item3 = types.KeyboardButton("Отзывы")
    item4 = types.KeyboardButton("Ответы на часто задаваемые вопросы")
    item5 = types.KeyboardButton("Контакты")



    markup.add(item1, item2, item3, item4,item5)

    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, Найду для вас всю информацию и полезные советы. Нажмите кнопку ниже 🤗".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)

# def startJoin(message):


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
    
        if message.text == 'О нас':
 
            markup = types.InlineKeyboardMarkup(row_width=1)
            item3 = types.InlineKeyboardButton("Миссия кооператива от руководителя, Камчыбек уулу Эрмат", callback_data='black')
            item4 = types.InlineKeyboardButton("Миссия кооператива от основательницы, Бекмурзаевой Акинай", callback_data='white')
            item5 = types.InlineKeyboardButton("Важная информация", callback_data='yellow')
            item6 = types.InlineKeyboardButton("Как всё происходит?", callback_data='pink')
 
            markup.add(item3, item4, item5, item6)
 
            bot.send_message(message.chat.id, 'Ниже вся информация', reply_markup=markup)
        
       
        elif message.text == 'Контакты':
 
            markup = types.InlineKeyboardMarkup(row_width=1)
            item89 = types.InlineKeyboardButton("Все контакты", callback_data='999')
 
            markup.add(item89)
 
            bot.send_message(message.chat.id, 'Ниже вся информация', reply_markup=markup)
        
        

        elif message.text == 'Отзывы':
            markup = types.InlineKeyboardMarkup(row_width=1)
            item7 = types.InlineKeyboardButton("Все отзывы", callback_data='one')
            item8 = types.InlineKeyboardButton("Оставить отзыв", callback_data='two')
 
            markup.add(item7, item8)
 
            bot.send_message(message.chat.id, 'Читайте ниже 👇', reply_markup=markup)
        



        elif message.text == 'Программы':
 
            markup = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton("50 + 4", callback_data='good')
            item2 = types.InlineKeyboardButton("35 + 4", callback_data='bad')
            item78 = types.InlineKeyboardButton("25 + 4", callback_data='fff')
            item87 = types.InlineKeyboardButton("Авто 50 + 7", callback_data='ddd')
            
 
            markup.add(item1, item2, item78, item87)

            bot.send_message(message.chat.id, 'Выберите программу', reply_markup=markup)
         
            


        elif message.text == 'Ответы на часто задаваемые вопросы':
 
            markup = types.InlineKeyboardMarkup(row_width=1)
            item10 = types.InlineKeyboardButton( u"Какая гарантия, что вы не закроетесь?", callback_data='qq')
            item11 = types.InlineKeyboardButton( u"Кому оформляется недвижимость?", callback_data='ww')
            item12 = types.InlineKeyboardButton( u"В случае отказа, могу ли я вернуть деньги назад?", callback_data='ee')
            item13 = types.InlineKeyboardButton( u"Если мы находимся в другой стране, можно ли производить оформления дистанционно?", callback_data='rr')
            item14 = types.InlineKeyboardButton( u"Если у меня нет денег для первоначального взноса?", callback_data='tt')
            item15 = types.InlineKeyboardButton( u"Можно ли досрочно закрыть долг?", callback_data='yy')
            item16 = types.InlineKeyboardButton( u"Помимо первоначального взноса, какие взносы необходимо вносить, чтобы получить недвижимость или авто?", callback_data='uu')
            item18 = types.InlineKeyboardButton( u"Могу ли я приобрести недвижимость в любом регионе страны?", callback_data='oo')
            item19 = types.InlineKeyboardButton( u"Почему не можем купить жилье в другой стране?", callback_data='pp')
            item20 = types.InlineKeyboardButton( u"Можно ли использовать средства для стройки дома?", callback_data='aa')
            item21 = types.InlineKeyboardButton( u"Есть ли бартер на авто или на что-то ещё?", callback_data='ss')

            markup.add(item10, item11, item12, item13, item14, item15, item16, item18, item19, item20, item21)
 
            bot.send_message(message.chat.id, 'Ответы на часто задаваемые вопросы 🤔', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'Я не .понимаю вас')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'one':
                bot.send_message(call.message.chat.id, 'https://www.youtube.com/channel/UCnfdcLSlbHlORf6fEx6RBAA')
            elif call.data == 'two':
                bot.send_message(call.message.chat.id, 'https://forms.gle/2UUjZ74GXcHy3mFC6')
        
        if call.message:
            if call.data == 'qq':
                bot.send_message(call.message.chat.id, u'Какая гарантия, что вы не закроетесь?')
                bot.send_message(call.message.chat.id, 'Кооператив не может закрыться, так как кооперативы создаются физическими и юридическими лицами на Добровольной основе для осуществления совместной хозяйственной и иной деятельности, предусмотренный уставом кооператива')
            if call.data == 'ww':
                bot.send_message(call.message.chat.id, u'Кому оформляется недвижимость?')
                bot.send_message(call.message.chat.id, 'Имущество оформляется на имя пайщика, при этом накладывается ограничение (ограничение / обременение) до полного погашения заемных средств.')
            if call.data == 'ee':
                bot.send_message(call.message.chat.id, u'Согласно уставу вы можете вернуть свои внесенные деньги назад')
                bot.send_message(call.message.chat.id, u'Согласно уставу вы можете вернуть свои внесенные деньги назад')
            if call.data == 'rr':
                bot.send_message(call.message.chat.id, u'Если мы находимся в другой стране, можно ли производить оформления дистанционно?')
                bot.send_message(call.message.chat.id, 'Если вы находитесь в другой стране, вы можете производить все оформления дистанционно.')
            if call.data == 'tt':
                bot.send_message(call.message.chat.id, u'Если у меня нет денег для первоначального взноса?')
                bot.send_message(call.message.chat.id, 'Если у вас нет первоначального взноса, то мы можем включить вас в накопительную программу')
            if call.data == 'yy':
                bot.send_message(call.message.chat.id, u'Можно ли досрочно закрыть долг?')
                bot.send_message(call.message.chat.id, 'В течении всего срока добавления вы можете досрочно закрыть долг перед кооперативом')
            if call.data == 'uu':
                bot.send_message(call.message.chat.id, u'Помимо первоначального взноса, какие взносы необходимо вносить, чтобы получить недвижимость или авто?')
                bot.send_message(call.message.chat.id, 'В момент покупки, помимо первоначального взноса вы платите 20 000 сом (недвижимость) или 10 000 сом (автомобиль) для юридического сопровождения')
            if call.data == 'oo':
                bot.send_message(call.message.chat.id, u'Могу ли я приобрести недвижимость в любом регионе страны?')
                bot.send_message(call.message.chat.id, 'Вы можете приобрести недвижимость на территории КР и РФ любом регионе страны')
            if call.data == 'pp':
                bot.send_message(call.message.chat.id, u'Почему не можем купить жилье в другой стране?')
                bot.send_message(call.message.chat.id, 'По уставу кооператива Ихсан групп ЛТД недвижимость можно обрести на территории РФ согласно по закону кооператива')
            if call.data == 'aa':
                bot.send_message(call.message.chat.id, u'Можно ли использовать средства для стройки дома?')
                bot.send_message(call.message.chat.id, 'Можно, вам нужно сначала выбрать поект дома, после этого вам нужно внести первоначальный взнос 35% или 50% от стоимости дома, единственное отличие вступительный взнос от стоимости жилья 8%. Преимущества |Дом будет под ключ с евро ремонтом на вам вкус |Закупки стоительных материалов и перевозка, работа с мастерами и их питание берет на себя ответсвенность кооператив на себя| Срок строительства от 4 до 8 месяцев.')
            if call.data == 'ss':
                bot.send_message(call.message.chat.id, u'Есть ли бартер на авто или на что-то ещё?')
                bot.send_message(call.message.chat.id, 'В качесве первоначального взноса можно делать бартер, квартиры в городе ош год постройки от 1965 года и выше, авто с 2005 года стоимость от 5000$ и выше. Отценщик компании производет осмотр после  этого только примется решение')

        if call.message:
            if call.data == 'black':
                bot.send_photo(call.message.chat.id, photo=open('img/Ermat.jpeg', 'rb'))
                bot.send_message(call.message.chat.id, 'Я, Камчыбек уулу Эрмат, являюсь руководителем. Считаю, что жизнь каждого человека зависит от страны, в которой он живет. Поэтому, каждый человек должен стараться сделать что-то полезное для своей страны. И тогда страна будет процветать! Меня беспокоят люди, которые не могут позволить себе недвижимость в родной стране. Сколько бы они не работали, их мечты о жилье могут не сбыться. Поэтому, кооператив Ихсан помогает приобрести жилье во благо народа. Моя цель служить своей стране и для наших кыргызстанцев.') 
            if call.data == 'white':
               bot.send_photo(call.message.chat.id, photo=open('img/Akinai.jpeg', 'rb'))
               bot.send_message(call.message.chat.id, u'Я, Бекмурзаева Акинай, являюсь основательницей НЖК Ихсан Групп ЛТД. Считаю что будущее начинается сегодня. Если мы хотим, чтобы оно было счастливым, то уже сейчас нужно делать что-то для этого. Мы готовы сделать вклад в светлое будущее для наших кыргызстанцев.')
            if call.data == 'yellow':
               bot.send_message(call.message.chat.id, 'Выгодные условия рассрочка до 10 лет с 0% на покупку жилья единоразовоя комиссия 4% минимальный первоначальный взнос 25% отсутствие членского взноса Гарантированная безопасность финансирование по программам фиксированный курс страхование вашего имущества (авто/недвижимость) юридическое сопровождение на 10 лет Полный спектр услуг минимальный пакет документов упрощенное приобретение имущества (авто/недвижимость) программы: 25%, 35%, 50% гибкий график приема граждан Уникальные возможности сотрудничество со строительной компанией Эмарк групп. Бартерная форма расчета после первоначального взноса, срок наступления очереди максимум 8 месяцев и минимум 1 месяц.')
            if call.data == 'pink':
               bot.send_message(call.message.chat.id, u'https://www.instagram.com/stories/highlights/17857848551571189/?hl=ru')

        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, '|Первоначальный взнос: 50% от стоимости недвижимости |Единоразовая комиссия: 4% от стоимости недвижимости |Сумма финансирования: от $10,000 до $65,000  |Срок наступления очереди: от 1 до 2 мес. |Срок рассрочки: до 10 лет')
            if call.data == 'bad':
                bot.send_message(call.message.chat.id, '|Первоначальный взнос: 35% от стоимости недвижимости |Единоразовая комиссия: 4% от стоимости недвижимости |Сумма финансирования: от $10,000 до $55,000 |Срок наступления очереди:  4 |Срок рассрочки: до 10 лет')
            if call.data == 'fff':
                bot.send_message(call.message.chat.id, '|25 + 4 |Первоначальный взнос: 25% от стоимости недвижимости |Единоразовая комиссия: 4% от стоимости недвижимости |Сумма финансирования: от $10,000 до $45,000 |Срок наступления очереди: 6|Срок рассрочки: до 10 лет')
            if call.data == 'ddd':
                bot.send_message(call.message.chat.id, '|ПРОГРАММА АВТОМАШИН |50 + 7|Первоначальный взнос: 50% от стоимости недвижимости |Единоразовая комиссия: 7% от стоимости недвижимости|Сумма финансирования: от $5,000 до $20,000| Срок наступления очереди: от 1 до 2 мес.|Срок рассрочки:  3 года')
            
        if call.message:
            if call.data == '999':
                bot.send_message(call.message.chat.id, '+996 222 005 150 | +996 990 005 150 | +996 700 005 150 | +996 500 005 150')
            
                
            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="",
                reply_markup=None)
 
            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                text="ready")


    except Exception as e:
        print(repr(e))
 
# RUN
bot.polling(none_stop=True)