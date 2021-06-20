import datetime
import re
import time

import os

import telegram
from django.utils import timezone
from telegram.ext import (
    ConversationHandler
)
from telegram.utils import helpers

from tgbot import utils

from tgbot.handlers import text_ru, text_eng
from tgbot.handlers.keyboard_utils import keyboard_confirm_decline_broadcasting, make_keyboard_for_portfolio_net, \
    make_keyboard_for_language_command
from tgbot.handlers.utils import handler_logging, send_typing_action, check_language
from tgbot.models import User, Portfolio, Stock
from tgbot.portfolio_utils import portfolio_update, portfolio_output_efficiency
# from tgbot.tasks import broadcast_message_rate_bot_pls
from tgbot.utils import extract_user_data_from_update

CURRENCY, TRADE_EXPERIENCE, HELP, CLOSE_PORTFOLIO, INTERESTED_MARK = range(5)

MODIFY, MODIFY_OPTIONS, BALANCE, TO_INVEST, STOCK_SHARES, \
STOCK_TOTAL_COSTS, ADD_STOCK, EDIT_STOCK, DELETE_STOCK, EXACT_DELETE_STOCK = range(66, 76)

END = ConversationHandler.END

from django.core.cache import cache


@send_typing_action
@handler_logging()
def command_start(update, context):
    try:
        context.bot.edit_message_reply_markup(chat_id=update.effective_chat.id,
                                              message_id=(update.effective_message.message_id - 1))
    except telegram.error.BadRequest:
        ...

    u, created = User.get_user_and_created(update, context)
    user_id = utils.extract_user_id_from_update(update)

    if f'language_{user_id}' not in cache:
        cache.set(f'language_{user_id}', u.language_code, timeout=None)

    if cache.get(f'language_{user_id}') == 'ru':
        language = text_ru
    else:
        language = text_eng

    file = r"tgbot/static/gif/portfolio.mp4"
    file = open(file, 'rb')

    # bot = context.bot
    # url = helpers.create_deep_linked_url(bot.username, payload=str(u.user_id), group=False)

    # welcome_text_full = welcome_text + static_text.start_created_2nd_string
    # context.bot.sendAnimation(chat_id=update.effective_chat.id, animation=file, caption=welcome_text_full)

    welcome_text = language .start_created.format(first_name=u.first_name)
    welcome_text_full = welcome_text + language.start_created_portfolio + language.start_created_portfolio_example
    update.message.reply_text(text=welcome_text_full)
    update.message.reply_animation(animation=file)
    time.sleep(3)
    update.message.reply_text(text=language.start_change_language)
    # time.sleep(3)
    # text = language.start_created_feedback + language.start_created_share_command
    # update.message.reply_text(text=text)

    # update.message.reply_text(text=static_text.start_created_feedback)
    # update.message.reply_text(text=static_text.start_created_share.format(share_url=url))
    # update.message.reply_text(text=static_text.start_created_share_command)

    if cache.get(f'language_{user_id}') == 'ru':
        time.sleep(3)
        update.message.reply_text(text=language.start_created_inbaze)

    # broadcast_message_rate_bot_pls.apply_async(args=(u.user_id,), countdown=100)


@check_language
@handler_logging()
def command_feedback(update, context, language):
    try:
        context.bot.edit_message_reply_markup(chat_id=update.effective_chat.id,
                                              message_id=(update.effective_message.message_id - 1))
    except telegram.error.BadRequest:
        ...

    user_id = utils.extract_user_id_from_update(update)

    if cache.get(f'language_{user_id}') == 'ru':
        link = os.getenv("GOOGLE_FORM_LINK")
    else:
        link = os.getenv("GOOGLE_FORM_LINK_ENG")

    update.message.reply_text(text=language.feedback.format(google_form_link=link))


@check_language
@send_typing_action
@handler_logging()
def command_portfolio(update, context, language):
    try:
        context.bot.edit_message_reply_markup(chat_id=update.effective_chat.id,
                                              message_id=(update.effective_message.message_id - 1))
    except telegram.error.BadRequest:
        ...

    update.message.reply_text(text=language.wait_for_portfolio)

    u = User.get_user(update, context)
    p = Portfolio.get_or_create_by_user(u)
    s = Stock.filter_by_portfolio(p)

    portfolio_update(p, s)
    text = portfolio_output_efficiency(p, s)
    # text = static_text.your_portfolio + portfolio_summary(p, s)
    context.bot.delete_message(chat_id=update.effective_chat.id,
                               message_id=update.effective_message.message_id + 1)
    update.message.reply_text(text=text, reply_markup=make_keyboard_for_portfolio_net(language),
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


@check_language
def broadcast_command_with_message(update, context, language):
    """ Type /broadcast <some_text>. Then check your message in Markdown format and broadcast to users."""
    u = User.get_user(update, context)
    # user_id = extract_user_data_from_update(update)['user_id']


    if not u.is_admin:
        text = language.broadcast_no_access
        markup = None

    else:
        text = f"{update.message.text.replace(f'{language.broadcast_command} ', '')}"
        markup = keyboard_confirm_decline_broadcasting()

    try:
        context.bot.send_message(
            text=text,
            chat_id=u.user_id,
            parse_mode=telegram.ParseMode.MARKDOWN,
            reply_markup=markup
        )
    except telegram.error.BadRequest as e:
        place_where_mistake_begins = re.findall(r"offset (\d{1,})$", str(e))
        text_error = text_ru.error_with_markdown
        if len(place_where_mistake_begins):
            text_error += f"{text_ru.specify_word_with_error}'{text[int(place_where_mistake_begins[0]):].split(' ')[0]}'"
        context.bot.send_message(
            text=text_error,
            chat_id=u.user_id
        )


@check_language
@handler_logging()
def command_share_bot(update, context, language):
    try:
        context.bot.edit_message_reply_markup(chat_id=update.effective_chat.id,
                                              message_id=(update.effective_message.message_id - 1))
    except telegram.error.BadRequest:
        ...

    update.message.reply_text(text=language.share_command)
    u = User.get_user(update, context)
    bot = context.bot
    url = helpers.create_deep_linked_url(bot.username, payload=str(u.user_id), group=False)
    text = language.share_message.format(share_url=url)
    update.message.reply_text(text=text)


@check_language
@handler_logging()
def command_language(update, context, language):
    try:
        context.bot.edit_message_reply_markup(chat_id=update.effective_chat.id,
                                              message_id=(update.effective_message.message_id - 1))
    except telegram.error.BadRequest:
        ...

    update.message.reply_text(text=language.language_ask, reply_markup=make_keyboard_for_language_command(language))