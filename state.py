class BotState:
    """Класс для управления состоянием бота"""

    def __init__(self):
        self.is_started = False
        self.waiting_for_domen = False

    def reset(self):
        """Сбрасываем состояния бота"""
        self.waiting_for_domen = False
        self.is_started = False


# Экземпляр для управления состоянием
bot_state = BotState()
