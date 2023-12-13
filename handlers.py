from telegram.ext import CallbackContext
from telegram import Update
from keyboards import start_keyboard

LIKES, DISLIKES = 0, 0

def start(update: Update, context: CallbackContext):
    user = update.message.from_user

    bot = context.bot

    bot.sendMessage(user.id, 'Asslomu alaykum.', reply_markup=start_keyboard)

def like(update: Update, context: CallbackContext):
    global LIKES

    LIKES += 1

    update.message.reply_html(
        text=f"""<b>Likes</b>: {LIKES}\n<b>Dislikes</b>: {DISLIKES}"""
    )

def dislike(update: Update, context: CallbackContext):
    global DISLIKES

    DISLIKES += 1

    update.message.reply_html(
        text=f"""<b>Likes</b>: {LIKES}\n<b>Dislikes</b>: {DISLIKES}"""
    )

def cl(update: Update, context: CallbackContext):
    global LIKES, DISLIKES

    LIKES, DISLIKES = 0, 0

    update.message.reply_html(
        text=f"""<b>Likes</b>: {LIKES}\n<b>Dislikes</b>: {DISLIKES}"""
    )
