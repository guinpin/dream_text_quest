import telebot
import os
from config import *
import keyboards as kb
from random import choice
from voice_converter import WitSpeechConvereter



bot = telebot.TeleBot(API_TOKEN)
controller = {}

INVALID_CHOICE = "Введите, пожалуйста, другой вариант - одно число из списка вариантов выше."
ERROR_TEXT = 'Не удалось распознать ваше голосовое сообщение. Попробуйте, пожалуйста, еще раз. Или напечатайте.'
VOICES_WAITING_STICKERS = [
    "CAACAgIAAxkBAAEBbupffp7NNGVTWh3piYyWiytPoZ4x0QACIwADKA9qFCdRJeeMIKQGGwQ",
    "CAACAgIAAxkBAAEBbuxffp7T-GwO2MMqgPmD4bR2R3TAIgAC9wYAAkb7rARWm6hbD5l2HRsE",
    "CAACAgIAAxkBAAEBbvBffp8qBnqe45QC9FpxU-VvVEpCOQACIgADr8ZRGtYR9zsFvVVnGwQ",
    "CAACAgIAAxkBAAEBbu5ffp8m-kFBrjurQXpC9aDAAAF1KZEAAtAIAAIYQu4Ihc4beyBycaobBA"
]

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.from_user.id,
                     """               
                     Вы сладенько укрылись одеялом, закрыли глаза и провалились в сон. Тут же перед вами возникла приборная панель с шестью кнопками. 
                     Каждая подписана. На какую вы нажмете?
                     """,  reply_markup=kb.main_kb)
    user_id = message.from_user.id
    controller[user_id] = 'start'

@bot.message_handler(content_types=['voice'])
def start_message(message):
    bot.send_message(message.from_user.id, "Подождите, пожалуйста. Пытаюсь понять, что вы сказали...")
    bot.send_sticker(message.from_user.id, choice(VOICES_WAITING_STICKERS))
    voice_converter = WitSpeechConvereter.get_instance()
    file_info = bot.get_file(message.voice.file_id)
    audio_filename = os.path.join(PATH_TO_VOICE_MESSAGES, '{}.ogg'.format(message.voice.file_id))
    downloaded_file = bot.download_file(file_info.file_path)
    with open(audio_filename, 'wb') as new_file:
        new_file.write(downloaded_file)
    try:
        converted_voice = voice_converter.to_text(audio_filename)
        bot.send_message(message.from_user.id, converted_voice)
    except ValueError:
        bot.send_message(message.from_user.id, ERROR_TEXT)


@bot.message_handler(content_types=['text'])
def start(message):
    user_id = message.from_user.id
    user_choice = message.text
    user_state = controller.get(user_id, 'start') # Если вдруг такой user_id не сохранен, то считаем, что статус = start
    #answer = 'none'
    if user_state == 'start':
        answer = start_handler(user_id, user_choice)
    if user_state == 'teacher':
        answer = teacher_handler(user_id, user_choice)
    bot.send_message(message.from_user.id, answer[0], reply_markup=answer[1])


def start_handler(user_id, user_choice):
    if user_choice == "Ваше домашнее животное":
        pass
    if user_choice == "Вы на 20 лет старше":
        pass
    if user_choice == "Полная противоположность вас":
        pass
    if user_choice == "Известная личность":
        pass    
    if user_choice == "Самый счастливый человек на Земле":
        pass
    if user_choice == "Ваш преподаватель по проектному программированию":
        controller[user_id] = 'teacher'
        return ["Вы открываете глаза. Звенит будильник. Перед вами ноутбук с Zoom. Что вы сделаете?", kb.teacher_kb]
    return [INVALID_CHOICE, None]


def teacher_handler(user_id, user_choice):
    if user_choice == "Выключите будильник и продолжите спать":
        controller[user_id] = 'start'
        return ["Перед вами опять возникла приборная панель с шестью кнопками. На какую вы нажмете в этот раз? Введите одно число.", kb.main_kb]
    if user_choice == "Войдете в Zoom и начнете урок":
        pass
    return [INVALID_CHOICE, None]


bot.polling()
