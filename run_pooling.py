import os, django
import logging


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dtb.settings')
django.setup()

# from tgbot.handlers.dispatcher import run_pooling

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

# if __name__ == "__main__":
#     run_pooling()