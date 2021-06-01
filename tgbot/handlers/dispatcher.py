"""
    Telegram event handlers
"""

import telegram
from telegram.ext import (
    Updater, Dispatcher, Filters,
    CommandHandler, MessageHandler,
    InlineQueryHandler, CallbackQueryHandler,
    ChosenInlineResultHandler, ConversationHandler
)

# from celery.decorators import task  # event processing in async mode

from dtb.settings import TELEGRAM_TOKEN

from tgbot.handlers import admin, commands, files, location
from tgbot.handlers.commands import broadcast_command_with_message
from tgbot.handlers.handlers import secret_level, broadcast_decision_handler, currency_button, trade_experience_button, \
    help_button, modify_button, balance_button, add_stock_button, delete_stock_button, \
    close_button, modify_to_invest_button, inline_modify_stock_check, inline_modify_stock_shares, \
    inline_modify_to_invest, \
    inline_wrong_ticket, inline_modify_stock_total_costs, inline_add_stock_check, inline_wrong_ticket_add_stock, \
    mark_interested_button, delete_stock_exact_button, inline_delete_stock_check, inline_wrong_ticket_delete_stock, \
    portfolio_values_button, update_portfolio, close_conversation
from tgbot.handlers.manage_data import SECRET_LEVEL_BUTTON, CONFIRM_DECLINE_BROADCAST
from tgbot.handlers.static_text import broadcast_command
from tgbot.handlers.commands import CURRENCY, TRADE_EXPERIENCE, HELP, CLOSE_PORTFOLIO, END, INTERESTED_MARK
from tgbot.handlers.commands import MODIFY, MODIFY_OPTIONS, BALANCE, TO_INVEST, STOCK_SHARES, STOCK_TOTAL_COSTS, \
    ADD_STOCK, DELETE_STOCK, EXACT_DELETE_STOCK

