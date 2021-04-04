from telegram.ext import *
import responses as r
import moviedatabase as key


print("Movbot has started....")  # To indicate the bot has started


# Start command for the bot - response for /start
def start_command(update, context):
    update.message.reply_text('Greet the bot to begin!')


# Help command for the bot - response for /help
def help_command(update, context):
    update.message.reply_text('This bot is to recommend you a movie in your chosen language and genre!')


# For generating the responses based on the input text
def handle_message(update, context):
    text = str(update.message.text).lower()
    response = r.sample_responses(text)

    update.message.reply_text(response)


# For Handling any errors
def error(update, context):
    print(f"Update{update} caused error {context.error}")


# Main function
def main():
    updater = Updater(key.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


# Calling main
main()
