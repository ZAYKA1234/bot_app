from invisible import tok
from handlers import start_handler, domen_handler, message_handler


if __name__ == '__main__':
    tok.message_handler(commands=['start'])(start_handler)

    tok.message_handler(commands=['domen'])(domen_handler)

    tok.message_handler(func=lambda message: True)(message_handler)

    tok.polling(none_stop=True)

