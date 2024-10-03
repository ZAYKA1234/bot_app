from invisible import tok
from questions import problems
from answers import solutions

MAX_MESSAGE_LENGTH = 4096
def send_long_message(chat_id, message):
    """Отправка длинных сообщений"""
    for i in range(0, len(message), MAX_MESSAGE_LENGTH):
        tok.send_message(chat_id, message[i:i + MAX_MESSAGE_LENGTH])

def find_relevant_solution(user_input):
    """Поиск релевантного решения"""
    for key, problem in problems.items():
        if problem.lower() in user_input.lower():
            return solutions.get(key, "Извините, я не смог найти решение для вашей проблемы.")
    return "Извините, я не смог найти решение для вашей проблемы."

@tok.message_handler(commands=['start'])
def start_handler(masseng):
    """Обработка команды /start"""
    p = f"Здравствуйте {masseng.from_user.first_name}! Вас приветствует помощник с решениями проблем по Информационным системам ЭПС и ЦРМ."
    tok.send_message(masseng.chat.id, p)

@tok.message_handler(func=lambda message: True)
def message_handler(masseng):
    """Обработка текстовых сообщений"""
    user_input = masseng.text
    relevant_solution = find_relevant_solution(user_input)
    send_long_message(masseng.chat.id, relevant_solution)

tok.polling(none_stop=True)