from telegram.ext import CallbackContext
from telegram import Update
from keyboards import start_keyboard
from db import (
    is_user,
    add,
    get_user,
    update_db,
)


def start(update: Update, context: CallbackContext):
    user = update.effective_user
    bot = context.bot

    if is_user(str(user.id)):
        bot.send_message(user.id, 'Asslomu alaykum qaytgangiz bilan.', reply_markup=start_keyboard)
        db_user = get_user(str(user.id))
        bot.send_message(   
            user.id, 
            f'likes: {db_user["likes"]}\ndislikes: {db_user["dislikes"]}', 
            reply_markup=start_keyboard)
        return

    add(str(user.id))
    bot.sendMessage(user.id, 'Asslomu alaykum.', reply_markup=start_keyboard)

def like(update: Update, context: CallbackContext):
    user = update.effective_user
    bot = context.bot

    if is_user(str(user.id)):
        update_db(str(user.id), is_like=True)
        db_user = get_user(str(user.id))
        bot.send_message(   
            user.id, 
            f'likes: {db_user["likes"]}\ndislikes: {db_user["dislikes"]}', 
            reply_markup=start_keyboard)
        return

    add(str(user.id))
    bot.sendMessage(user.id, 'Asslomu alaykum.', reply_markup=start_keyboard)

def dislike(update: Update, context: CallbackContext):
    user = update.effective_user
    bot = context.bot

    if is_user(str(user.id)):
        update_db(str(user.id), is_dislike=True)
        db_user = get_user(str(user.id))
        bot.send_message(   
            user.id, 
            f'likes: {db_user["likes"]}\ndislikes: {db_user["dislikes"]}', 
            reply_markup=start_keyboard)
        return

    add(str(user.id))
    bot.sendMessage(user.id, 'Asslomu alaykum.', reply_markup=start_keyboard)

def cl(update: Update, context: CallbackContext):
    user = update.effective_user
    bot = context.bot

    if is_user(str(user.id)):
        update_db(str(user.id), clear=True)
        db_user = get_user(str(user.id))
        bot.send_message(   
            user.id, 
            f'likes: {db_user["likes"]}\ndislikes: {db_user["dislikes"]}', 
            reply_markup=start_keyboard)
        return

    add(str(user.id))
    bot.sendMessage(user.id, 'Asslomu alaykum.', reply_markup=start_keyboard)
