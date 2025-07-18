import os
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import psycopg2
from datetime import datetime, timedelta

BOT_TOKEN = os.getenv("BOT_TOKEN")
DATABASE_URL = os.getenv("DATABASE_URL")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def start(update, context):
    update.message.reply_text("Welcome please enter chatroom to meet new people round the world")

def help_command(update, context):
    update.message.reply_text("Commands:\n/start - Welcome Message\n/help - Help Info")

def error(update, context):
    logger.warning(f'Update {update} caused error {context.error}')

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()