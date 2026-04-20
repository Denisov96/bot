import os
import time
import telebot
from telebot import types

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN не найден!")

bot = telebot.TeleBot(TOKEN, parse_mode="HTML")

# 🔥 картинки с GitHub
GITHUB_RAW = "https://raw.githubusercontent.com/Denisov96/bot/main/"



graduates_who = (
    "🎓 <b>Кем ты станешь после филологии?</b>\n\n"
    "ОП готовит:\n"
    "• преподавателей\n"
    "• исследователей\n"
    "• переводчиков\n"
    "• редакторов\n"
    "• специалистов по литературе\n\n"
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
    "📊 <b>ЕГЭ 2026:</b>\n\n"
    "Обязательные:\n"
    "• Русский язык — 40\n"
    "• Литература — 40\n\n"
    "По выбору:\n"
    "• Иностранный — 40\n"
    "• История — 40\n"
    "• Обществознание — 45\n\n"
    "🎯 Бюджет: 30 мест"
)

site_op = (
    "🌐 <b>Официальный сайт:</b>\n"
    "https://programs.edu.urfu.ru/ru/10145/"
)

head_contacts = (
    "👩‍🏫 <b>Руководитель:</b>\n\n"
    "Меньщикова Анна Манасовна\n\n"
    "📍 Аудитория 303, пр. Ленина, 51\n"
    "📞 +7 (343) 3899417\n"
    "✉ anna.menschikova@urfu.ru"
)

socials = (
    "🌐 <b>Социальные сети:</b>\n\n"
    "VK: https://vk.com/filfak_urfu\n"
    "TG: https://t.me/philology_urfu\n\n"
    "Абитуриентам:\n"
    "https://vk.com/abiturient_filfaka"
)

informal = (
    "💬 <b>Неофициальные сообщества:</b>\n\n"
    "https://t.me/citaty_filfak\n"
    "https://vk.com/feel_fuck_quotes\n"
    "https://t.me/litsafilfakaurfu"
)



def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("📘 Описание программы")
    markup.add("📞 Контакты")
    markup.add("🌐 Онлайн-ресурсы")
    return markup


def submenu_general():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🎓 Профессии", "📚 Дисциплины")
    markup.add("📊 ЕГЭ", "🔙 Назад")
    return markup


def submenu_contacts():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🌐 Сайт", "👩‍🏫 Руководитель")
    markup.add("🔙 Назад")
    return markup


def submenu_online():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("📱 Соцсети", "💬 Сообщества")
    markup.add("🔙 Назад")
    return markup



@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "👋 <b>Хочешь поступить на филологию в УрФУ?</b>\n\n"
        "Я помогу тебе разобраться 👇\n"
        "Жми кнопку и узнаешь всё про поступление, предметы и перспективы 🚀",
        reply_markup=main_menu()
    )



@bot.message_handler(content_types=['text'])
def handler(message):
    text = message.text.strip()

    print("USER:", text)

    try:

        
        if text == "📘 Описание программы":
            bot.send_message(message.chat.id, "Выбери раздел 👇", reply_markup=submenu_general())

        elif text == "📞 Контакты":
            bot.send_message(message.chat.id, "Контактная информация 👇", reply_markup=submenu_contacts())

        elif text == "🌐 Онлайн-ресурсы":
            bot.send_message(message.chat.id, "Полезные ресурсы 👇", reply_markup=submenu_online())

        
        elif text == "🎓 Профессии":
            bot.send_photo(
                message.chat.id,
                GITHUB_RAW + "vypuskniki_profili_deyatelnosti.jpg",
                caption=graduates_who
            )

        elif text == "📚 Дисциплины":
            bot.send_message(message.chat.id, key_disciplines)

        elif text == "📊 ЕГЭ":
            bot.send_message(message.chat.id, ege_scores)

       
        elif text == "🌐 Сайт":
            bot.send_photo(
                message.chat.id,
                GITHUB_RAW + "site_op.jpg",
                caption=site_op
            )

        elif text == "👩‍🏫 Руководитель":
            bot.send_message(message.chat.id, head_contacts)

       
        elif text == "📱 Соцсети":
            bot.send_message(message.chat.id, socials)

        elif text == "💬 Сообщества":
            bot.send_photo(
                message.chat.id,
                GITHUB_RAW + "not_official_resources.jpg",
                caption=informal
            )

        
        elif text == "🔙 Назад":
            bot.send_message(message.chat.id, "Главное меню 👇", reply_markup=main_menu())

        else:
            bot.send_message(message.chat.id, "Нажми кнопку из меню 👇")

    except Exception as e:
        print("ERROR:", e)
        bot.send_message(message.chat.id, "⚠️ Ошибка, попробуй ещё раз")



if __name__ == "__main__":
    print("BOT STARTING...")

    try:
        bot.remove_webhook()
        time.sleep(1)
    except:
        pass

    bot.infinity_polling(skip_pending=True, timeout=30)
        skip_pending=True,
        timeout=30,
        long_polling_timeout=30
    )
