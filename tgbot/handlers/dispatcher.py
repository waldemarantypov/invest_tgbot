"""
    Telegram event handlers
"""

import telegram
from telegram.ext import (
    Updater, Dispatcher, Filters, PicklePersistence,
    CommandHandler, MessageHandler,
    CallbackQueryHandler,
    ConversationHandler, Defaults
)

from dtb.settings import TELEGRAM_TOKEN
from tgbot.handlers import admin, commands, files
from tgbot.handlers.commands import MODIFY, MODIFY_OPTIONS, BALANCE, TO_INVEST, STOCK_SHARES, STOCK_TOTAL_COSTS, \
    ADD_STOCK, EDIT_STOCK, DELETE_STOCK, EXACT_DELETE_STOCK
from tgbot.handlers.commands import broadcast_command_with_message
from tgbot.handlers.handlers import broadcast_decision_handler, modify_button, \
    close_button, inline_modify_stock_check, inline_modify_stock_shares, \
    inline_modify_stock_total_costs, inline_add_stock_check, delete_stock_exact_button, \
    inline_delete_stock_check, portfolio_values_button, update_portfolio, close_conversation, \
    inline_wrong_ticket_delete, balance_button_edit, inline_wrong_ticket_add, inline_wrong_ticket_edit, \
    inline_wrong_stock_shares, inline_wrong_stock_costs, balance_button_add, balance_button_delete, \
    back_to_modify_button, language_changer, wrong_command_entered
from tgbot.handlers.manage_data import CONFIRM_DECLINE_BROADCAST
from tgbot.handlers.text_ru import broadcast_command


# from celery.decorators import task  # event processing in async mode

# not_commands_pattern = '^' + '(?!(\/portfolio|\/share|\/feedback|\/stats|\/admin|\/language)).*' + '$'
not_commands_pattern = '^' + '(\/start|\/portfolio|\/share|\/feedback|\/stats|\/admin|\/language)' + '$'

