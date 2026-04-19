import os
import telebot
from telebot import types


bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))

IMG_VYPUSKNIKI = "vypuskniki_profili_deyatelnosti.jpg"
IMG_SITE_OP = "site_op.jpg"
IMG_INFORMAL = "not_official_resources.jpg"

def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Общее описание программы «Филология»")
    markup.add("Официальный сайт и контакты")
    markup.add("Онлайн-ресурсы 💻")
    return markup

def submenu_general():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Будущие профессии🎓", "Ключевые дисциплины", "Баллы ЕГЭ📊", "В главное меню")
    return markup

def submenu_contacts():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Сайт ОП", "Контакты руководителя", "В главное меню")
    return markup

def submenu_online():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Социальные сети", "Неофициальные сообщества", "В главное меню")
    return markup


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "Добро пожаловать! Выберите пункт меню:",
        reply_markup=main_menu()
    )


@bot.message_handler(content_types=['text'])
def func(message):
    text = message.text

    if text == "Общее описание программы «Филология»":
        bot.send_message(message.chat.id, "Общее описание программы:", reply_markup=submenu_general())

    elif text == "Официальный сайт и контакты":
        bot.send_message(message.chat.id, "Официальный сайт и контакты:", reply_markup=submenu_contacts())

    elif text == "Онлайн-ресурсы 💻":
        bot.send_message(message.chat.id, "Онлайн-ресурсы:", reply_markup=submenu_online())

    elif text == "Будущие профессии🎓":
        bot.send_photo(message.chat.id, open(IMG_VYPUSKNIKI, "rb"))
        bot.send_message(message.chat.id, graduates_who)

    elif text == "Ключевые дисциплины":
        bot.send_message(message.chat.id, key_disciplines)

    elif text == "Баллы ЕГЭ📊":
        bot.send_message(message.chat.id, ege_scores)

    elif text == "Сайт ОП":
        bot.send_photo(message.chat.id, open(IMG_SITE_OP, "rb"))
        bot.send_message(message.chat.id, site_op)

    elif text == "Контакты руководителя":
        bot.send_message(message.chat.id, head_contacts)

    elif text == "Социальные сети":
        bot.send_message(message.chat.id, socials)

    elif text == "Неофициальные сообщества":
        bot.send_photo(message.chat.id, open(IMG_INFORMAL, "rb"))
        bot.send_message(message.chat.id, informal)

    elif text == "В главное меню":
        bot.send_message(message.chat.id, "Вы вернулись в главное меню.", reply_markup=main_menu())

    else:
        bot.send_message(message.chat.id, "Команда не распознана. Выберите кнопку.")


# 📌 данные
graduates_who = (
    "ОП готовит преподавателей, историков, музейных работников и филологов..."
)

key_disciplines = (
    "Основы филологии\nЯзыкознание\nИстория языка\nКультура речи\nТеория перевода"
)

ege_scores = (
    "Литература – 40\nРусский язык – 40\nИстория – 40\nОбществознание – 45"
)

site_op = "https://programs.edu.urfu.ru/ru/10145/"

head_contacts = (
    "Меньщикова Анна Манасовна\n+7 (343) 3899417\nanna.menschikova@urfu.ru"
)

socials = (
    "VK: https://vk.com/filfak_urfu\nTelegram: https://t.me/philology_urfu"
)

informal = (
    "Цитаты: https://t.me/citaty_filfak"
)


bot.infinity_polling()
