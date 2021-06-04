from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from tgbot.handlers.manage_data import SECRET_LEVEL_BUTTON, CONFIRM_DECLINE_BROADCAST, CONFIRM_BROADCAST, \
    DECLINE_BROADCAST
from tgbot.handlers.static_text import confirm_broadcast, \
    decline_broadcast, modify_button, balance_button, add_stock_button, delete_stock_button, close_button,\
    modify_to_invest_button, back_to_modify_button, delete_stock_yes_text, delete_stock_no_text, net_profit_button,\
    total_profit_button, costs_button, efficiency_button, amount_button, update_button


def make_keyboard_for_delete_stock():
    buttons = [[
        InlineKeyboardButton(delete_stock_yes_text, callback_data='Yes'),
        InlineKeyboardButton(delete_stock_no_text, callback_data='No')
    ]]

    return InlineKeyboardMarkup(buttons)


def make_keyboard_for_portfolio_net():
    buttons = [[
        InlineKeyboardButton(net_profit_button, callback_data='Net'),
        InlineKeyboardButton(modify_button, callback_data='Modify')
    ], [
        InlineKeyboardButton(update_button, callback_data='Update')
    ]
    ]

    return InlineKeyboardMarkup(buttons)


def make_keyboard_for_portfolio_total():
    buttons = [[
        InlineKeyboardButton(total_profit_button, callback_data='Total'),
        InlineKeyboardButton(modify_button, callback_data='Modify')
    ], [
        InlineKeyboardButton(update_button, callback_data='Update')
    ]
    ]

    return InlineKeyboardMarkup(buttons)


def make_keyboard_for_portfolio_costs():
    buttons = [[
        InlineKeyboardButton(costs_button, callback_data='Costs'),
        InlineKeyboardButton(modify_button, callback_data='Modify')
    ], [
        InlineKeyboardButton(update_button, callback_data='Update')
    ]
    ]

    return InlineKeyboardMarkup(buttons)


def make_keyboard_for_portfolio_amount():
    buttons = [[
        InlineKeyboardButton(amount_button, callback_data='Amount'),
        InlineKeyboardButton(modify_button, callback_data='Modify')
    ], [
        InlineKeyboardButton(update_button, callback_data='Update')
    ]
    ]

    return InlineKeyboardMarkup(buttons)


def make_keyboard_for_portfolio_efficiency():
    buttons = [[
        InlineKeyboardButton(efficiency_button, callback_data='Efficiency'),
        InlineKeyboardButton(modify_button, callback_data='Modify')
    ], [
        InlineKeyboardButton(update_button, callback_data='Update')
    ]
    ]

    return InlineKeyboardMarkup(buttons)

def make_keyboard_for_modify_options():
    buttons = [
        [InlineKeyboardButton(balance_button, callback_data='Change Balance')],
        [InlineKeyboardButton(add_stock_button, callback_data='Add Stock')],
        [InlineKeyboardButton(delete_stock_button, callback_data='Delete Stock')],
        [InlineKeyboardButton(close_button, callback_data='Close')],
    ]

    return InlineKeyboardMarkup(buttons)


def make_keyboard_for_modify_to_invest_or_back():
    buttons = [
        [InlineKeyboardButton(modify_to_invest_button, callback_data='Change To invest')],
        [InlineKeyboardButton(back_to_modify_button, callback_data='Back to Modify Options')],
    ]

    return InlineKeyboardMarkup(buttons)


def make_keyboard_for_add_stock_go_back():
    buttons = [
        [InlineKeyboardButton(back_to_modify_button, callback_data='Back to Modify Options')],
    ]

    return InlineKeyboardMarkup(buttons)


def keyboard_confirm_decline_broadcasting():
    buttons = [[
        InlineKeyboardButton(confirm_broadcast, callback_data=f'{CONFIRM_DECLINE_BROADCAST}{CONFIRM_BROADCAST}'),
        InlineKeyboardButton(decline_broadcast, callback_data=f'{CONFIRM_DECLINE_BROADCAST}{DECLINE_BROADCAST}')
    ]]

    return InlineKeyboardMarkup(buttons)