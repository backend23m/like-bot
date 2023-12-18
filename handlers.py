from telegram.ext import CallbackContext
from telegram import Update
from keyboards import start_keyboard, start_inline_keyboard
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
        bot.send_message(
            user.id,
            f'inline likes: {db_user["inline_likes"]}\ninline dislikes: {db_user["inline_dislikes"]}', 
            reply_markup=start_inline_keyboard)
        return

    add(str(user.id))
    bot.sendMessage(user.id, 'Asslomu alaykum.', reply_markup=start_keyboard)
    bot.sendMessage(user.id, 'inline likes: 0\ninline dislikes: 0', reply_markup=start_inline_keyboard)

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

def inline_like(update: Update, context: CallbackContext):
    user = update.effective_user
    bot = context.bot
    print('inlike like')

    # if is_user(str(user.id)):
    #     update_db(str(user.id), is_like=True)
    #     db_user = get_user(str(user.id))
    #     bot.send_message(   
    #         user.id, 
    #         f'likes: {db_user["likes"]}\ndislikes: {db_user["dislikes"]}', 
    #         reply_markup=start_keyboard)
    #     return

    # add(str(user.id))
    # bot.sendMessage(user.id, 'Asslomu alaykum.', reply_markup=start_keyboard)

def inline_dislike(update: Update, context: CallbackContext):
    user = update.effective_user
    bot = context.bot
    print('inlike dislike')

    # if is_user(str(user.id)):
    #     update_db(str(user.id), is_dislike=True)
    #     db_user = get_user(str(user.id))
    #     bot.send_message(   
    #         user.id, 
    #         f'likes: {db_user["likes"]}\ndislikes: {db_user["dislikes"]}', 
    #         reply_markup=start_keyboard)
    #     return

    # add(str(user.id))
    # bot.sendMessage(user.id, 'Asslomu alaykum.', reply_markup=start_keyboard)

def inline_cl(update: Update, context: CallbackContext):
    user = update.effective_user
    bot = context.bot
    print('inlike clear')

    # if is_user(str(user.id)):
    #     update_db(str(user.id), clear=True)
    #     db_user = get_user(str(user.id))
    #     bot.send_message(   
    #         user.id, 
    #         f'likes: {db_user["likes"]}\ndislikes: {db_user["dislikes"]}', 
    #         reply_markup=start_keyboard)
    #     return

    # add(str(user.id))
    # bot.sendMessage(user.id, 'Asslomu alaykum.', reply_markup=start_keyboard)
