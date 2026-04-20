import os
import telebot
from telebot import types

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN не найден в переменных окружения!")

bot = telebot.TeleBot(TOKEN, parse_mode="HTML")


# --------- КНОПКИ ---------
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


# --------- ДАННЫЕ ---------
graduates_who = "Филология: преподаватели, исследователи, редакторы, переводчики."
key_disciplines = "Языкознание\nЛитература\nСтилистика\nПеревод"
ege_scores = "Русский 40\nЛитература 40\nИстория 40\nОбществознание 45"
site_op = "https://programs.edu.urfu.ru/ru/10145/"
head_contacts = "Анна Меньщикова\n+7 (343) 3899417\nanna@urfu.ru"
socials = "VK: vk.com/filfak_urfu\nTG: t.me/philology_urfu"
informal = "t.me/citaty_filfak\nvk.com/feel_fuck_quotes"


# --------- START ---------
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "Добро пожаловать 👋 Выберите пункт:",
        reply_markup=main_menu()
    )


# --------- ОБРАБОТКА ---------
@bot.message_handler(content_types=['text'])
def handler(message):
    text = message.text.strip()

    print("USER:", text)  # 👈 важно для отладки

    if text == "Общее описание программы «Филология»":
        bot.send_message(message.chat.id, "📘 О программе", reply_markup=submenu_general())

    elif text == "Официальный сайт и контакты":
        bot.send_message(message.chat.id, "📞 Контакты", reply_markup=submenu_contacts())

    elif text == "Онлайн-ресурсы 💻":
        bot.send_message(message.chat.id, "🌐 Ресурсы", reply_markup=submenu_online())

    elif text == "Будущие профессии🎓":
        bot.send_message(message.chat.id, graduates_who)

    elif text == "Ключевые дисциплины":
        bot.send_message(message.chat.id, key_disciplines)

    elif text == "Баллы ЕГЭ📊":
        bot.send_message(message.chat.id, ege_scores)

    elif text == "Сайт ОП":
        bot.send_message(message.chat.id, site_op)

    elif text == "Контакты руководителя":
        bot.send_message(message.chat.id, head_contacts)

    elif text == "Социальные сети":
        bot.send_message(message.chat.id, socials)

    elif text == "Неофициальные сообщества":
        bot.send_message(message.chat.id, informal)

    elif text == "В главное меню":
        bot.send_message(message.chat.id, "Главное меню", reply_markup=main_menu())

    else:
        bot.send_message(message.chat.id, "Нажми кнопку из меню")


# --------- ЗАПУСК ---------
bot.infinity_polling(skip_pending=True)
