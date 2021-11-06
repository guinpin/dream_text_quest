if __name__ == '__main__':

    import telebot
    from config import API_TOKEN

    bot = telebot.TeleBot(API_TOKEN)
    controller = {}

    INVALID_CHOICE = "Введите, пожалуйста, другой вариант - одно число из списка вариантов выше."


    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.from_user.id,
                         """               
                         Вы сладенько укрылись одеялом, закрыли глаза и провалились в сон. 
                         \U000023F9 Тут же перед вами возникла приборная панель с четырьмя кнопками.
                         \U000025B6 Каждая подписана. На какую вы нажмете? Введите одно число.
                         [1] Кнопка "Ваше домашнее животное" 
                         [2] Кнопка "Вы на 20 лет старше"
                         [3] Кнопка "Полная противоположность вас"
                         [4] Кнопка "Известная личность"
                         [5] Кнопка "Самый счастливый человек на Земле"
                         [6] Кнопка "Ваш преподаватель по проектному программированию"
                         """)
        user_id = message.from_user.id
        controller[user_id] = 'start'


    @bot.message_handler(content_types=['text'])
    def start(message):
        user_id = message.from_user.id
        user_choice = message.text
        user_state = controller.get(user_id,
                                    'start')  # Если вдруг такой user_id не сохранен, то считаем, что статус = start
        # answer = 'none'
        if user_state == 'start':
            answer = start_handler(user_id, user_choice)
        if user_state == 'teacher':
            answer = teacher_handler(user_id, user_choice)
        if user_state == 'pet':
            answer = pet_handler(user_id, user_choice)
        bot.send_message(message.from_user.id, answer)


    def start_handler(user_id, user_choice):
        if user_choice == "1":
            controller[user_id] = 'pet'
            return """
                Вы слышите возню Олафа, вашего снежно-белого пса. Что вы сделаете?
                [1] Улыбнетесь и снова уснете
                [2] Встанете с кровати и пройдете на кухню
                """
        if user_choice == "2":
            pass
        if user_choice == "3":
            pass
        if user_choice == "4":
            pass
        if user_choice == "5":
            pass
        if user_choice == "6":
            controller[user_id] = 'teacher'
            return """
                Вы открываете глаза. Звенит будильник. Перед вами ноутбук с Zoom. Что вы сделаете?
                [1] Выключите будильник и продолжите спать
                [2] Войдете в Zoom и начнете урок
                """
        return INVALID_CHOICE


    def teacher_handler(user_id, user_choice):
        if user_choice == "1":
            controller[user_id] = 'start'
            return """
                Перед вами опять возникла приборная панель с четырьмя кнопками.
                На какую вы нажмете в этот раз? Введите одно число.
                [1] Кнопка "Ваше домашнее животное" 
                [2] Кнопка "Вы на 20 лет старше"
                [3] Кнопка "Полная противоположность вас"
                [4] Кнопка "Известная личность"
                [5] Кнопка "Самый счастливый человек на Земле"
                [6] Кнопка "Ваш преподаватель по проектному программированию"
                """
        if user_choice == "2":
            pass
        return INVALID_CHOICE

    def pet_handler(user_id, user_choice):
        if user_choice == "1":
            controller[user_id] = 'start'
            return """
                Перед вами опять возникла приборная панель с четырьмя кнопками.
                На какую вы нажмете в этот раз? Введите одно число.
                [1] Кнопка "Ваше домашнее животное" 
                [2] Кнопка "Вы на 20 лет старше"
                [3] Кнопка "Полная противоположность вас"
                [4] Кнопка "Известная личность"
                [5] Кнопка "Самый счастливый человек на Земле"
                [6] Кнопка "Ваш преподаватель по проектному программированию"
                """
        if user_choice == "2":
            return """
                Вы на кухне и пока кофемашина создает святую жидкость, 
                вы раздумываете, что же хотите сделать.
                [1] Позвать Олафа
                [2] Насыпать корм в миску"""

        return INVALID_CHOICE
    bot.polling()
