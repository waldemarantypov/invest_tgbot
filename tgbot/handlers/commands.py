import telegram
import datetime
import re

from tgbot.handlers.keyboard_utils import keyboard_confirm_decline_broadcasting, make_keyboard_for_start_currency, \
    make_keyboard_for_start_trade_experience, make_keyboard_for_portfolio_net, make_keyboard_for_start_help
from tgbot.handlers.static_text import start_help_tune_portfolio_text, start_trade_experience_recommendation_text
from tgbot.handlers.utils import handler_logging, send_typing_action
from tgbot.models import User, Portfolio, Stock, Transaction
from django.utils import timezone
from tgbot.handlers import static_text
from telegram.ext import (
    ConversationHandler
)

from tgbot.portfolio_utils import portfolio_summary, portfolio_update, portfolio_output_efficiency

from tgbot.utils import extract_user_data_from_update

CURRENCY, TRADE_EXPERIENCE, HELP, CLOSE_PORTFOLIO, INTERESTED_MARK = range(5)

MODIFY, MODIFY_OPTIONS, BALANCE, TO_INVEST, STOCK_SHARES, \
STOCK_TOTAL_COSTS, ADD_STOCK, DELETE_STOCK, EXACT_DELETE_STOCK = range(66, 75)

END = ConversationHandler.END


@send_typing_action
@handler_logging()
def command_start(update, context):
    try:
        context.bot.edit_message_reply_markup(chat_id=update.effective_chat.id,
                                              message_id=(update.effective_message.message_id - 1))
    except telegram.error.BadRequest:
        ...

    context.user_data['NESTED_CLOSE_PORTFOLIO'] = True

    u, created = User.get_user_and_created(update, context)

    # if created:
    #     welcome_text = static_text.start_created.format(first_name=u.first_name)
    # else:
    #     welcome_text = static_text.start_not_created.format(first_name=u.first_name)

    welcome_text = static_text.start_created.format(first_name=u.first_name)

    # update.message.reply_text(text=text,
    #                           reply_markup=make_keyboard_for_start_command())

    update.message.reply_text(text=welcome_text)
    # time.sleep(1)
    update.message.reply_text(text=static_text.start_intro)
    # time.sleep(2)

    # update.message.reply_text(text=static_text.start_currency, reply_markup=make_keyboard_for_start_currency())
    # return CURRENCY

    update.message.reply_text(text=start_trade_experience_recommendation_text)
    # time.sleep(3)
    update.message.reply_text(text=start_help_tune_portfolio_text)
    # time.sleep(3)
    update.message.reply_text(text=static_text.start_help_tune_portfolio_question_text,
                              reply_markup=make_keyboard_for_start_help())
    return HELP


@send_typing_action
@handler_logging()
def command_portfolio(update, context):
    try:
        context.bot.edit_message_reply_markup(chat_id=update.effective_chat.id,
                                              message_id=(update.effective_message.message_id - 1))
    except telegram.error.BadRequest:
        ...

    update.message.reply_text(text=static_text.wait_for_portfolio)
    u = User.get_user(update, context)
    p = Portfolio.get_or_create_by_user(u)
    s = Stock.filter_by_portfolio(p)

    portfolio_update(p, s)
    text = portfolio_output_efficiency(p, s)
    # text = static_text.your_portfolio + portfolio_summary(p, s)
    update.message.reply_text(text=text, reply_markup=make_keyboard_for_portfolio_net(),
                              parse_mode=telegram.ParseMode.HTML)

    return MODIFY


def stats(update, context):
    """ Show help info about all secret admins commands """
    u = User.get_user(update, context)
    if not u.is_admin:
        return update.message.reply_text('Ты ж вроде не админ, так что стату не увидишь')

    text = f"""
*Users*: {User.objects.count()}
*24h active*: {User.objects.filter(updated_at__gte=timezone.now() - datetime.timedelta(hours=24)).count()}
    """

    return update.message.reply_text(
        text,
        parse_mode=telegram.ParseMode.MARKDOWN,
        disable_web_page_preview=True,
    )


def broadcast_command_with_message(update, context):
    """ Type /broadcast <some_text>. Then check your message in Markdown format and broadcast to users."""
    u = User.get_user(update, context)
    user_id = extract_user_data_from_update(update)['user_id']

    if not u.is_admin:
        text = static_text.broadcast_no_access
        markup = None

    else:
        text = f"{update.message.text.replace(f'{static_text.broadcast_command} ', '')}"
        markup = keyboard_confirm_decline_broadcasting()

    try:
        context.bot.send_message(
            text=text,
            chat_id=user_id,
            parse_mode=telegram.ParseMode.MARKDOWN,
            reply_markup=markup
        )
    except telegram.error.BadRequest as e:
        place_where_mistake_begins = re.findall(r"offset (\d{1,})$", str(e))
        text_error = static_text.error_with_markdown
        if len(place_where_mistake_begins):
            text_error += f"{static_text.specify_word_with_error}'{text[int(place_where_mistake_begins[0]):].split(' ')[0]}'"
        context.bot.send_message(
            text=text_error,
            chat_id=user_id
        )
