from telegram import (
    ReplyKeyboardMarkup, KeyboardButton,
    InlineKeyboardMarkup, InlineKeyboardButton
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

start_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='👍', callback_data='like'), InlineKeyboardButton(text='👎', callback_data='dislike')
        ],
        [
            InlineKeyboardButton(text='🆑', callback_data='clear')
        ]
    ]
)
