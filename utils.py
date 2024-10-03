from answers import solutions
from questions import problems
from bot_app.invisible import tok

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
