import telebot
import random

token = 'TOKEN'

bot = telebot.TeleBot(token)


@bot.message_handler(content_types=['text'])
def echo(message):
    name = ''
    adjectives = ['большой', 'маленький', 'хороший', 'плохой', 'грустный', 'угрюмый', 'депрессивный', 'великолепный',
                  'потрясающий', 'слабый', 'молодой', 'старый', 'сильный', 'страшный', 'худой', 'отвратный', 'жирный',
                  'красивый', 'привлекательный', 'вонючий', 'какой-то', 'симпатичный', 'странный']
    adverbs = ['часто', 'сильно', 'много', 'довольно часто', 'достаточно комфортно', 'интенсивно', 'завораживающе',
               'душераздирающе', 'с энтузиазмом', 'с наслаждением', 'уверенно', 'профессионально', 'предсказуемо',
               'красиво', 'уродливо', 'нервно', 'спокойно', 'плохо', 'мирно', 'напряженно', 'расслабленно', 'методично']
    nouns = ['пёс', 'мужик', 'бык', 'лосось', 'квазимода', 'орел', 'спортсмен', 'автомобилист', 'придурок', 'дурачок',
             'алкаш', 'жених', 'доходяга', 'толстяк', 'кит', 'кошак', 'диван', 'самолет', 'автомобиль', 'слон', 'конь',
             'червяк', 'трансгендер', 'маньяк']
    verbs = ['ездит', 'ходит', 'летает', 'парит', 'существует', 'перемещается', 'пьет', 'бегает', 'курит', 'ржёт',
             'носится', 'стоит', 'скользит', 'корчится', 'умирает', 'гниет', 'спит', 'разлагается', 'устаревает',
             'молодеет', 'выздоравливает', 'испражняется', 'читает', 'смотрит телевизор', 'достает занозу',
             'наносит удары']
    adverbal_modifier = ['на земле', 'на дороге', 'на небе', 'в воде', 'на асфальте', 'на полу', 'в канализации',
                         'в ресторане', 'в кромешной темноте', 'в гнетущей тишине', 'со страшным шумом', 'дома',
                         'в небесах', 'в прихожей', 'в пивной', 'в лесу', ', вихляя задом', ', забившись под стол',
                         ', выглядывая из-под дивана', ', прильнув к унитазу', 'в библиотеке', 'на полянке', 'у реки',
                         'у озера', 'у моря', 'в больнице', 'на кладбище', 'в морге', 'на траве']

    random_replies = ['Ты, что ли? Как же я тебе не рад...', 'Че те надо?', 'Кто это тут до меня докопался?',
                      'Опять? Какие-то придурки все пишут и пишут... :-((',
                      'Опа, еще один долдон в чате... Че хотел-то?', 'Даже не знаю, что тебе на это ответить...',
                      'Да что ты все об одном и том же? Давай, меняем тему...',
                      'Нет, ну это ни в какие ворота не лезет... Яснее выражайте свои мысли, плиз...',
                      'Ну, ОК, поговорим... Предлагаю тему для разговора: сегодня на улице было не очень жарко, как думаете?']
    list = ['Дима', 'Олег', 'Кристина']
    exist = False
    for element in list:
        if element.lower() in message.text.lower():
            name = element
            random_replies_known = [f'Ба! Знакомые все лица! Это же {name}!', f'{name}, ты, что ли? Какими судьбами?',
                                    f'{name}, ты, что ли? Вот кого не ожидал услышать!',
                                    f'Хм..., это тот самый {name}, о котором я думаю?',
                                    f'{name}? Да не может быть! Сколько лет сколько зим?!',
                                    f'{name}? Блин, попал... Сто лет бы тебя не видеть...:-))']
            exist = True
            break
    if exist == True:
        text = random.choice(random_replies_known)
    elif 'как дела' in message.text.lower() and 'привет' in message.text.lower():
        text = 'Сам привет :-(, eще пока не родила, хе-хе :-)'
    elif 'как у тебя дела' in message.text.lower() and 'привет' in message.text.lower():
        text = 'Сам привет :-(, eще, ммать ттвою, не родила, хе-хе :-)'
    elif message.text.lower().startswith('привет'):
        text = 'Сам привет, мать твою... :-('
    elif 'как дела' in message.text.lower():
        text = 'Еще не родила, хе-хе :-)'
    elif 'как у тебя дела' in message.text.lower():
        text = 'Еще пока не родила, хе-хе :-)'
    elif 'скажи' in message.text.lower():
        text = random.choice(adjectives) + ' ' + random.choice(nouns) + ' ' + random.choice(
            adverbs) + ' ' + random.choice(verbs) + ' ' + random.choice(adverbal_modifier)
    elif 'скажешь' in message.text.lower():
        text = random.choice(adjectives) + ' ' + random.choice(nouns) + ' ' + random.choice(
            adverbs) + ' ' + random.choice(verbs) + ' ' + random.choice(adverbal_modifier)
    else:
        text = random.choice(random_replies)

    bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)
