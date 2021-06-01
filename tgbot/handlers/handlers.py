import datetime
import telegram
import yfinance as yf


from tgbot.handlers.manage_data import CONFIRM_DECLINE_BROADCAST, CONFIRM_BROADCAST
from tgbot.handlers.static_text import unlock_secret_room, message_is_sent, start_currency_button_answer_button,\
    start_currency_dollar_text, start_currency_euro_text, start_trade_experience_button_answer_yes_button,\
    start_trade_experience_button_answer_no_button, start_trade_experience, start_trade_experience_recommendation_text,\
    start_help_tune_portfolio_text, start_help_tune_portfolio_question_text, start_important_to_invest_text,\
    start_help_button_answer_yes_button, start_help_button_answer_no_button, start_write_portfolio_command_text,\
    modify_question, change_balance_text, change_to_invest_text, changed_to_invest_text, modify_wrong_ticket, \
    modify_balance_stock_not_in_portfolio, modify_balance_stock_symbol_shares, modify_balance_stock_shares_success, \
    change_balance_text_stock_write, close_modify_menu_portfolio, close_modify_menu_nested_after_start, \
    modify_balance_stock_total_costs_success, add_stock_text, add_stock_symbol_check_already_have, \
    add_stock_symbol_check_success, add_stock_not_in_yfinance, answer_on_mark, delete_stock_text, delete_stock_write, \
    delete_stock_info, delete_stock_success, delete_stock_cancel, add_wrong_ticket, delete_wrong_ticket, add_stock_write, \
    wait_update
from tgbot.handlers.keyboard_utils import make_keyboard_for_start_trade_experience, make_keyboard_for_start_help,\
    make_keyboard_for_modify_options, make_keyboard_for_modify_to_invest_or_back, make_keyboard_for_add_stock_go_back, \
    make_keyboard_for_interested_in_bot, make_keyboard_for_delete_stock, make_keyboard_for_portfolio_total, \
    make_keyboard_for_portfolio_net, make_keyboard_for_portfolio_costs, make_keyboard_for_portfolio_amount, \
    make_keyboard_for_portfolio_efficiency
from tgbot.handlers.utils import handler_logging, send_typing_action

from tgbot.handlers.commands import TRADE_EXPERIENCE, CURRENCY, HELP, CLOSE_PORTFOLIO, END, INTERESTED_MARK
from tgbot.handlers.commands import MODIFY, MODIFY_OPTIONS, TO_INVEST, BALANCE, STOCK_SHARES, STOCK_TOTAL_COSTS,\
    ADD_STOCK, DELETE_STOCK, EXACT_DELETE_STOCK

from tgbot.models import User, Portfolio, Stock
# from tgbot.tasks import broadcast_message
from tgbot.utils import extract_user_data_from_update
from django.utils import timezone
from telegram.ext import (
    ConversationHandler
)

