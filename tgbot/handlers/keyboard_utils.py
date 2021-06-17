from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from tgbot.handlers.manage_data import SECRET_LEVEL_BUTTON, CONFIRM_DECLINE_BROADCAST, CONFIRM_BROADCAST, \
    DECLINE_BROADCAST
from tgbot.handlers.text_ru import confirm_broadcast, decline_broadcast
from tgbot.handlers import text_ru, text_eng



def make_keyboard_for_delete_stock(language):
    buttons = [[
        InlineKeyboardButton(language.delete_stock_yes_text, callback_data='Yes'),
        InlineKeyboardButton(language.delete_stock_no_text, callback_data='No')
    ]]

    return InlineKeyboardMarkup(buttons)


def make_keyboard_for_portfolio_net(language):
    buttons = [[
        InlineKeyboardButton(language.net_profit_button, callback_data='Net'),
        InlineKeyboardButton(language.modify_button, callback_data='Modify')
    ], [
        InlineKeyboardButton(language.update_button, callback_data='Update')
    ]
    ]

    return InlineKeyboardMarkup(buttons)


def make_keyboard_for_portfolio_total(language):
    buttons = [[
        InlineKeyboardButton(language.total_profit_button, callback_data='Total'),
        InlineKeyboardButton(language.modify_button, callback_data='Modify')
    ], [
        InlineKeyboardButton(language.update_button, callback_data='Update')
    ]
    ]

    return InlineKeyboardMarkup(buttons)


def make_keyboard_for_portfolio_costs(language):
    buttons = [[
        InlineKeyboardButton(language.costs_button, callback_data='Costs'),
        InlineKeyboardButton(language.modify_button, callback_data='Modify')
    ], [
        InlineKeyboardButton(language.update_button, callback_data='Update')
    ]
    ]

    return InlineKeyboardMarkup(buttons)


def make_keyboard_for_portfolio_amount(language):
    buttons = [[
        InlineKeyboardButton(language.amount_button, callback_data='Amount'),
        InlineKeyboardButton(language.modify_button, callback_data='Modify')
    ], [
        InlineKeyboardButton(language.update_button, callback_data='Update')
    ]
    ]

    return InlineKeyboardMarkup(buttons)


def make_keyboard_for_portfolio_efficiency(language):
    buttons = [[
        InlineKeyboardButton(language.efficiency_button, callback_data='Efficiency'),
        InlineKeyboardButton(language.modify_button, callback_data='Modify')
    ], [
        InlineKeyboardButton(language.update_button, callback_data='Update')
    ]
    ]

    return InlineKeyboardMarkup(buttons)

def make_keyboard_for_modify_options(language):
    buttons = [
        [InlineKeyboardButton(language.add_stock_button, callback_data='Add Stock')],
        [InlineKeyboardButton(language.balance_button, callback_data='Change Balance')],
        [InlineKeyboardButton(language.delete_stock_button, callback_data='Delete Stock')],
        [InlineKeyboardButton(language.close_button, callback_data='Close')],
    ]

    return InlineKeyboardMarkup(buttons)


def make_keyboard_for_modify_to_invest_or_back(language):
    buttons = [
        # [InlineKeyboardButton(language.modify_to_invest_button, callback_data='Change To invest')],
        [InlineKeyboardButton(language.back_to_modify_button, callback_data='Back to Modify Options')],
    ]

    return InlineKeyboardMarkup(buttons)


def make_keyboard_for_add_stock_go_back(language):
    buttons = [
        [InlineKeyboardButton(language.back_to_modify_button, callback_data='Back to Modify Options')],
    ]

    return InlineKeyboardMarkup(buttons)


def keyboard_confirm_decline_broadcasting():
    buttons = [[
        InlineKeyboardButton(confirm_broadcast, callback_data=f'{CONFIRM_DECLINE_BROADCAST}{CONFIRM_BROADCAST}'),
        InlineKeyboardButton(decline_broadcast, callback_data=f'{CONFIRM_DECLINE_BROADCAST}{DECLINE_BROADCAST}')
    ]]

    return InlineKeyboardMarkup(buttons)


def make_keyboard_for_language_command(language):
    buttons = [[
        InlineKeyboardButton(language.language_EN, callback_data='en'),
        InlineKeyboardButton(language.language_RU, callback_data='ru')
    ]]

    return InlineKeyboardMarkup(buttons)