def setup_dispatcher(dp):
    """
    Adding handlers for events from Telegram
    """

    # start comands and buttons
    dp.add_handler(CommandHandler("start", commands.command_start))
    # dp.add_handler(CallbackQueryHandler(currency_button))
    # dp.add_handler(CallbackQueryHandler(trade_experience_button))
    # dp.add_handler(CommandHandler("help", commands.command_help))

    portfolio_conv_handler = ConversationHandler(
        entry_points=[CommandHandler('portfolio', commands.command_portfolio)],
        states={
            MODIFY: [
                CallbackQueryHandler(modify_button, pattern='^' + 'Modify' + '$'),
                CallbackQueryHandler(portfolio_values_button, pattern='^' + '(Net|Total|Costs|Efficiency|Amount)' + '$'),
                CallbackQueryHandler(update_portfolio, pattern='^' + 'Update' + '$'),
            ],
            MODIFY_OPTIONS: [
                CallbackQueryHandler(balance_button, pattern='^' + 'Change Balance' + '$'),
                CallbackQueryHandler(add_stock_button, pattern='^' + 'Add Stock' + '$'),
                CallbackQueryHandler(delete_stock_button, pattern='^' + 'Delete Stock' + '$'),
                CallbackQueryHandler(close_button, pattern='^' + 'Close' + '$')
            ],
            BALANCE: [
                CallbackQueryHandler(modify_to_invest_button, pattern='^' + 'Change To invest' + '$'),
                CallbackQueryHandler(modify_button, pattern='^' + 'Back to Modify Options' + '$'),
                MessageHandler(Filters.regex('^(([a-zA-Z0-9]{3,6})|([a-zA-Z0-9]{3,6}((\.)|(\-))([a-zA-Z0-9]{1,4})))$'),
                               inline_modify_stock_check),
                MessageHandler((~ Filters.command), inline_wrong_ticket)
            ],
            TO_INVEST: [
                MessageHandler(Filters.regex('^(([0-9]{1,10}\.[0-9]{1,2})|([0-9]{1,10}))$'), inline_modify_to_invest)
            ],
            STOCK_SHARES: [
                MessageHandler(Filters.regex('^(([0-9]{1,10}\.[0-9]{1,10})|([0-9]{1,10}))$'), inline_modify_stock_shares)
            ],
            STOCK_TOTAL_COSTS: [
                MessageHandler(Filters.regex('^(([0-9]{1,10}\.[0-9]{1,2})|([0-9]{1,10}))$'),
                               inline_modify_stock_total_costs)
            ],
            ADD_STOCK: [
                CallbackQueryHandler(modify_button, pattern='^' + 'Back to Modify Options' + '$'),
                MessageHandler(Filters.regex('^(([a-zA-Z0-9]{3,6})|([a-zA-Z0-9]{3,6}((\.)|(\-))([a-zA-Z0-9]{1,4})))$'),
                               inline_add_stock_check),
                MessageHandler((~ Filters.command), inline_wrong_ticket)
            ],
            # INTERESTED_MARK: [
            #     CallbackQueryHandler(mark_interested_button, pattern='^' + '[1-5]' + '$'),
            # ],
            DELETE_STOCK: [
                CallbackQueryHandler(modify_button, pattern='^' + 'Back to Modify Options' + '$'),
                MessageHandler(Filters.regex('^^(([a-zA-Z0-9]{3,6})|([a-zA-Z0-9]{3,6}((\.)|(\-))([a-zA-Z0-9]{1,4})))$'),
                               inline_delete_stock_check),
                MessageHandler((~ Filters.command), inline_wrong_ticket)
            ],
            EXACT_DELETE_STOCK: [
                CallbackQueryHandler(delete_stock_exact_button, pattern='^(Yes|No)$'),
            ]
        },
        fallbacks=[
            MessageHandler(Filters.command, close_conversation)
        ],
        allow_reentry=True,
    )
    dp.add_handler(portfolio_conv_handler, 2)

    dp.add_handler(CallbackQueryHandler(mark_interested_button, pattern='^' + '[1-5]' + '$'))


    # start_conv_handler = ConversationHandler(
    #     entry_points=[CommandHandler('start', commands.command_start)],
    #     states={
    #         # CURRENCY: [CallbackQueryHandler(currency_button, pattern='^(dollar|euro)$')],
    #         # TRADE_EXPERIENCE: [CallbackQueryHandler(trade_experience_button, pattern='^(Yes|No)$')],
    #         HELP: [CallbackQueryHandler(help_button, pattern='^(Yes|No)$')],
    #     },
    #     fallbacks=[
    #         MessageHandler(Filters.command, close_conversation)
    #     ],
    #     allow_reentry=True,
    # )
    # dp.add_handler(start_conv_handler, 1)


    # admin commands
    dp.add_handler(CommandHandler("admin", admin.admin))
    dp.add_handler(CommandHandler("stats", admin.stats))

    dp.add_handler(MessageHandler(
        Filters.animation, files.show_file_id,
    ))

    # location
    # dp.add_handler(CommandHandler("ask_location", location.ask_for_location))
    # dp.add_handler(MessageHandler(Filters.location, location.location_handler))

    #buttons

    # dp.add_handler(CallbackQueryHandler(secret_level, pattern=f"^{SECRET_LEVEL_BUTTON}"))
    dp.add_handler(MessageHandler(Filters.regex(rf'^{broadcast_command} .*'), broadcast_command_with_message))
    dp.add_handler(CallbackQueryHandler(broadcast_decision_handler, pattern=f"^{CONFIRM_DECLINE_BROADCAST}"))

    #EXAMPLES FOR HANDLERS
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

    return dp


def run_pooling():
    """ Run bot in pooling mode """
    updater = Updater(TELEGRAM_TOKEN, use_context=True)

    dp = updater.dispatcher
    dp = setup_dispatcher(dp)

    bot_info = telegram.Bot(TELEGRAM_TOKEN).get_me()
    bot_link = f"https://t.me/" + bot_info["username"]

    print(f"Pooling of '{bot_link}' started")
    updater.start_polling()
    updater.idle()


# @task(ignore_result=True)
# def process_telegram_event(update_json):
#     update = telegram.Update.de_json(update_json, bot)
#     dispatcher.process_update(update)


# Global variable - best way I found to init Telegram bot
bot = telegram.Bot(TELEGRAM_TOKEN)
dispatcher = setup_dispatcher(Dispatcher(bot, None, workers=0, use_context=True))
TELEGRAM_BOT_USERNAME = bot.get_me()["username"]