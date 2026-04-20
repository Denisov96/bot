import os
import telebot
from telebot import types


TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN не найден!")

bot = telebot.TeleBot(TOKEN)

# file_id (твои картинки)
IMG1 = "AgACAgIAAxkBAAIBWmnlG25tTRdXbB4OO51r4r3aOBCsAAJfEWsbPxAxSw5a4bsK727sAQADAgADeQADOwQ"
IMG2 = "AgACAgIAAxkBAAIBXmnlHXi-lVsmVgpGudxbske-aMFIAAJ7EWsbPxAxS9zIJTc81pEwAQADAgADeQADOwQ"
IMG3 = "AgACAgIAAxkBAAIBX2nlHYhkkHYQadjCWAIBDOcYoZHuAAJ8EWsbPxAxS9u4HyG--yjmAQADAgADeQADOwQ"



graduates_who = (
    "ОП готовит преподавателей, историков, музейных работников и филологов "
    "широкого профиля – специалистов по русской и мировой литературе."
)

key_disciplines = (
    "Основы филологии\n"
    "Языкознание\n"
    "История языка\n"
    "Культура речи\n"
    "Теория перевода"
)

ege_scores = (
    "Минимальные баллы 2026:\n"
    "Литература – 40\n"
    "Русский – 40\n"
    "Иностранный – 40\n"
    "История – 40\n"
    "Обществознание – 45"
)

site_op = "https://programs.edu.urfu.ru/ru/10145/"

head_contacts = (
    "Меньщикова Анна Манасовна\n"
    "+7 (343) 3899417\n"
    "anna.menschikova@urfu.ru"
)

socials = (
    "VK: https://vk.com/filfak_urfu\n"
    "TG: https://t.me/philology_urfu"
)

informal = (
    "https://t.me/citaty_filfak\n"
    "https://vk.com/feel_fuck_quotes"
)



def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Общее описание программы «Филология»")
    markup.add("Официальный сайт и контакты")
    markup.add("Онлайн-ресурсы 💻")
    return markup

def submenu_general():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Будущие профессии🎓", "Ключевые дисциплины")
    markup.add("Баллы ЕГЭ📊", "В главное меню")
    return markup

def submenu_contacts():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Сайт ОП", "Контакты руководителя")
    markup.add("В главное меню")
    return markup

def submenu_online():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Социальные сети", "Неофициальные сообщества")
    markup.add("В главное меню")
    return markup



@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "Добро пожаловать! Выберите пункт:",
        reply_markup=main_menu()
    )

@bot.message_handler(content_types=['text'])
def handler(message):
    text = message.text.strip()

    
    if text == "Общее описание программы «Филология»":
        bot.send_message(message.chat.id, "Описание:", reply_markup=submenu_general())

    elif text == "Официальный сайт и контакты":
        bot.send_message(message.chat.id, "Контакты:", reply_markup=submenu_contacts())

    elif text == "Онлайн-ресурсы 💻":
        bot.send_message(message.chat.id, "Ресурсы:", reply_markup=submenu_online())

   
    elif text == "Будущие профессии🎓":
        try:
            bot.send_photo(message.chat.id, IMG1)
        except:
            bot.send_message(message.chat.id, "Ошибка картинки")
        bot.send_message(message.chat.id, graduates_who, reply_markup=submenu_general())

    elif text == "Ключевые дисциплины":
        bot.send_message(message.chat.id, key_disciplines, reply_markup=submenu_general())

    elif text == "Баллы ЕГЭ📊":
        bot.send_message(message.chat.id, ege_scores, reply_markup=submenu_general())

    elif text == "Сайт ОП":
        try:
            bot.send_photo(message.chat.id, IMG2)
        except:
            pass
        bot.send_message(message.chat.id, site_op, reply_markup=submenu_contacts())

    elif text == "Контакты руководителя":
        bot.send_message(message.chat.id, head_contacts, reply_markup=submenu_contacts())

    elif text == "Социальные сети":
        bot.send_message(message.chat.id, socials, reply_markup=submenu_online())

    elif text == "Неофициальные сообщества":
        try:
            bot.send_photo(message.chat.id, IMG3)
        except:
            pass
        bot.send_message(message.chat.id, informal, reply_markup=submenu_online())

    elif text == "В главное меню":
        bot.send_message(message.chat.id, "Главное меню", reply_markup=main_menu())

    else:
        bot.send_message(message.chat.id, "Выберите кнопку из меню")


bot.infinity_polling()
