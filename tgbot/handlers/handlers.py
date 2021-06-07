import datetime
import time
import json

import telegram
import yfinance as yf
from django.utils import timezone
from telegram.ext import (
    ConversationHandler
)

from tgbot.handlers.commands import MODIFY, MODIFY_OPTIONS, TO_INVEST, BALANCE, STOCK_SHARES, STOCK_TOTAL_COSTS, \
    ADD_STOCK, DELETE_STOCK, EXACT_DELETE_STOCK
from tgbot.handlers.commands import TRADE_EXPERIENCE, HELP, END
from tgbot.handlers.keyboard_utils import make_keyboard_for_modify_options, make_keyboard_for_modify_to_invest_or_back,\
    make_keyboard_for_add_stock_go_back, make_keyboard_for_delete_stock, make_keyboard_for_portfolio_total,\
    make_keyboard_for_portfolio_net, make_keyboard_for_portfolio_costs, make_keyboard_for_portfolio_amount,\
    make_keyboard_for_portfolio_efficiency
from tgbot.handlers.manage_data import CONFIRM_DECLINE_BROADCAST, CONFIRM_BROADCAST
from tgbot.handlers.static_text import unlock_secret_room, message_is_sent, modify_question, change_balance_text, \
    change_to_invest_text, changed_to_invest_text, modify_wrong_ticket, \
    modify_balance_stock_not_in_portfolio, modify_balance_stock_symbol_shares, modify_balance_stock_shares_success, \
    change_balance_text_stock_write, close_modify_menu_portfolio, modify_balance_stock_total_costs_success, \
    add_stock_text, add_stock_symbol_check_already_have, add_stock_symbol_check_success, add_stock_not_in_yfinance, \
    delete_stock_text, delete_stock_write, delete_stock_info, delete_stock_success, delete_stock_cancel, \
    add_wrong_ticket, delete_wrong_ticket, add_stock_write, wait_update, modify_wrong_stock_parameters
from tgbot.handlers.utils import handler_logging, send_typing_action
from tgbot.models import User, Portfolio, Stock
from tgbot.portfolio_utils import portfolio_output_net, portfolio_output_total, \
    portfolio_output_amount, portfolio_output_costs, portfolio_output_efficiency, portfolio_update
# from tgbot.tasks import broadcast_message
from tgbot.utils import extract_user_data_from_update


@send_typing_action
@handler_logging()
def secret_level(update, context): #callback_data: SECRET_LEVEL_BUTTON variable from manage_data.py
    """ Pressed 'secret_level_button_text' after /start command"""
    user_id = extract_user_data_from_update(update)['user_id']
    text = unlock_secret_room.format(
        user_count=User.objects.count(),
        active_24=User.objects.filter(updated_at__gte=timezone.now() - datetime.timedelta(hours=24)).count()
    )

    context.bot.edit_message_text(
        text=text,
        chat_id=user_id,
        message_id=update.callback_query.message.message_id,
        parse_mode=telegram.ParseMode.MARKDOWN
    )


'''
Portfolio command functions
'''

"""
Portfolio
First menu - buttons:
1) modify
2) portfolio values button
"""


@send_typing_action
@handler_logging()
def portfolio_values_button(update, context):
    query = update.callback_query

    query.answer()

    u = User.get_user(update, context)
    p = Portfolio.get_or_create_by_user(u)
    s = Stock.filter_by_portfolio(p)

    if query.data == 'Net':
        text = portfolio_output_net(p, s)
        reply_markup = make_keyboard_for_portfolio_total()
    elif query.data == 'Total':
        text = portfolio_output_total(p, s)
        reply_markup = make_keyboard_for_portfolio_costs()
    elif query.data == 'Costs':
        text = portfolio_output_costs(p, s)
        reply_markup = make_keyboard_for_portfolio_amount()
    elif query.data == 'Amount':
        text = portfolio_output_amount(p, s)
        reply_markup = make_keyboard_for_portfolio_efficiency()
    elif query.data == 'Efficiency':
        text = portfolio_output_efficiency(p, s)
        reply_markup = make_keyboard_for_portfolio_net()

    query.edit_message_text(text=text, reply_markup=reply_markup, parse_mode=telegram.ParseMode.HTML)

    return MODIFY


