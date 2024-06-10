import telebot
from telebot import types

from config import bot_token

from access import get_feedback_access_id

import time


# create telegram bot:
bot = telebot.TeleBot(bot_token)

# feedback dict:
feedback = {}


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    write_comment_button = types.KeyboardButton("Оставить отзыв")
    see_comment_button = types.KeyboardButton("Смотреть комментарии")
    # check user_id for view comments access:
    if message.from_user.id in get_feedback_access_id():
        markup.add(write_comment_button, see_comment_button)
    else:
        markup.add(write_comment_button)

    bot.send_message(message.chat.id, "Здесь вы можете предложить свои идеи по улучшению проекта, \n"
                                      "а также поставить оценку нашему проекту", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Оставить отзыв')
def write_comment(message):
    bot.send_message(message.chat.id, "Мы будем рады каждому оставленному отзыву")
    bot.register_next_step_handler(message, save_comment)


def save_comment(message):
    user_id = message.chat.id
    username = message.from_user.username

    feedback[user_id] = [username, message.text]

    bot.send_message(user_id, "Благодарим за оставленный отзыв")


@bot.message_handler(func=lambda message: message.text == 'Смотреть комментарии')
def view_comments(message):
    if len(feedback) == 0:
        bot.send_message(message.chat.id,"Пока нет комментариев...")
    else:
        comments_list = list(feedback.values())
        for comment in comments_list:
            time.sleep(1)
            bot.send_message(
                message.chat.id,
                f"*Пользователь:* {comment[0]}\n"
                f"*Комментарий:* {comment[1]}",
                parse_mode='Markdown'
            )


bot.polling(none_stop=True)
