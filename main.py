import telebot
import os

bot = telebot.TeleBot("6386017395:AAF_haqXPtHwqPmTena8AcL-YhocS03_zNI")


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message,
                 "Добро пожаловать в чат с Кинет-терапевтом! Я - ваш персональный Кинет-терапевт, готовый помочь вам в "
                 "вопросах физического здоровья и восстановления. Вместе мы сможем разработать индивидуальные планы "
                 "лечения и реабилитации, основанные на вашей уникальной ситуации. Я обладаю знаниями и опытом в "
                 "области физиотерапии, упражнений и методов восстановления. Будь то спортивная травма, хроническая "
                 "боль или просто желание улучшить свою физическую форму, я здесь, чтобы помочь вам достичь ваших "
                 "целей.")
    bot.reply_to(message, "Для начала введите ваше полное имя и фамилию")
    bot.register_next_step_handler(message, create_folder)


def create_folder(message):
    user_name = message.text
    user_folder = os.path.join("users_data", user_name)
    if not os.path.exists(user_folder):
        os.makedirs(user_folder)
    bot.reply_to(message, f"Папка создана для пользователя {user_name}")
    bot.reply_to(message, "Какова ваша медицинская и физическая история?")
    bot.register_next_step_handler(message, save_history, user_folder)


def save_history(message, user_folder):
    history = message.text
    bot.reply_to(message, "Какие симптомы или проблемы вы испытываете?")
    bot.register_next_step_handler(message, save_symptoms, user_folder, history)


def save_symptoms(message, user_folder, history):
    symptoms = message.text
    bot.reply_to(message, "Когда и как начались ваши симптомы или проблемы?")
    bot.register_next_step_handler(message, save_onset, user_folder, history, symptoms)


def save_onset(message, user_folder, history, symptoms):
    onset = message.text
    bot.reply_to(message, "Какие действия или движения усиливают или облегчают ваши симптомы?")
    bot.register_next_step_handler(message, save_actions, user_folder, history, symptoms, onset)


def save_actions(message, user_folder, history, symptoms, onset):
    actions = message.text
    bot.reply_to(message, "Были ли у вас какие-либо травмы или операции, связанные с вашими текущими проблемами?")
    bot.register_next_step_handler(message, save_injuries, user_folder, history, symptoms, onset, actions)


def save_injuries(message, user_folder, history, symptoms, onset, actions):
    injuries = message.text
    bot.reply_to(message, "Какую физическую активность или спорт вы обычно занимаетесь?")
    bot.register_next_step_handler(message, save_activity, user_folder, history, symptoms, onset, actions, injuries)


def save_activity(message, user_folder, history, symptoms, onset, actions, injuries):
    activity = message.text
    bot.reply_to(message,
                 "Есть ли у вас какие-либо ограничения или аллергии на физическую активность или определенные "
                 "упражнения?")
    bot.register_next_step_handler(message, save_restrictions, user_folder, history, symptoms, onset, actions, injuries,
                                   activity)


def save_restrictions(message, user_folder, history, symptoms, onset, actions, injuries, activity):
    restrictions = message.text
    bot.reply_to(message, "Какие цели вы хотели бы достичь через кинетотерапию?")
    bot.register_next_step_handler(message, save_goals, user_folder, history, symptoms, onset, actions, injuries,
                                   activity, restrictions)


def save_goals(message, user_folder, history, symptoms, onset, actions, injuries, activity, restrictions):
    goals = message.text
    bot.reply_to(message, "Каков ваш образ жизни и уровень физической активности?")
    bot.register_next_step_handler(message, save_lifestyle, user_folder, history, symptoms, onset, actions, injuries,
                                   activity, goals, restrictions)


def save_lifestyle(message, user_folder, history, symptoms, onset, actions, injuries, activity, goals, restrictions, ):
    lifestyle = message.text
    bot.reply_to(message, "Какие методы лечения или реабилитации вы уже пробовали?")
    bot.register_next_step_handler(message, save_treatments, user_folder, history, symptoms, onset, actions, injuries,
                                   activity, goals, restrictions, lifestyle)


def save_treatments(message, user_folder, history, symptoms, onset, actions, injuries, activity, goals, restrictions,
                    lifestyle):
    treatments = message.text
    bot.reply_to(message, "Введите ваш номер телефона:")
    bot.register_next_step_handler(message, save_phone, user_folder, history, symptoms, onset, actions, injuries,
                                   activity, goals, treatments, restrictions, lifestyle)


def save_phone(message, user_folder, history, symptoms, onset, actions, injuries, activity, goals, treatments,
               restrictions, lifestyle):
    phone = message.text
    file_path = os.path.join(user_folder, "history.txt")
    with open(file_path, "w") as file:
        file.write(
            f"Медицинская и физическая история:\n{history}\n\nСимптомы или проблемы:\n{symptoms}\n\nНачало симптомов "
            f"или проблем:\n{onset}\n\nДействия или движения, усиливающие или облегчающие симптомы:\n"
            f"{actions}\n\nТравмы или операции, связанные с текущими проблемами:\n{injuries}\n\nФизическая активность "
            f"или спорт, которым вы обычно занимаетесь:\n{activity}\n\nОграничения или аллергии на физическую "
            f"активность или определенные упражнения:\n{restrictions}\n\nЦели через кинетотерапию:\n{goals}\n\nОбраз "
            f"жизни и уровень физической активности:\n{lifestyle}\n\nМетоды лечения или реабилитации, пробованные "
            f"ранее:\n{treatments}\n\nНомер телефона:\n{phone}")

    bot.reply_to(message, "Спасибо за предоставленную информацию, мы скоро с вами свяжемся.")


bot.polling()
