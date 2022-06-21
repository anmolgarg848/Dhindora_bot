# Enable Logging 
import logging as log
from telegram.ext import Updater , CommandHandler,MessageHandler,Filters
# print(log)
# Decides Level Of Warning 
log.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level= log.INFO)

logger = log.getLogger(__name__)

# Create Updater--> Needs Telegram Token 
TOKEN = "5571563522:AAEczm874wVQKtCu2rYYxbulhxFkwcXa24c"

# Start Function when user says /start
def start(bot,update):
    # print(update)
    author = update.message.from_user.first_name  
    reply = "Hi! {}".format(author)
    # msg = update.message.text 
    bot.send_message(chat_id = update.message.chat_id,text=reply )
    
def _help(bot,update):
    help_txt = "Hey! I am Here To Help You "
    bot.send_message(chat_id = update.message.chat_id,text=help_txt )
     
def echo_text(bot,update):
    reply = update.message.text
    bot.send_message(chat_id = update.message.chat_id,text=reply )
def echo_sticker(bot,update):
    bot.send_sticker(chat_id = update.message.chat_id,sticker=update.message.sticker.file_id )
def error(bot,update):
    logger.error("Update '%s' Caused Error '%s' ",update,update.error)
    
# Handler Function 
def main():
    updater = Updater(TOKEN)    
    # Creating Dispatcher Object --> Handles All the Updates On Bot 
    dp = updater.dispatcher
    # For a Dispatcher We need Multiples Handler's 
    dp.add_handler(CommandHandler("start",start))
    dp.add_handler(CommandHandler("help",_help))
    dp.add_handler(MessageHandler(Filters.text,echo_text))
    dp.add_handler(MessageHandler(Filters.sticker,echo_sticker))
    dp.add_error_handler(error)    
    # Just Triggers The Polling 
    updater.start_polling()
    logger.info("Started Polling  . . .  . ")
    updater.idle()
    
if __name__ == "__main__":
    main()

 






