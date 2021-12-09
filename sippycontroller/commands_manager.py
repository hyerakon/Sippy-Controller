from telegram import ParseMode

def getStatus(update, context):
    print("hello")
    todo(update, context)


def getWaterLevel(update, context):
    print("hello")
    todo(update, context)

def getTemperature(update, context):
    print("hello")
    todo(update, context)

def getPh(update, context):
    print("hello")
    todo(update, context)

def getLed(update, context):
    print("hello")
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
