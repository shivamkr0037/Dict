import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

from config import TELEGRAM_BOT_TOKEN
from dictionary import define_word, find_synonyms, find_antonyms

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

DICTIONARY_PAGE_IMAGE_URL = "https://i.imgur.com/YOUR_IMAGE_CODE.jpg"

def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("Ask Definition", callback_data="ask_definition")],
        [InlineKeyboardButton("Find Synonyms", callback_data="find_synonyms")],
        [InlineKeyboardButton("Find Antonyms", callback_data="find_antonyms")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Welcome to the Dictionary Bot! Choose an option:', reply_markup=reply_markup)

def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()

    if query.data == "ask_definition":
        query.edit_message_text("Type /ask followed by a word to get its definition.")
    elif query.data == "find_synonyms":
        query.edit_message_text("Type /synonym followed by a word to find its synonyms.")
    elif query.data == "find_antonyms":
        query.edit_message_text("Type /antonyms followed by a word to find its antonyms.")

def ask(update: Update, context: CallbackContext) -> None:
    word = ' '.join(context.args)
    definition = define_word(word)
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=DICTIONARY_PAGE_IMAGE_URL)
    update.message.reply_text(f"<b>{word.capitalize()}</b>: {definition}", parse_mode=ParseMode.HTML)

def synonym(update: Update, context: CallbackContext) -> None:
    word = ' '.join(context.args)
    synonyms = find_synonyms(word)
    context.bot.send_photo(chat_id=update.effective_chat
