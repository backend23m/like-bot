from telegram import (
    ReplyKeyboardMarkup,
    KeyboardButton
)


start_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='👍'), KeyboardButton(text='👎')
        ],
        [
            KeyboardButton(text='🆑')
        ]
    ]
)
