from invisible import tok


@tok.message_handler(commands=['start'])
def start_handler(masseng):
    """Обработка команды /start"""
    p = f"Здравствуйте {masseng.from_user.first_name}! Вас приветствует помощник с решениями проблем по Информационным системам ЭПС и ЦРМ."
    tok.send_message(masseng.chat.id, p)

tok.polling(none_stop=True)
