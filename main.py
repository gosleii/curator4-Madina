import telebot

bot = telebot.TeleBot('6897995110:AAH9Cq5NkkzdtIyQaC2R1qobXFJZnQM2D4U')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id,
                     'Привет! Я помогу тебе выбрать лучшего учителя информатики для подготовки к экзамену.\n Просто напиши к какому экзамену:*ЕГЭ* или *ОГЭ* ты готовишься. ',
                     parse_mode='Markdown')


@bot.message_handler(commands=['ОГЭ'])
def main(message):
    bot.send_message(message.chat.id,
                     'Прекрасно! Для уверенной сдачи экзамена я рекомендую тебе преподавателя информатики в  онлайн-школе Умскул *Артема Фролова*)\nВот ссылка ТГ-канала Артема-> [текст ссылки](https://t.me/twocod)',
                     parse_mode='Markdown')


@bot.message_handler(commands=['ЕГЭ'])
def main(message):
    bot.send_message(message.chat.id,
                     'Прекрасно! Для уверенной сдачи экзамена я рекомендую тебе преподавателя информатики в онлайн-школе Умскул *Вику Ланскую*)\nВот ссылка ТГ-канала Вики-> [текст ссылки](https://t.me/infa_vikusya',
                     parse_mode='Markdown')


@bot.message_handler(commands=['спасибо'])
def main(message):
    bot.send_message(message.chat.id, 'Всегда пожалуйста)', parse_mode='Markdown')


bot.infinity_polling()

