import telebot
import os
import pandas as pd
from datetime import datetime

bot = telebot.TeleBot("6386017395:AAF_haqXPtHwqPmTena8AcL-YhocS03_zNI")

# Определите путь к общему файлу данных
data_file = "user_data/data.xlsx"


@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
    item1 = telebot.types.KeyboardButton('Русский')
    item2 = telebot.types.KeyboardButton('Română')
    markup.add(item1, item2)

    bot.send_message(message.chat.id, 'Выберите язык / Alegeți limba:', reply_markup=markup)
    bot.register_next_step_handler(message, handle_language, )


def handle_language(message):
    language = message.text

    if language == 'Русский':
        bot.send_message(message.chat.id, 'Вы выбрали русский язык.\n')
        bot.reply_to(message,
                     "Добро пожаловать в чат с Кинет-терапевтом! Я - ваш персональный Кинет-терапевт, готовый помочь "
                     "вам в \n"
                     "вопросах физического здоровья и восстановления. Вместе мы сможем разработать индивидуальные планы\n"
                     "лечения и реабилитации, основанные на вашей уникальной ситуации. Я обладаю знаниями и опытом в \n"
                     "области физиотерапии, упражнений и методов восстановления. Будь то спортивная травма, хроническая\n"
                     "боль или просто желание улучшить свою физическую форму, я здесь, чтобы помочь вам достичь ваших \n"
                     "целей.")
        bot.send_message(message.chat.id, 'Введите ваше полное имя и фамилию:',
                         reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, create_folder_ru, language)
    elif language == 'Română':
        bot.send_message(message.chat.id, 'Ați selectat limba română.')
        bot.reply_to(message,
                     'Bine ați venit să discutați cu un terapeut Kinet! Sunt Kinetterapeutul dvs. personal, '
                     'gata să vă ajut cu\n'
                     'probleme de sănătate fizică și de recuperare. Împreună putem dezvolta planuri individuale\n'
                     'tratament și reabilitare în funcție de situația dvs. unică. Am cunoștințele și experiența în\n '
                     'Domenii de fizioterapie, exerciții fizice și tehnici de recuperare. Fie că este vorba despre o '
                     'accidentare sportivă, cronică\n'
                     'durere sau doar dorința de a-ți îmbunătăți forma fizică, sunt aici să te ajut să-ți atingi\n'
                     'goluri')
        bot.send_message(message.chat.id, 'Introduceți numele și prenumele complet:\n',
                         reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, create_folder_ro, language)


def create_folder_ru(message, language):
    user_name = message.text
    if user_name == "kinetoadmin234":
        chat_id = message.chat.id
        file_path = r"user_data/data.xlsx"  # Replace with the actual file path

        # Check if the file exists
        if os.path.exists(file_path):
            with open(file_path, 'rb') as file:
                bot.send_document(chat_id, file)
        else:
            bot.reply_to(message, "File not found.\n")
    else:
        bot.reply_to(message, "Какова ваша медицинская и физическая история?\n")
        bot.register_next_step_handler(message, save_history_ru, user_name, language)


def create_folder_ro(message, language):
    user_name = message.text

    bot.send_message(message.chat.id, 'Care este istoricul dumneavoastră medical și fizic?\n')
    bot.register_next_step_handler(message, save_history_ro, user_name, language)


def save_history_ru(message, user_name, language):
    history = message.text
    bot.send_message(message.chat.id, 'Какие симптомы или проблемы вы испытываете?\n')
    bot.register_next_step_handler(message, save_symptoms_ru, user_name, history, language)


def save_history_ro(message, user_name, language):
    history = message.text
    bot.send_message(message.chat.id, 'Ce simptome sau probleme te confrunți?\n')
    bot.register_next_step_handler(message, save_symptoms_ro, user_name, history, language)


def save_symptoms_ru(message, user_name, history, language):
    symptoms = message.text
    bot.send_message(message.chat.id, 'Когда и как начались ваши симптомы или проблемы?\n')
    bot.register_next_step_handler(message, save_onset_ru, user_name, history, symptoms, language)


def save_symptoms_ro(message, user_name, history, language):
    symptoms = message.text
    bot.send_message(message.chat.id, 'Când și cum au început simptomele sau problemele tale?\n')
    bot.register_next_step_handler(message, save_onset_ro, user_name, history, symptoms, language)


