import datetime
from django.utils.timezone import now

# Telegram imports
import telegram

# Local imports
from tgbot.handlers import text_ru
from tgbot.models import User

def admin(update, context):
    """ Show help info about all secret admins commands """
    u = User.get_user(update, context)
    if not u.is_admin:
        return update.message.reply_text(text_ru.not_admin_answer)

    return update.message.reply_text(text_ru.secret_admin_commands)
    

def stats(update, context):
    """ Show help info about all secret admins commands """
    u = User.get_user(update, context)
    if not u.is_admin:
        return update.message.reply_text(text_ru.not_admin_answer)

    text = f"""
*Users*: {User.objects.count()}
*24h active*: {User.objects.filter(updated_at__gte=now() - datetime.timedelta(hours=24)).count()}
    """

    return update.message.reply_text(
        text, 
        parse_mode=telegram.ParseMode.MARKDOWN,
        disable_web_page_preview=True,
    )