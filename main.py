import telebot
import constants

bot = telebot.TeleBot(constants.token)

#  bot.send_message(53257673, "Huy\nPizda\nSkovoroda")
#  upd = bot.get_updates()
#  print(upd)
#  last_upd = upd[-1]
#  message_from_user = last_upd.message
#  print(message_from_user)

print(bot.get_me())


def log(message, answer):
    print("\n -----")
    from datetime import datetime
    print(datetime.now())
    print("Message from {0} {1}. (id = {2}) \n Text - {3}".format(message.from_user.first_name,
                                                                  message.from_user.last_name,
                                                                  str(message.from_user.id),
                                                                  message.text))
    print(answer)


@bot.message_handler(commands=['start'])
def handle_text(message):
    bot.send_message(message.chat.id, "We already got started, you dumb moron!")


@bot.message_handler(commands=['settings'])
def handle_text(message):
    bot.send_message(message.chat.id, "Settings sample message")


@bot.message_handler(commands=['help'])
def handle_text(message):
    bot.send_message(message.chat.id, "Help sample message")


@bot.message_handler(content_types=['document'])
def handle_document(message):
    bot.send_message(message.chat.id, "Document has received")


@bot.message_handler(content_types=['audio'])
def handle_audio(message):
    bot.send_message(message.chat.id, "Audio has received")


@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    bot.send_message(message.chat.id, "Photo has received")


@bot.message_handler(content_types=['sticker'])
def handle_sticker(message):
    bot.send_message(message.chat.id, "Sticker has received")


@bot.message_handler(content_types=['text'])
def handle_text(message):
    answer = "Simple message has received"
    bot.send_message(message.chat.id, answer)
    log(message, answer)


#@bot.message_handler(content_types=['text'])
#def handle_text(message):
#   if message.text == "a":
#        bot.send_message(message.chat.id, "B")
#    elif message.text == "b":
#        bot.send_message(message.chat.id, "C")
#    else:
#        bot.send_message(message.chat.id, "You such a stupid asshole, you can't play this game, kill yourself")

bot.polling(none_stop=True, interval=0)






