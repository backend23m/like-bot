from settings import TOKEN
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from handlers import (
    start,
    like, dislike, cl,
    inline_like, inline_dislike, inline_cl,
)


def main():
    # create updater obj.
    updater = Updater(TOKEN)
    
    # create dispatcher obj.
    dispatcher = updater.dispatcher
    
    # add command handlers
    dispatcher.add_handler(
        handler=CommandHandler(
            command=['start', 'boshlash'], 
            callback=start
        )
    )

    # add message handlers
    dispatcher.add_handler(
        handler=MessageHandler(
            filters=Filters.text("👍"),
            callback=like
        )
    )
    dispatcher.add_handler(
        handler=MessageHandler(
            filters=Filters.text("👎"),
            callback=dislike
        )
    )
    dispatcher.add_handler(
        handler=MessageHandler(
            filters=Filters.text("🆑"),
            callback=cl
        )
    )

    # add callback query handlers
    dispatcher.add_handler(
        handler=CallbackQueryHandler(
            callback=inline_dislike,
            pattern='dislike'
        )
    )
    dispatcher.add_handler(
        handler=CallbackQueryHandler(
            callback=inline_like,
            pattern='like'
        )
    )
    dispatcher.add_handler(
        handler=CallbackQueryHandler(
            callback=inline_cl,
            pattern='clear'
        )
    )

    # start polling
    updater.start_polling()
    updater.idle()

main()
