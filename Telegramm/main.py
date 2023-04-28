import json

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Application, MessageHandler, filters, CommandHandler, ConversationHandler
from datetime import date, datetime, time
import random

dict = []
q = ''

suc_q, bad_q = 0, 0


def take_q():
    with open('questions.json', encoding="utf-8") as f:
        data = json.load(f)
    for i in data["test"]:
        a = [i['question'], i['response']]
        dict.append(a)


async def start(update, context):
    global q
    take_q()
    q = random.choice(dict)
    dict.remove(q)
    await update.message.reply_text(q)


async def echo(update, context):
    global q, suc_q, bad_q
    text = update.message.text
    r = dict.get(q)
    if text == r:
        suc_q += 1
        if len(dict) >= 1:
            q = random.choice(dict)
            dict.remove(q)
            await update.message.reply_text(q)
        else:
            await update.message.reply_text(f"Bad {bad_q}, Sucses {suc_q}")
    else:
        bad_q += 1


def main():
    application = Application.builder().token("6288300265:AAF8zcSYA_E46qtoGzmnjE8nvTNAfj71hd0").build()

    application.add_handler(CommandHandler("start", start))
    text_handler = MessageHandler(filters.TEXT, echo)
    application.add_handler(text_handler)
    application.run_polling()


if __name__ == '__main__':
    main()