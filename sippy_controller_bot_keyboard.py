from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, CallbackContext
from sippycontroller import command_logger, commands_manager, token_manager, arduino_manager

TOKEN=token_manager.getTokens(0)
GROUP_ID=token_manager.getTokens(1)

def main():
	print('BOT START!!!!')
	command_logger.command_log('Sippy Controller', 'Avviato')
	
	upd = Updater(TOKEN, use_context=True)
	disp = upd.dispatcher
	
	disp.add_handler(CommandHandler("start",commands_manager.menu))
	disp.add_handler(CommandHandler("menu",commands_manager.menu))
	disp.add_handler(CommandHandler("riepilogo",commands_manager.getStatus))
	disp.add_handler(CommandHandler("acqua",commands_manager.getWaterLevel))
	disp.add_handler(CommandHandler("temperatura",commands_manager.getTemperature))
	disp.add_handler(CommandHandler("ph",commands_manager.getPh))
	disp.add_handler(CommandHandler("led",commands_manager.getLed))
	disp.add_handler(CallbackQueryHandler(commands_manager.button))
	disp.add_handler(CommandHandler("aiuto",commands_manager.help_command))
	
	#arduino_manager.arduino_setup()
	#arduino_manager.arduino_loop()

	upd.start_polling()

	upd.idle()

if __name__=='__main__':
	main()





