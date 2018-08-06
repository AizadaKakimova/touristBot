import telebot
import constants
import urllib.request, json

bot = telebot.TeleBot(constants.token)

#bot.send_message(488113841, "bot is working...")

#upd = bot.get_updates()
#print(upd)
#last_upd = upd[-1]
#message_from_user = last_upd.message
#print(message_from_user)

print(bot.get_me())

@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row("Где поесть в Алматы ?")
    user_markup.row("Где отдохнуть в Алматы ?")
    user_markup.row("Где переночевать в Алматы ?")
    user_markup.row("Построить свой план")
    bot.send_message(message.chat.id, 'Добро пожаловать', reply_markup = user_markup)

@bot.message_handler(commands=['help'])
def handle_text(message):
    bot.send_message(message.chat.id, "Помощь")

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "Где поесть в Алматы ?":
        keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button = telebot.types.KeyboardButton(text="Отправить местоположение", request_location=True)
        keyboard.add(button)
        bot.send_message(message.chat.id, "Отправьте пожалуйста локацию: ", reply_markup=keyboard)
    else:
        bot.send_message(message.chat.id, "Ошибка")

@bot.message_handler(content_types=['location'])
def handle_location(message):
    lat = message.location.latitude
    lng = message.location.longitude
    #bot.send_location(message.chat.id, lat, lng)
    with urllib.request.urlopen("https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670522,151.1957362&radius=500&type=restaurant&keyword=cruise&key=AIzaSyC0AuanxSq5DMmcnojnInlFRzqz0KF5HZI") as url:
        data = json.loads(url.read().decode())
        print(data)
        bot.send_message(message.chat.id, data)
    #https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=/// lng ///,/// lat ///&radius=/// rad ///&type=restaurant&keyword=cruise&key=AIzaSyC0AuanxSq5DMmcnojnInlFRzqz0KF5HZI

#bot.polling(none_stop=True, interval=0)