@send_typing_action
@handler_logging()
def update_portfolio(update, context):
    query = update.callback_query

    query.answer()

    query.edit_message_text(text=wait_update)

    u = User.get_user(update, context)
    p = Portfolio.get_or_create_by_user(u)
    s = Stock.filter_by_portfolio(p)

    portfolio_update(p, s)
    text = portfolio_output_efficiency(p, s)
    query.edit_message_text(text=text, reply_markup=make_keyboard_for_portfolio_net(), parse_mode=telegram.ParseMode.HTML)

    return MODIFY


@handler_logging()
def modify_button(update, context):
    try:
        query = update.callback_query
        query.answer()
        query.edit_message_reply_markup()
    except:
        ...

    context.bot.sendMessage(chat_id=update.effective_chat.id, text=modify_question,
                            reply_markup=make_keyboard_for_modify_options())
    return MODIFY_OPTIONS


@handler_logging()
def back_to_modify_button(update, context):
    try:
        query = update.callback_query
        query.answer()
        query.delete_message()
    except:
        ...
    return modify_button(update, context)

"""
END
Portfolio
First menu
"""

'''
Portfolio
Second menu - buttons:
1) balance
2) add stock
3) delete stock
4) close
'''

'''
Portfolio
Second menu
Button: Balance
Options - 2 buttons(modify to invest, go back to modify button(in dispatcher)) and 2 inlines(modify_stock_check,
 wrong inline)
'''


@send_typing_action
@handler_logging()
def balance_button_edit(update, context):
    try:
        query = update.callback_query
        query.answer()
        query.delete_message()
    except:
        ...

    # context.bot.sendMessage(chat_id=update.effective_chat.id, text=change_balance_text,
    #                         reply_markup=make_keyboard_for_modify_to_invest_or_back())

    file = r"tgbot/static/gif/edit_stock.mp4"
    file = open(file, 'rb')

    caption = change_balance_text

    context.bot.sendAnimation(chat_id=update.effective_chat.id, animation=file, caption=caption,
                              reply_markup=make_keyboard_for_modify_to_invest_or_back())

    return BALANCE


@send_typing_action
@handler_logging()
def balance_button_add(update, context):
    try:
        query = update.callback_query
        query.answer()
        query.delete_message()
    except:
        ...

    # context.bot.sendMessage(chat_id=update.effective_chat.id, text=add_stock_text,
    #                         reply_markup=make_keyboard_for_modify_to_invest_or_back())

    file = r"tgbot/static/gif/add_stock.mp4"
    file = open(file, 'rb')

    caption = add_stock_text

    context.bot.sendAnimation(chat_id=update.effective_chat.id, animation=file, caption=caption,
                              reply_markup=make_keyboard_for_modify_to_invest_or_back())

    return ADD_STOCK


@send_typing_action
@handler_logging()
def balance_button_delete(update, context):
    try:
        query = update.callback_query
        query.answer()
        query.delete_message()
    except:
        ...

    # context.bot.sendMessage(chat_id=update.effective_chat.id, text=delete_stock_text,
    #                         reply_markup=make_keyboard_for_modify_to_invest_or_back())

    file = r"tgbot/static/gif/delete_stock.mp4"
    file = open(file, 'rb')

    caption = delete_stock_text

    context.bot.sendAnimation(chat_id=update.effective_chat.id, animation=file, caption=caption,
                              reply_markup=make_keyboard_for_modify_to_invest_or_back())

    return DELETE_STOCK


'''
Portfolio
Second menu
Button: Balance
Button: modify to invest
'''


