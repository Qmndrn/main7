from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
from dotenv import load_dotenv


zodiac_predictions = {
    'овен': 'Сегодня день для решительных действий! Вас ждёт успех.',
    'телец': 'Проведите день спокойно, подумайте о будущем. Хороший день для планирования.',
    'близнецы': 'Будьте осторожны с новыми знакомыми, не все они искренни.',
    'рак': 'Сегодня удачный день для улучшения отношений с близкими.',
    'лев': 'Постарайтесь избежать конфликтов на работе, они могут затянуться.',
    'дева': 'Сегодня удачный день для финансовых вложений и покупок.',
    'весы': 'Возможно, вам придется принять важное решение, доверьтесь интуиции.',
    'скорпион': 'Не бойтесь рисковать сегодня, это принесет свои плоды.',
    'стрелец': 'Сегодня отличный день для путешествий и новых впечатлений.',
    'козерог': 'Уделите внимание здоровью, не перегружайте себя на работе.',
    'водолей': 'Вы найдете решение проблемы, которая давно вас беспокоит.',
    'рыбы': 'Сегодня вас ждет приятный сюрприз от близкого человека.'
}


def start(update, context):
    update.message.reply_text("Привет! Я могу предсказать твою судьбу по знаку зодиака! Напиши свой знак!")


def help(update, context):
    update.message.reply_text("Напиши свой знак зодиака и я дам тебе предсказание или напиши (зодиаки), что бы узнать все знаки зодиака")


def zodiac_prediction(update, context):
    users_answ = update.message.text.lower().strip()
    if users_answ in zodiac_predictions:
        update.message.reply_text(zodiac_predictions[users_answ])
    elif users_answ == "зодиаки":
        signs = ', '.join(zodiac_predictions.keys())
        update.message.reply_text(f"Вот все знаки зодиака: {signs}")
    else:
        signs = ', '.join(zodiac_predictions.keys())
        update.message.reply_text(f"Знак не найден. Напиши один из: {signs}")   


def main():
    load_dotenv()
    TOKEN = os.getenv("TELEGRAM_TOKEN")
    
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('help', help))
    dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), zodiac_prediction))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
