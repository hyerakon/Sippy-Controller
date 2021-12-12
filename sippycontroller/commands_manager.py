from telegram import ParseMode, InlineKeyboardButton, InlineKeyboardMarkup, Update, callbackquery, update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
from sippycontroller import arduino_manager

#emoji

status_emoji = u'\U0001F343'
water_emoji = u'\U0001F4A7'
temperature_emoji = u'\U0001F525'
ph_emoji = u'\U0001F34B'
led_emoji = u'\U0001F4A1'
help_emoji = u'\U0001F647'

stato_led = 'spenti'




def menu(update, context: CallbackContext) -> None:
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
    chat_id = query.message.chat.id
    full_name = query.message.chat.full_name
    
    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    if query.data == 'riepilogo':
        
        print("Richiesto Status del SIP da", full_name)       
        query.answer()
        
        context.bot.send_message(
            chat_id = chat_id,
            text=f"La tua serra Sippy e' in funzione: \n\nIl livello dell'<b>acqua</b> e': {arduino_manager.acqua} ml\nLa <b>temperatura</b> dell'acqua e': {arduino_manager.temp}\nIl <b>PH</b> dell'acqua e': {arduino_manager.ph}\nLo stato dei <b>LED</b> e': {arduino_manager.luce}\n", 
            parse_mode=ParseMode.HTML
            ) 

    elif query.data == 'acqua':
        
        print("Richiesto Livello Acqua del SIP da",full_name)
        query.answer()
        
        context.bot.send_message(
            chat_id = chat_id,
            text=f"Il livello dell'acqua e': {arduino_manager.acqua} ml", 
            parse_mode=ParseMode.HTML
            )
        

    elif query.data == 'temperatura':
        
        print("Richiesto Temperatura Acqua del SIP da",full_name)
        query.answer()        
        
        context.bot.send_message(
            chat_id = chat_id,
            text=f"La temperatura dell'acqua e': {arduino_manager.temp}", 
            parse_mode=ParseMode.HTML
            )

    elif query.data == 'ph':
        
        print("Richiesto Livello PH del SIP da",full_name)
        query.answer()
        #query.edit_message_text(text=f"Il PH dell'acqua e': {arduino_manager.ph}")
                
        context.bot.send_message(
            chat_id = chat_id,
            text=f"Il PH dell'acqua e': {arduino_manager.ph}", 
            parse_mode=ParseMode.HTML
            )
        
        
    elif query.data == 'led':
        
        print("Richiesto Stato dei Led del SIP da",full_name)
        query.answer()
        #query.edit_message_text(text=f"Lo stato dei LED e': {stato}")
                
        if arduino_manager.luce == 1:
            stato = 'accesi'
        else:
            stato = 'spenti'
    
        context.bot.send_message(
            chat_id = chat_id,
            text="Lo stato dei LED e': {stato}", 
            parse_mode=ParseMode.HTML
            )
        

    elif query.data == 'help':
        
        print("Richiesto menu di Aiuto del SIP da",full_name)
        query.answer()

        context.bot.send_message(
            chat_id = chat_id,
            text=f"Usa il comando <b>/menu</b> per avviare il bot", 
            parse_mode=ParseMode.HTML
            )
        


def help_command(update, context) -> None:
    
    full_name = update.message.chat.full_name
    print("Richiesto menu di Aiuto del SIP da",full_name)


    context.bot.send_message(
            chat_id = update.message.chat_id,
            text=f"Usa il comando <b>/menu</b> per avviare il bot", 
            parse_mode=ParseMode.HTML
            )

def getStatus(update, context):

    full_name = update.message.chat.full_name
    print("Richiesto Status del SIP da", full_name)
    
    context.bot.send_message(
            chat_id = update.message.chat_id,
            text=f"La tua serra Sippy e' in funzione: \n\nIl livello dell'<b>acqua</b> e': {arduino_manager.acqua} ml\nLa <b>temperatura</b> dell'acqua e': {arduino_manager.temp}\nIl <b>PH</b> dell'acqua e': {arduino_manager.ph}\nLo stato dei <b>LED</b> e': {arduino_manager.luce}\n", 
            parse_mode=ParseMode.HTML
            ) 

def getWaterLevel(update, context):
    
    full_name = update.message.chat.full_name
    print("Richiesto Livello Acqua del SIP da",full_name)
    
    context.bot.send_message(
            chat_id = update.message.chat_id,
            text=f"Il livello dell'acqua e': {arduino_manager.acqua} ml", 
            parse_mode=ParseMode.HTML
            )

def getTemperature(update, context):
    
    full_name = update.message.chat.full_name
    print("Richiesto Temperatura Acqua del SIP da",full_name)
    
    context.bot.send_message(
            chat_id = update.message.chat_id,
            text=f"La temperatura dell'acqua e': {arduino_manager.temp}", 
            parse_mode=ParseMode.HTML
            )

def getPh(update, context):
    
    full_name = update.message.chat.full_name
    print("Richiesto Livello PH del SIP da",full_name)
    
    context.bot.send_message(
            chat_id = update.message.chat_id,
            text=f"Il PH dell'acqua e': {arduino_manager.ph}", 
            parse_mode=ParseMode.HTML
            )

def getLed(update, context):
    
    full_name = update.message.chat.full_name
    print("Richiesto Stato dei Led del SIP da",full_name)

    if arduino_manager.luce == 1:
        stato = 'accesi'
    else:
        stato = 'spenti'
    
    context.bot.send_message(
            chat_id = update.message.chat_id,
            text="Lo stato dei LED e': {stato}", 
            parse_mode=ParseMode.HTML
            ) 
    

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