# @send_typing_action
# @handler_logging()
# def modify_to_invest_button(update, context):
#     query = update.callback_query
#
#     query.answer()
#
#     user = User.get_user(update, context)
#     to_invest = Portfolio.get_or_create_by_user(user).to_invest
#     text = change_to_invest_text.format(to_invest=to_invest)
#
#     query.delete_message()
#
#     file = r"tgbot/static/gif/edit_to_invest.gif.mp4"
#     file = open(file, 'rb')
#     context.bot.sendAnimation(chat_id=update.effective_chat.id, animation=file, caption=text)
#
#     return TO_INVEST


@send_typing_action
@handler_logging()
def inline_modify_to_invest(update, context):
    to_invest = float(update.message.text)

    u = User.get_user(update, context)
    p = Portfolio.get_or_create_by_user(u)
    p.update_to_invest(to_invest)
    s = Stock.filter_by_portfolio(p)

    text = changed_to_invest_text.format(to_invest=to_invest)

    update.message.reply_text(text=text)
    time.sleep(2)
    update.message.reply_text(text=modify_question,
                              reply_markup=make_keyboard_for_modify_options())

    return MODIFY_OPTIONS


'''
END
Portfolio
Second menu
Button: Balance
Button: modify to invest
'''


'''
Portfolio
Second menu
Button: Balance
Inline: modify stock check
'''


@send_typing_action
@handler_logging()
def inline_modify_stock_check(update, context):
    try:
        context.bot.edit_message_reply_markup(chat_id=update.effective_chat.id,
                                              message_id=(update.effective_message.message_id - 1))
    except telegram.error.BadRequest:
        ...
    stock = update.message.text.upper()
    u = User.get_user(update, context)
    p = Portfolio.get_or_create_by_user(u)
    list_of_stock_symbols = Stock.list_of_stock_symbols_in_portfolio(p)

    update.message.reply_text(text=change_balance_text_stock_write)

    if stock in list_of_stock_symbols:
        s = Stock.get_stock_by_symbol(p, stock)
        s_symbol = s.symbol
        s_shares = s.shares
        context.user_data['stock_for_change'] = s
        context.user_data['changing_status(new_stock_or_already_existed)'] = 'already_existed'

        update.message.reply_text(modify_balance_stock_symbol_shares.format(symbol=s_symbol, shares=s_shares))

        return STOCK_SHARES
    else:
        context.bot.sendMessage(chat_id=update.effective_chat.id, text=modify_balance_stock_not_in_portfolio)
        time.sleep(2)
        return balance_button_edit(update, context)


@send_typing_action
@handler_logging()
def inline_modify_stock_shares(update, context):
    #write try except block for ',' case
    shares = float(update.message.text)
    stock = context.user_data['stock_for_change']
    Stock.update_shares_of_stock(stock, shares)
    update.message.reply_text(modify_balance_stock_shares_success.format(stock=stock.symbol, shares=stock.shares))
    return STOCK_TOTAL_COSTS


@send_typing_action
@handler_logging()
def inline_modify_stock_total_costs(update, context):
    total_costs = float(update.message.text)
    stock = context.user_data['stock_for_change']
    Stock.update_total_costs_of_stock(stock, total_costs)
    update.message.reply_text(modify_balance_stock_total_costs_success.format(stock=stock.symbol,
                                                                              total_costs=stock.total_costs,
                                                                              shares=stock.shares))
    time.sleep(2)
    if context.user_data['changing_status(new_stock_or_already_existed)'] == 'already_existed':
        return balance_button_edit(update, context)
    elif context.user_data['changing_status(new_stock_or_already_existed)'] == 'new_stock':
        return balance_button_add(update, context)


'''
END
Portfolio
Second menu
Button: Balance
Inline: modify stock check
'''

'''
Portfolio
Second menu
Button: Balance
Inline: wrong inline
'''


