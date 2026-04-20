import os
import time
import telebot
from telebot import types

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN не найден!")

bot = telebot.TeleBot(TOKEN, parse_mode="HTML")

# --------- КАРТИНКИ (GitHub RAW) ---------
GITHUB_RAW = "https://raw.githubusercontent.com/Denisov96/bot/main/"

IMG_PROF = GITHUB_RAW + "vypuskniki_profili_deyatelnosti.jpg"
IMG_SITE = GITHUB_RAW + "site_op.jpg"
IMG_COMM = GITHUB_RAW + "not_official_resources.jpg"


# --------- ТЕКСТЫ ---------
graduates_who = (
    "🎓 <b>Кем ты станешь?</b>\n\n"
    "Преподаватель 📚\n"
    "Филолог 📝\n"
    "Редактор ✍️\n"
    "Переводчик 🌍\n"
    "Научный сотрудник 🔬\n\n"
    "Ты сможешь работать в образовании, медиа, культуре и науке."
)

key_disciplines = (
    "📚 <b>Ключевые дисциплины:</b>\n\n"
    "• Основы филологии\n"
    "• Языкознание\n"
    "• История языка\n"
    "• Культура речи и стилистика\n"
    "• Теория перевода\n"
    "• Литературоведение"
)

ege_scores = (
    "📊 <b>Баллы ЕГЭ (2026):</b>\n\n"
    "Русский — 40\n"
    "Литература — 40\n\n"
    "По выбору:\n"
    "Иностранный — 40\n"
    "История — 40\n"
    "Обществознание — 45\n\n"
    "🎯 Бюджетных мест: 30"
)

site_op = "🌐 https://programs.edu.urfu.ru/ru/10145/"

head_contacts = (
    "👩‍🏫 <b>Руководитель:</b>\n\n"
    "Меньщикова Анна Манасовна\n"
    "📍 Ауд. 303, пр. Ленина 51\n"
    "📞 +7 (343) 3899417\n"
    "✉️ anna.menschikova@urfu.ru"
)

socials = (
    "🌐 <b>Соцсети:</b>\n\n"
    "VK: https://vk.com/filfak_urfu\n"
    "TG: https://t.me/philology_urfu\n\n"
    "Абитуриентам:\n"
    "https://vk.com/abiturient_filfaka"
)

informal = (
    "💬 <b>Неофициальные:</b>\n\n"
    "t.me/citaty_filfak\n"
    "vk.com/feel_fuck_quotes\n"
    "t.me/litsafilfakaurfu"
)


# --------- МЕНЮ ---------
def main_menu():
    m = types.ReplyKeyboardMarkup(resize_keyboard=True)
    m.add("📘 О программе")
    m.add("📞 Контакты")
    m.add("💻 Ресурсы")
    return m


def submenu_general():
    m = types.ReplyKeyboardMarkup(resize_keyboard=True)
    m.add("🎓 Профессии", "📚 Дисциплины")
    m.add("📊 ЕГЭ", "🔙 Назад")
    return m


def submenu_contacts():
    m = types.ReplyKeyboardMarkup(resize_keyboard=True)
    m.add("🌐 Сайт", "👩‍🏫 Руководитель")
    m.add("🔙 Назад")
    return m


def submenu_online():
    m = types.ReplyKeyboardMarkup(resize_keyboard=True)
    m.add("🌐 Соцсети", "💬 Комьюнити")
    m.add("🔙 Назад")
    return m


# --------- START ---------
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "👋 <b>Хочешь поступить на филологию в УрФУ?</b>\n\n"
        "Я помогу тебе разобраться:\n"
        "• что изучают 📚\n"
        "• кем ты станешь 🎓\n"
        "• какие баллы нужны 📊\n\n"
        "👇 Просто выбери пункт:",
        reply_markup=main_menu()
    )


# --------- ЛОГИКА ---------
@bot.message_handler(content_types=['text'])
def handler(message):
    text = message.text.strip()

    print("USER:", text)

    if text == "📘 О программе":
        bot.send_message(message.chat.id, "Выбери:", reply_markup=submenu_general())

    elif text == "📞 Контакты":
        bot.send_message(message.chat.id, "Контакты:", reply_markup=submenu_contacts())

    elif text == "💻 Ресурсы":
        bot.send_message(message.chat.id, "Ресурсы:", reply_markup=submenu_online())

    elif text == "🎓 Профессии":
        bot.send_photo(message.chat.id, IMG_PROF, caption=graduates_who)

    elif text == "📚 Дисциплины":
        bot.send_message(message.chat.id, key_disciplines)

    elif text == "📊 ЕГЭ":
        bot.send_message(message.chat.id, ege_scores)

    elif text == "🌐 Сайт":
        bot.send_photo(message.chat.id, IMG_SITE, caption=site_op)

    elif text == "👩‍🏫 Руководитель":
        bot.send_message(message.chat.id, head_contacts)

    elif text == "🌐 Соцсети":
        bot.send_message(message.chat.id, socials)

    elif text == "💬 Комьюнити":
        bot.send_photo(message.chat.id, IMG_COMM, caption=informal)

    elif text == "🔙 Назад":
        bot.send_message(message.chat.id, "Главное меню", reply_markup=main_menu())

    else:
        bot.send_message(message.chat.id, "Используй кнопки 👇")


# --------- ЗАПУСК ---------
if __name__ == "__main__":
    print("BOT START")

    try:
        bot.remove_webhook()
        time.sleep(1)
    except:
        pass

    bot.infinity_polling(skip_pending=True)
