class BotState:
    """Класс для управления состоянием бота"""
    def __init__(self):
        self.is_started = False

    def reset(self):
        """Сбрасываем состояния бота"""
        self.is_started = False

# Экземпляр для управления состоянием
bot_state = BotState()