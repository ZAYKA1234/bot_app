from utils import find_relevant_solution,send_long_message
from state import bot_state
import os
import pandas as pd
from invisible import tok, tables


def start_handler(masseng):
    """Обработка команды /start"""
    p = f"Здравствуйте {masseng.from_user.first_name}! Вас приветствует помощник с решениями проблем по Информационным системам ЭПС и ЦРМ."
    tok.send_message(masseng.chat.id, p)


def domen_handler(masseng):
    """Обработка команды /domen"""
    bot_state.waiting_for_domen = True
    tok.send_message(masseng.chat.id, 'Введите ваш домен.')


def message_handler(masseng):
    """Обработка текстовых сообщений"""
    if bot_state.waiting_for_domen:
        handle_domen(masseng)
    else:
        user_input = masseng.text
        relevant_solution = find_relevant_solution(user_input)
        send_long_message(masseng.chat.id, relevant_solution)


def handle_domen(masseng):
    """Обработка домена"""
    text = masseng.text.lower()
    fil = tables[tables['Домен'] == text]

    if not fil.empty:
        pod = fil['Подразделения']
        fio = fil['ФИО кадровика']
        out = []
        for o in range(len(fil)):
            info = {
                'id': o + 1,
                'Подразделения': pod.iloc[o],
                'ФИО кадровика': fio.iloc[o]
            }
            out.append(info)

        df = pd.DataFrame(out)
        name = f'{text}.xlsx'
        df.to_excel(name, index=False)

        # Отправка документа
        with open(name, 'rb') as file:
            tok.send_document(masseng.chat.id, file)

        os.remove(name)  # Удаляем файл после отправки
        bot_state.waiting_for_domen = False
    else:
        tok.send_message(masseng.chat.id, "Ваш домен не найден или его нет в списке.")
        bot_state.waiting_for_domen = False