from tgbot.portfolio_utils import portfolio_summary, portfolio_output_net, portfolio_output_total, \
    portfolio_output_amount, portfolio_output_costs, portfolio_output_efficiency, portfolio_update



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
Start command functions
'''


@send_typing_action
@handler_logging()
def currency_button(update, context):
    query = update.callback_query

    query.answer()

    if query.data == 'dollar':
        currency = start_currency_dollar_text
    elif query.data == 'euro':
        currency = start_currency_euro_text

    User.get_user_and_updated_currency(update, context, currency=query.data)
    query.edit_message_text(text=start_currency_button_answer_button.format(currency=currency))
    context.bot.sendMessage(chat_id=update.effective_chat.id, text=start_trade_experience,
                            reply_markup=make_keyboard_for_start_trade_experience())

    return TRADE_EXPERIENCE


@send_typing_action
@handler_logging()
def trade_experience_button(update, context):
    query = update.callback_query

    query.answer()

    if query.data == 'Yes':
        trade_experience = start_trade_experience_button_answer_yes_button
    elif query.data == 'No':
        trade_experience = start_trade_experience_button_answer_no_button

    User.get_user_and_updated_trade_experience(update, context, trade_experience=query.data)
    query.edit_message_text(text=trade_experience)
    context.bot.sendMessage(chat_id=update.effective_chat.id, text=start_trade_experience_recommendation_text)
    context.bot.sendMessage(chat_id=update.effective_chat.id, text=start_help_tune_portfolio_text)
    context.bot.sendMessage(chat_id=update.effective_chat.id, text=start_help_tune_portfolio_question_text,
                            reply_markup=make_keyboard_for_start_help())

    return HELP


@send_typing_action
@handler_logging()
def help_button(update, context):
    query = update.callback_query

    query.answer()

    if query.data == 'Yes':
        query.edit_message_text(text=start_help_button_answer_yes_button)
        context.bot.sendMessage(chat_id=update.effective_chat.id, text=start_important_to_invest_text)
        context.bot.sendMessage(chat_id=update.effective_chat.id, text=start_write_portfolio_command_text)

        return MODIFY

    elif query.data == 'No':
        query.edit_message_text(text=start_help_button_answer_no_button)

        return ConversationHandler.END



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


@send_typing_action
@handler_logging()
def modify_button(update, context):
    query = update.callback_query

    query.answer()

    #query.edit_message_text(text=modify_question, reply_markup=make_keyboard_for_modify_options())
    query.edit_message_reply_markup()
    context.bot.sendMessage(chat_id=update.effective_chat.id, text=modify_question,
                            reply_markup=make_keyboard_for_modify_options())
    return MODIFY_OPTIONS


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
def balance_button(update, context):
    try:
        query = update.callback_query
        query.answer()
        query.edit_message_text(text=change_balance_text, reply_markup=make_keyboard_for_modify_to_invest_or_back())
    except AttributeError:
        context.bot.sendMessage(chat_id=update.effective_chat.id, text=change_balance_text,
                                reply_markup=make_keyboard_for_modify_to_invest_or_back())
    return BALANCE

'''
Portfolio
Second menu
Button: Balance
Button: modify to invest
'''


@send_typing_action
@handler_logging()
def modify_to_invest_button(update, context):
    query = update.callback_query

    query.answer()

    user = User.get_user(update, context)
    to_invest = Portfolio.get_or_create_by_user(user).to_invest
    text = change_to_invest_text.format(to_invest=to_invest)
    query.edit_message_text(text=text)

    return TO_INVEST


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
        return balance_button(update, context)


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
    if context.user_data['changing_status(new_stock_or_already_existed)'] == 'already_existed':
        return balance_button(update, context)
    elif context.user_data['changing_status(new_stock_or_already_existed)'] == 'new_stock':
        return add_stock_button(update, context)


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
def inline_wrong_ticket(update, context):
    context.bot.sendMessage(chat_id=update.effective_chat.id, text=modify_wrong_ticket)
    return balance_button(update, context)


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
def add_stock_button(update, context):
    try:
        query = update.callback_query
        query.answer()
        query.edit_message_text(text=add_stock_text, reply_markup=make_keyboard_for_add_stock_go_back())
    except AttributeError:
        context.bot.sendMessage(chat_id=update.effective_chat.id, text=add_stock_text,
                                reply_markup=make_keyboard_for_add_stock_go_back())
    return ADD_STOCK


@send_typing_action
@handler_logging()
def inline_add_stock_check(update, context):
    stock = update.message.text.upper()
    u = User.get_user(update, context)
    p = Portfolio.get_or_create_by_user(u)
    list_of_stock_symbols = Stock.list_of_stock_symbols_in_portfolio(p)

    update.message.reply_text(text=add_stock_write)

    if stock in list_of_stock_symbols:
        s = Stock.get_stock_by_symbol(p, stock)

        update.message.reply_text(add_stock_symbol_check_already_have.format(symbol=s.symbol, shares=s.shares))

        return add_stock_button(update, context)
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
            return add_stock_button(update, context)


@send_typing_action
@handler_logging()
def inline_wrong_ticket_add_stock(update, context):
    context.bot.sendMessage(chat_id=update.effective_chat.id, text=add_wrong_ticket)
    return add_stock_button(update, context)


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
def delete_stock_button(update, context):
    try:
        if context.user_data['already_visit_delete_stock']:
            context.bot.sendMessage(chat_id=update.effective_chat.id, text=delete_stock_text,
                                    reply_markup=make_keyboard_for_add_stock_go_back())
        else:
            query = update.callback_query
            query.answer()
            query.edit_message_text(text=delete_stock_text, reply_markup=make_keyboard_for_add_stock_go_back())
    except AttributeError:
        context.bot.sendMessage(chat_id=update.effective_chat.id, text=delete_stock_text,
                                reply_markup=make_keyboard_for_add_stock_go_back())
    except KeyError:
        query = update.callback_query
        query.answer()
        query.edit_message_text(text=delete_stock_text, reply_markup=make_keyboard_for_add_stock_go_back())

    context.user_data['already_visit_delete_stock'] = False
    return DELETE_STOCK


@send_typing_action
@handler_logging()
def inline_delete_stock_check(update, context):
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
        return delete_stock_button(update, context)


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
    query.edit_message_text(text=text)
    return delete_stock_button(update, context)


@send_typing_action
@handler_logging()
def inline_wrong_ticket_delete_stock(update, context):
    context.bot.sendMessage(chat_id=update.effective_chat.id, text=delete_wrong_ticket)
    return delete_stock_button(update, context)


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


@send_typing_action
@handler_logging()
def close_button(update, context):
    query = update.callback_query

    query.answer()

    query.edit_message_text(text=close_modify_menu_portfolio)
    return END
    # try:
    #     if context.user_data['NESTED_CLOSE_PORTFOLIO']:
    #         query.edit_message_text(text=close_modify_menu_nested_after_start,
    #                                 reply_markup=make_keyboard_for_interested_in_bot())
    #         context.user_data['NESTED_CLOSE_PORTFOLIO'] = False
    #         return INTERESTED_MARK
    #     else:
    #         query.edit_message_text(text=close_modify_menu_portfolio)
    #         return END
    # except:
    #     query.edit_message_text(text=close_modify_menu_portfolio)
    #     return END


@send_typing_action
@handler_logging()
def mark_interested_button(update, context):
    query = update.callback_query

    query.answer()

    User.get_user_and_updated_interested_mark(update, context, mark=query.data)
    query.edit_message_text(text=answer_on_mark)

    # return END


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