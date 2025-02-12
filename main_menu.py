from telegram import ReplyKeyboardMarkup

def main_menu_keyboard():
    """Creates the main menu keyboard."""
    keyboard = [
        ['/option1', '/option2'],  # 每行两个按钮
        ['/start'] # 返回主菜单
    ]
    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True,  # 使键盘更小
        one_time_keyboard=False  # 键盘是否在选择后消失
    )
