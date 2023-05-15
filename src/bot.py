import logging

from telegram import Update

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

from config import TELEGRAM_BOT_TOKEN

from dictionary import define_word, find_synonyms, find_antonyms

logging.basicConfig(

    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO

)

logger = logging.getLogger(__name__)

def start(update: Update, context: CallbackContext) -> None:

    update.message.reply_text('Welcome to the Dictionary Bot! Type /ask, /synonym, or /antonyms followed by a word.')

def ask(update: Update, context: CallbackContext) -> None:

    word = ' '.join(context.args)

    definition = define_word(word)

    update.message.reply_text(definition)

def synonym(update: Update, context: CallbackContext) -> None:

    word = ' '.join(context.args)

    synonyms = find_synonyms(word)

    update.message.reply_text(', '.join(synonyms))

def antonyms(update: Update, context: CallbackContext) -> None:

    word = ' '.join(context.args)

    antonyms = find_antonyms(word)

    update.message.reply_text(', '.join(antonyms))

def main() -> None:

    updater = Updater(TELEGRAM_BOT_TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))

    dispatcher.add_handler(CommandHandler("ask", ask))

    dispatcher.add_handler(CommandHandler("synonym", synonym))

    dispatcher.add_handler(CommandHandler("antonyms", antonyms))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':

    main()
