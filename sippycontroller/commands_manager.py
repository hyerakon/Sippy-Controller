from telegram import ParseMode, InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
from sippycontroller import arduino_manager

#emoji

status_emoji = u'\U0001F343'
water_emoji = u'\U0001F4A7'
temperature_emoji = u'\U0001F525'
ph_emoji = u'\U0001F34B'
led_emoji = u'\U0001F4A1'
help_emoji = u'\U0001F647'





def start(update, context: CallbackContext) -> None:
    """Sends a message with three inline buttons attached."""
    keyboard = [
        [
            InlineKeyboardButton("Riepilogo "+status_emoji, callback_data='riepilogo'),
            InlineKeyboardButton("Acqua "+water_emoji, callback_data='acqua')
        ],
        [
            InlineKeyboardButton("Temperatura "+temperature_emoji, callback_data='temperatura'),
            InlineKeyboardButton("PH "+ph_emoji, callback_data='ph')
        ],
        [
            InlineKeyboardButton("LED "+led_emoji, callback_data='led'),
            InlineKeyboardButton("Aiuto! "+help_emoji, callback_data='help')           
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Scegli un\' opzione:', reply_markup=reply_markup)

def button(update: Update, context: CallbackContext) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    if query.data == 'riepilogo':
        query.answer()
        query.edit_message_text(text=f"La tua serra Sippy e' in funzione: \nIl livello dell'acqua e': {arduino_manager.acqua}\nLa temperatura dell'acqua e': {arduino_manager.temp}\nIl PH dell'acqua e': {arduino_manager.ph}\nLo stato dei led e': {arduino_manager.luce}\n")
    elif query.data == 'acqua':
        query.answer()
        query.edit_message_text(text=f"Il livello dell'acqua e': {arduino_manager.acqua}")
    elif query.data == 'temperatura':
        query.answer()
        query.edit_message_text(text=f"La temperatura dell'acqua e': {arduino_manager.temp}")
    elif query.data == 'ph':
        query.answer()
        query.edit_message_text(text=f"Il PH dell'acqua e': {arduino_manager.ph}")
    elif query.data == 'led':
        query.answer()
        query.edit_message_text(text=f"Lo stato dei led e': {arduino_manager.luce}")
    elif query.data == 'aiuto':
        query.answer()
        query.edit_message_text(text=f"Usa il comando '\start' per avviare il bot")            
    


def help_command(update: Update, context: CallbackContext) -> None:
    """Displays info on how to use the bot."""
    update.message.reply_text("Use /start to test this bot.")

def getStatus(update, context):
    print("Richiesto Status del SIP da",update.message.from_user.username)
    todo(update, context)  

def getWaterLevel(update, context):
    print("Richiesto Livello Acqua del SIP da",update.message.from_user)
    todo(update, context)

def getTemperature(update, context):
    print("Richiesto Temperatura Acqua del SIP da",update.message.from_user)
    todo(update, context)

def getPh(update, context):
    print("Richiesto Livello PH del SIP da",update.message.from_user)
    todo(update, context)

def getLed(update, context):
    print("Richiesto Stato dei Led del SIP da",update.message.chat_id)
    todo(update, context)


#def hello(update, context):
#    todo(update, context)
    #chat_id = update.message.chat_id
    #message = "hello"
    #context.bot.send_message(chat_id=chat_id, text='<b>hello</b>', parse_mode=ParseMode.HTML)

def todo(update, context):
    chat_id = update.message.chat_id
    
    context.bot.send_message(
        chat_id=chat_id, 
        text='<b>Scusa</b>,Ma sono ignorante come un leghista e non so fare quello che mi chiedi.', 
        parse_mode=ParseMode.HTML
        )


def _test():
    print ("Start: Command Manager")


if __name__ == "__main__":
    _test()