def save_onset_ru(message, user_name, history, symptoms, language):
    onset = message.text
    bot.send_message(message.chat.id, 'Какие действия или движения усиливают или облегчают ваши симптомы?\n')
    bot.register_next_step_handler(message, save_actions_ru, user_name, history, onset, symptoms, language)


def save_onset_ro(message, user_name, history, symptoms, language):
    onset = message.text
    bot.send_message(message.chat.id, 'Ce activități sau mișcări vă agravează sau vă ameliorează simptomele?\n')
    bot.register_next_step_handler(message, save_actions_ro, user_name, history, onset, symptoms, language)


def save_actions_ru(message, user_name, history, onset, symptoms, language):
    actions = message.text
    bot.send_message(message.chat.id,
                     'Были ли у вас какие-либо травмы или операции, связанные с вашими текущими проблемами?\n')
    bot.register_next_step_handler(message, save_injuries_ru, user_name, history, onset, actions, symptoms, language)


def save_actions_ro(message, user_name, history, onset, symptoms, language):
    actions = message.text
    bot.send_message(message.chat.id,
                     'Ați avut răni sau intervenții chirurgicale legate de problemele dvs. actuale?\n')
    bot.register_next_step_handler(message, save_injuries_ro, user_name, history, onset, actions, symptoms, language)


def save_injuries_ru(message, user_name, history, onset, actions, symptoms, language):
    injuries = message.text
    bot.send_message(message.chat.id, 'Какую физическую активность или спорт вы обычно занимаетесь?\n')
    bot.register_next_step_handler(message, save_activity_ru, user_name, history, onset, actions, injuries, symptoms,
                                   language)


def save_injuries_ro(message, user_name, history, onset, actions, symptoms, language):
    injuries = message.text
    bot.send_message(message.chat.id, 'Ce activitate fizică sau sport practicați de obicei?\n')
    bot.register_next_step_handler(message, save_activity_ro, user_name, history, onset, actions, injuries, symptoms,
                                   language)


def save_activity_ru(message, user_name, history, onset, actions, injuries, symptoms, language):
    activity = message.text
    bot.send_message(message.chat.id,
                     'Есть ли у вас какие-либо ограничения или аллергии на физическую активность или определенные '
                     'упражнения?\n')
    bot.register_next_step_handler(message, save_restrictions_ru, user_name, history, onset, actions, injuries,
                                   activity,
                                   symptoms, language)


def save_activity_ro(message, user_name, history, onset, actions, injuries, symptoms, language):
    activity = message.text
    bot.send_message(message.chat.id,
                     'Aveți restricții sau alergii la activitatea fizică sau anumite exerciții?\n')
    bot.register_next_step_handler(message, save_restrictions_ro, user_name, history, onset, actions, injuries,
                                   activity,
                                   symptoms, language)


def save_restrictions_ru(message, user_name, history, onset, actions, injuries, activity, symptoms, language):
    restrictions = message.text
    bot.send_message(message.chat.id, 'Какие цели вы хотели бы достичь через кинетотерапию?\n')
    bot.register_next_step_handler(message, save_goals_ru, user_name, history, onset, actions, injuries, activity,
                                   restrictions, symptoms, language)


def save_restrictions_ro(message, user_name, history, onset, actions, injuries, activity, symptoms, language):
    restrictions = message.text
    bot.send_message(message.chat.id, 'Ce obiective ați dori să atingeți prin kinetoterapie?\n')
    bot.register_next_step_handler(message, save_goals_ro, user_name, history, onset, actions, injuries, activity,
                                   restrictions, symptoms, language)


def save_goals_ru(message, user_name, history, onset, actions, injuries, activity, restrictions, symptoms, language):
    goals = message.text
    bot.send_message(message.chat.id, 'Каков ваш образ жизни и уровень физической активности?\n')
    bot.register_next_step_handler(message, save_lifestyle_ru, user_name, history, onset, actions, injuries, goals,
                                   activity, restrictions, symptoms, language)