def setup_dispatcher(dp):
    """
    Adding handlers for events from Telegram
    """
    dp.add_handler(CommandHandler("start", commands.command_start))
    dp.add_handler(CommandHandler("feedback", commands.command_feedback))
    dp.add_handler(CommandHandler("share", commands.command_share_bot))
    dp.add_handler(CommandHandler("language", commands.command_language))
    dp.add_handler(CallbackQueryHandler(language_changer,
                                        pattern='^' + '(en|ru)' + '$'))

    portfolio_conv_handler = ConversationHandler(
        entry_points=[CommandHandler('portfolio', commands.command_portfolio)],
        states={
            MODIFY: [
                CallbackQueryHandler(modify_button, pattern='^' + 'Modify' + '$'),
                CallbackQueryHandler(portfolio_values_button,
                                     pattern='^' + '(Net|Total|Costs|Efficiency|Amount)' + '$'),
                CallbackQueryHandler(update_portfolio, pattern='^' + 'Update' + '$'),
            ],
            MODIFY_OPTIONS: [
                CallbackQueryHandler(balance_button_edit, pattern='^' + 'Change Balance' + '$'),
                CallbackQueryHandler(balance_button_add, pattern='^' + 'Add Stock' + '$'),
                CallbackQueryHandler(balance_button_delete, pattern='^' + 'Delete Stock' + '$'),
                CallbackQueryHandler(close_button, pattern='^' + 'Close' + '$')
            ],
            BALANCE: [
                # CallbackQueryHandler(modify_to_invest_button, pattern='^' + 'Change To invest' + '$'),
                CallbackQueryHandler(back_to_modify_button, pattern='^' + 'Back to Modify Options' + '$'),
                MessageHandler(Filters.regex('^(([a-zA-Z0-9]{2,16})|([a-zA-Z0-9]{2,16}((\.)|(\-))([a-zA-Z0-9]{1,4})))$'),
                               inline_modify_stock_check),
                MessageHandler((~ Filters.command), inline_wrong_ticket_edit),
                MessageHandler((~ Filters.regex(not_commands_pattern)), inline_wrong_ticket_edit)
            ],
            # TO_INVEST: [
            #     MessageHandler(Filters.regex('^(([0-9]{1,10}\.[0-9]{1,2})|([0-9]{1,10}))$'), inline_modify_to_invest)
            # ],
            STOCK_SHARES: [
                MessageHandler(Filters.regex('^(([0-9]{1,10}\.[0-9]{1,10})|([0-9]{1,10}))$'),
                               inline_modify_stock_shares),
                MessageHandler((~ Filters.command), inline_wrong_stock_shares)
            ],
            STOCK_TOTAL_COSTS: [
                MessageHandler(Filters.regex('^(([0-9]{1,10}\.[0-9]{1,2})|([0-9]{1,10}))$'),
                               inline_modify_stock_total_costs),
                MessageHandler((~ Filters.command), inline_wrong_stock_costs)
            ],
            ADD_STOCK: [
                CallbackQueryHandler(back_to_modify_button, pattern='^' + 'Back to Modify Options' + '$'),
                MessageHandler(Filters.regex('^(([a-zA-Z0-9]{2,16})|([a-zA-Z0-9]{2,16}((\.)|(\-))([a-zA-Z0-9]{1,4})))$'),
                               inline_add_stock_check),
                MessageHandler((~ Filters.command), inline_wrong_ticket_add),
                MessageHandler((~ Filters.regex(not_commands_pattern)), inline_wrong_ticket_add)
            ],
            DELETE_STOCK: [
                CallbackQueryHandler(back_to_modify_button, pattern='^' + 'Back to Modify Options' + '$'),
                MessageHandler(Filters.regex('^(([a-zA-Z0-9]{2,16})|([a-zA-Z0-9]{2,16}((\.)|(\-))([a-zA-Z0-9]{1,4})))$'),
                               inline_delete_stock_check),
                MessageHandler((~ Filters.command), inline_wrong_ticket_delete),
                MessageHandler((~ Filters.regex(not_commands_pattern)), inline_wrong_ticket_delete)
            ],
            EXACT_DELETE_STOCK: [
                CallbackQueryHandler(delete_stock_exact_button, pattern='^(Yes|No)$'),
            ]
        },
        fallbacks=[
            MessageHandler(Filters.command, close_conversation)
        ],
        allow_reentry=True,
        persistent=True,
        name='portfolio_conversation_persistance',
    )
    dp.add_handler(portfolio_conv_handler, 1)

    # admin commands
    dp.add_handler(CommandHandler("admin", admin.admin))
    dp.add_handler(CommandHandler("stats", admin.stats))

    # dp.add_handler(MessageHandler(
    #     Filters.animation, files.show_file_id,
    # ))

    # location
    # dp.add_handler(CommandHandler("ask_location", location.ask_for_location))
    # dp.add_handler(MessageHandler(Filters.location, location.location_handler))

    # buttons

    # dp.add_handler(CallbackQueryHandler(secret_level, pattern=f"^{SECRET_LEVEL_BUTTON}"))
    dp.add_handler(MessageHandler(Filters.regex(rf'^{broadcast_command} .*'), broadcast_command_with_message))
    dp.add_handler(CallbackQueryHandler(broadcast_decision_handler, pattern=f"^{CONFIRM_DECLINE_BROADCAST}"))

    # EXAMPLES FOR HANDLERS
    # dp.add_handler(MessageHandler(Filters.text, <function_handler>))
    # dp.add_handler(MessageHandler(
    #     Filters.document, <function_handler>,
    # ))
    # dp.add_handler(CallbackQueryHandler(<function_handler>, pattern="^r\d+_\d+"))
    # dp.add_handler(MessageHandler(
    #     Filters.chat(chat_id=int(TELEGRAM_FILESTORAGE_ID)),
    #     # & Filters.forwarded & (Filters.photo | Filters.video | Filters.animation),
    #     <function_handler>,
    # ))

    #dp.add_handler(MessageHandler((Filters.regex(not_commands_pattern) & (Filters.text)), wrong_command_entered), 1)
    dp.add_handler(MessageHandler((~ Filters.regex(not_commands_pattern)), wrong_command_entered), 1)

    return dp


def run_pooling():
    defaults = Defaults(parse_mode=telegram.ParseMode.HTML)

    """ Run bot in pooling mode """
    updater = Updater(TELEGRAM_TOKEN, persistence=my_persistence, defaults=defaults, use_context=True)

    dp = updater.dispatcher
    dp = setup_dispatcher(dp)

    bot_info = telegram.Bot(TELEGRAM_TOKEN).get_me()
    bot_link = f"https://t.me/" + bot_info["username"]

    print(f"Pooling of '{bot_link}' started")
    updater.start_polling()
    updater.idle()


# @task(ignore_result=True)
def process_telegram_event(update_json):
    update = telegram.Update.de_json(update_json, bot)
    dispatcher.process_update(update)


# Global variable - best way I found to init Telegram bot
bot = telegram.Bot(TELEGRAM_TOKEN)
my_persistence = PicklePersistence(filename='my_persistence_file')
dispatcher = setup_dispatcher(Dispatcher(bot, None, workers=0, persistence=my_persistence, use_context=True))
TELEGRAM_BOT_USERNAME = bot.get_me()["username"]
