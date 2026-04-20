import os
import telebot
from telebot import types

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN не найден!")

bot = telebot.TeleBot(TOKEN)


# картинки (file_id)
IMG1 = "AgACAgIAAxkBAAIBWmnlG25tTRdXbB4OO51r4r3aOBCsAAJfEWsbPxAxSw5a4bsK727sAQADAgADeQADOwQ"
IMG2 = "AgACAgIAAxkBAAIBXmnlHXi-lVsmVgpGudxbske-aMFIAAJ7EWsbPxAxS9zIJTc81pEwAQADAgADeQADOwQ"
IMG3 = "AgACAgIAAxkBAAIBX2nlHYhkkHYQadjCWAIBDOcYoZHuAAJ8EWsbPxAxS9u4HyG--yjmAQADAgADeQADOwQ"


# тексты
graduates_who = "ОП готовит преподавателей, историков и филологов."
key_disciplines = "Основы филологии\nЯзыкознание\nИстория языка"
ege_scores = "Литература – 40\nРусский – 40\nИстория – 40"
site_op = "https://programs.edu.urfu.ru/ru/10145/"
head_contacts = "Меньщикова Анна Манасовна\n+7..."
socials = "VK: https://vk.com/filfak_urfu"
informal = "https://t.me/citaty_filfak"


# меню
def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("📚 Описание", "📞 Контакты", "💻 Ресурсы")
    return markup

def menu_general():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🎓 Профессии", "📖 Дисциплины")
    markup.add("📊 Баллы", "⬅️ Назад")
    return markup

def menu_contacts():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🌐 Сайт", "👤 Руководитель")
    markup.add("⬅️ Назад")
    return markup

def menu_online():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("📱 Соцсети", "👥 Сообщества")
    markup.add("⬅️ Назад")
    return markup


# старт
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Выбери пункт:", reply_markup=main_menu())


# обработка
@bot.message_handler(func=lambda m: True)
def handler(message):
    text = message.text

    print(">>", text)  # лог

    # главное меню
    if text == "📚 Описание":
        bot.send_message(message.chat.id, "Описание:", reply_markup=menu_general())

    elif text == "📞 Контакты":
        bot.send_message(message.chat.id, "Контакты:", reply_markup=menu_contacts())

    elif text == "💻 Ресурсы":
        bot.send_message(message.chat.id, "Ресурсы:", reply_markup=menu_online())

    # описание
    elif text == "🎓 Профессии":
        bot.send_photo(message.chat.id, IMG1)
        bot.send_message(message.chat.id, graduates_who)

    elif text == "📖 Дисциплины":
        bot.send_message(message.chat.id, key_disciplines)

    elif text == "📊 Баллы":
        bot.send_message(message.chat.id, ege_scores)

    # контакты
    elif text == "🌐 Сайт":
        bot.send_photo(message.chat.id, IMG2)
        bot.send_message(message.chat.id, site_op)

    elif text == "👤 Руководитель":
        bot.send_message(message.chat.id, head_contacts)

    # ресурсы
    elif text == "📱 Соцсети":
        bot.send_message(message.chat.id, socials)

    elif text == "👥 Сообщества":
        bot.send_photo(message.chat.id, IMG3)
        bot.send_message(message.chat.id, informal)

    # назад
    elif text == "⬅️ Назад":
        bot.send_message(message.chat.id, "Главное меню", reply_markup=main_menu())

    else:
        bot.send_message(message.chat.id, "Нажми кнопку 👇", reply_markup=main_menu())


print("Бот запущен...")
bot.infinity_polling()
