import telebot
import search

bot = telebot.TeleBot('1196220678:AAGOGKvVO00fd7MlH4F4qNxmfGQfVjj34WM')
user_id = 0

url = 'https://ru.wikipedia.org/wiki/'


@bot.message_handler(commands=['start'])
def handle_command_start(message):
    global user_id
    user_id = message.from_user.id

    bot.send_message(user_id, f'Hello, {message.from_user.username}!\n'
                              f'Send me the word you want to google and I will find it &#128269', parse_mode='html')


@bot.message_handler(content_types=['text'])
def handle_text(message):
    bot.send_message(user_id, search.search_text(message.text, url), parse_mode='html')


bot.polling()