def save_goals_ro(message, user_name, history, onset, actions, injuries, activity, restrictions, symptoms, language):
    goals = message.text
    bot.send_message(message.chat.id, 'Care este stilul tău de viață și nivelul tău de activitate fizică?\n')
    bot.register_next_step_handler(message, save_lifestyle_ro, user_name, history, onset, actions, injuries, goals,
                                   activity, restrictions, symptoms, language)


def save_lifestyle_ru(message, user_name, history, onset, actions, injuries, goals, activity, restrictions, symptoms,
                      language):
    lifestyle = message.text
    bot.send_message(message.chat.id, 'Какие методы лечения или реабилитации вы уже пробовали?\n')
    bot.register_next_step_handler(message, save_treatments_ru, user_name, history, onset, actions, injuries, goals,
                                   activity, restrictions, lifestyle, symptoms, language)


def save_lifestyle_ro(message, user_name, history, onset, actions, injuries, goals, activity, restrictions, symptoms,
                      language):
    lifestyle = message.text
    bot.send_message(message.chat.id, 'Ce tratamente sau metode de reabilitare ați încercat deja?\n')
    bot.register_next_step_handler(message, save_treatments_ro, user_name, history, onset, actions, injuries, goals,
                                   activity, restrictions, lifestyle, symptoms, language)


def save_treatments_ru(message, user_name, history, onset, actions, injuries, goals, activity, restrictions, lifestyle,
                       symptoms, language):
    treatments = message.text
    bot.send_message(message.chat.id, 'Введите ваш номер телефона:\n')
    bot.register_next_step_handler(message, save_phone, user_name, history, onset, actions, injuries, goals, treatments,
                                   activity, restrictions, lifestyle, symptoms, language)


def save_treatments_ro(message, user_name, history, onset, actions, injuries, goals, activity, restrictions, lifestyle,
                       symptoms, language):
    treatments = message.text
    bot.send_message(message.chat.id, 'Introdu numarul tau de telefon:\n')
    bot.register_next_step_handler(message, save_phone, user_name, history, onset, actions, injuries, goals, treatments,
                                   activity, restrictions, lifestyle, symptoms, language)


def save_phone(message, user_name, history, onset, actions, injuries, goals, treatments, activity, restrictions,
               lifestyle, symptoms, language):
    if language == 'Русский':
        bot.send_message(message.chat.id, "Спасибо! Ваша информация сохранена.\n")
        bot.send_message(message.chat.id, "Мы свяжемся с вами в ближайшее время для дальнейшей консультации.\n")
    elif language == 'Română':
        bot.send_message(message.chat.id, "Mulțumesc! Informațiile dvs. au fost salvate.\n")
        bot.send_message(message.chat.id, "Vă vom contacta în cel mai scurt timp pentru consultare.\n")

    current_date = datetime.now()
    date_string = current_date.strftime("%Y-%m-%d")
    phone = message.text
    name = message.from_user.first_name

    # Проверка доступности номера телефона
    if message.contact is not None:
        phone_number = message.contact.phone_number
    else:
        phone_number = None

    data = {
        "язык": [language],
        "Имя": [user_name],
        "Медицинская и физическая история": [history],
        "Симптомы или проблемы": [symptoms],
        "Начало симптомов или проблем": [onset],
        "Действия или движения, усиливающие или облегчающие симптомы": [actions],
        "Травмы или операции, связанные с текущими проблемами": [injuries],
        "Физическая активность или спорт, которым вы обычно занимаетесь": [activity],
        "Ограничения или аллергии на физическую активность или определенные упражнения": [restrictions],
        "Цели через кинетотерапию": [goals],
        "Образ жизни и уровень физической активности": [lifestyle],
        "Методы лечения или реабилитации, которые вы уже пробовали": [treatments],
        "Номер телефона": [phone],
        "Дата": [date_string],
        "Имя пользователя": [name],
        "Настоящий номер телефона": [phone_number]
    }

    df = pd.DataFrame(data)

    # Добавление данных пользователя в общий файл данных
    if os.path.exists(data_file):
        existing_data = pd.read_excel(data_file)
        updated_data = pd.concat([existing_data, df], ignore_index=True)
        updated_data.to_excel(data_file, index=False)
    else:
        df.to_excel(data_file, index=False)


bot.polling()