@send_typing_action
@handler_logging()
def inline_wrong_ticket_add(update, context):
    try:
        context.bot.edit_message_reply_markup(chat_id=update.effective_chat.id,
                                              message_id=(update.effective_message.message_id - 1))
    except telegram.error.BadRequest:
        ...
    context.bot.sendMessage(chat_id=update.effective_chat.id, text=modify_wrong_ticket)
    time.sleep(2)
    return balance_button_add(update, context)


@send_typing_action
@handler_logging()
def inline_wrong_ticket_edit(update, context):
    try:
        context.bot.edit_message_reply_markup(chat_id=update.effective_chat.id,
                                              message_id=(update.effective_message.message_id - 1))
    except telegram.error.BadRequest:
        ...
    context.bot.sendMessage(chat_id=update.effective_chat.id, text=modify_wrong_ticket)
    time.sleep(2)
    return balance_button_edit(update, context)


@send_typing_action
@handler_logging()
def inline_wrong_ticket_delete(update, context):
    try:
        context.bot.edit_message_reply_markup(chat_id=update.effective_chat.id,
                                              message_id=(update.effective_message.message_id - 1))
    except telegram.error.BadRequest:
        ...
    context.bot.sendMessage(chat_id=update.effective_chat.id, text=modify_wrong_ticket)
    time.sleep(2)
    return balance_button_delete(update, context)


@handler_logging()
def inline_wrong_stock_shares(update, context):
    context.bot.sendMessage(chat_id=update.effective_chat.id, text=modify_wrong_stock_parameters)
    return STOCK_SHARES


@handler_logging()
def inline_wrong_stock_costs(update, context):
    context.bot.sendMessage(chat_id=update.effective_chat.id, text=modify_wrong_stock_parameters)
    return STOCK_TOTAL_COSTS


'''
END
Portfolio
Second menu
Button: Balance
Inline: wrong inline
'''

'''
END
Portfolio
Second menu
Button: Balance
Options - 2 buttons(modify to invest, go back to modify button(in dispatcher)) and 2 inlines(modify_stock_check,
 wrong inline)
'''

'''
Portfolio
Second menu
Button: Add stock
Options - 1 button(go back to modify button(in dispatcher)) and 2 inlines(add_stock_check,
 wrong inline)
'''


@send_typing_action
@handler_logging()
def inline_add_stock_check(update, context):
    try:
        context.bot.edit_message_reply_markup(chat_id=update.effective_chat.id,
                                              message_id=(update.effective_message.message_id - 1))
    except telegram.error.BadRequest:
        ...
    stock = update.message.text.upper()
    u = User.get_user(update, context)
    p = Portfolio.get_or_create_by_user(u)
    list_of_stock_symbols = Stock.list_of_stock_symbols_in_portfolio(p)

    update.message.reply_text(text=add_stock_write)

    if stock in list_of_stock_symbols:
        s = Stock.get_stock_by_symbol(p, stock)

        update.message.reply_text(add_stock_symbol_check_already_have.format(symbol=s.symbol, shares=s.shares))
        time.sleep(2)
        return balance_button_add(update, context)
    else:
        try:
            ticker_price = yf.Ticker(stock).info['regularMarketPrice']
            Stock.create_by_portfolio(portfolio=p, symbol=stock)
            update.message.reply_text(add_stock_symbol_check_success.format(symbol=stock))
            context.user_data['stock_for_change'] = Stock.get_stock_by_symbol(p, stock)
            context.user_data['changing_status(new_stock_or_already_existed)'] = 'new_stock'
            return STOCK_SHARES
        except KeyError:
            context.bot.sendMessage(chat_id=update.effective_chat.id, text=add_stock_not_in_yfinance)
            time.sleep(2)
            return balance_button_add(update, context)


'''
END
Portfolio
Second menu
Button: Add stock
Options - 1 button(go back to modify button(in dispatcher)) and 2 inlines(add_stock_check,
 wrong inline)
'''

