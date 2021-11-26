from telebot import types

button_1 = types.KeyboardButton('Ваше домашнее животное')
button_2 = types.KeyboardButton('Вы на 20 лет старше')
button_3 = types.KeyboardButton('Полная противоположность вас')
button_4 = types.KeyboardButton('Известная личность')
button_5 = types.KeyboardButton('Самый счастливый человек на Земле')
button_6 = types.KeyboardButton('Ваш преподаватель по проектному программированию')

main_kb = types.ReplyKeyboardMarkup()
main_kb.add(button_1).add(button_2).add(button_3).add(button_4).add(button_5).add(button_6)

button_teacher_1 = types.KeyboardButton('Выключите будильник и продолжите спать')
button_teacher_2 = types.KeyboardButton('Войдете в Zoom и начнете урок')

teacher_kb = types.ReplyKeyboardMarkup()
teacher_kb.add(button_teacher_1).add(button_teacher_2)