'''
Portfolio
Second menu
Button: Delete stock
Options - 1 button(go back to modify button(in dispatcher)) and 2 inlines(add_stock_check,
 wrong inline)
'''


@send_typing_action
@handler_logging()
def inline_delete_stock_check(update, context):
    try:
        context.bot.edit_message_reply_markup(chat_id=update.effective_chat.id,
                                              message_id=(update.effective_message.message_id - 1))
    except telegram.error.BadRequest:
        ...
    stock = update.message.text.upper()
    u = User.get_user(update, context)
    p = Portfolio.get_or_create_by_user(u)
    list_of_stock_symbols = Stock.list_of_stock_symbols_in_portfolio(p)

    update.message.reply_text(text=delete_stock_write)

    if stock in list_of_stock_symbols:
        s = Stock.get_stock_by_symbol(p, stock)
        s_symbol = s.symbol
        s_shares = s.shares
        context.user_data['stock_for_delete'] = s

        update.message.reply_text(text=delete_stock_info.format(symbol=s_symbol, shares=s_shares),
                                  reply_markup=make_keyboard_for_delete_stock())

        return EXACT_DELETE_STOCK
    else:
        context.bot.sendMessage(chat_id=update.effective_chat.id, text=modify_balance_stock_not_in_portfolio)
        time.sleep(3)
        return balance_button_delete(update, context)


@send_typing_action
@handler_logging()
def delete_stock_exact_button(update, context):
    query = update.callback_query

    query.answer()
    stock = context.user_data['stock_for_delete']

    if query.data == 'Yes':
        text = delete_stock_success.format(symbol=stock.symbol)
        stock.delete()
    elif query.data == 'No':
        text = delete_stock_cancel.format(symbol=stock.symbol)

    context.user_data['already_visit_delete_stock'] = True
    query.delete_message()
    context.bot.sendMessage(chat_id=update.effective_chat.id, text=text)
    time.sleep(2)
    return balance_button_delete(update, context)


@handler_logging()
def inline_wrong_ticket_delete_stock(update, context):
    context.bot.sendMessage(chat_id=update.effective_chat.id, text=delete_wrong_ticket)
    return balance_button_delete(update, context)


'''
END
Portfolio
Second menu
Button: Delete stock
Options - 1 button(go back to modify button(in dispatcher)) and 2 inlines(add_stock_check,
 wrong inline)
'''

'''
Portfolio
Second menu
Button: Close
'''


@handler_logging()
def close_button(update, context):
    query = update.callback_query

    query.answer()

    query.edit_message_text(text=close_modify_menu_portfolio)
    return END


@handler_logging()
def close_conversation(update, context):
    try:
        context.bot.edit_message_reply_markup(chat_id=update.effective_chat.id,
                                              message_id=(update.effective_message.message_id - 1))
    except telegram.error.BadRequest:
        ...
    return END


'''
END
Portfolio
Second menu
Button: Close
'''


def broadcast_decision_handler(update, context): #callback_data: CONFIRM_DECLINE_BROADCAST variable from manage_data.py
    """ Entered /broadcast <some_text>.
        Shows text in Markdown style with two buttons:
        Confirm and Decline
    """
    broadcast_decision = update.callback_query.data[len(CONFIRM_DECLINE_BROADCAST):]
    entities_for_celery = update.callback_query.message.to_dict().get('entities')
    entities = update.callback_query.message.entities
    text = update.callback_query.message.text
    if broadcast_decision == CONFIRM_BROADCAST:
        admin_text = f"{message_is_sent}"
        user_ids = list(User.objects.all().values_list('user_id', flat=True))
        broadcast_message.delay(user_ids=user_ids, message=text, entities=entities_for_celery)
    else:
        admin_text = text

    context.bot.edit_message_text(
        text=admin_text,
        chat_id=update.callback_query.message.chat_id,
        message_id=update.callback_query.message.message_id,
        entities=None if broadcast_decision == CONFIRM_BROADCAST else entities
    )