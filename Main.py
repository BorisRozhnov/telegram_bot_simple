"""
This in telebot based telegram bot
Token:      {{ api_token}}
Name:       Gitlab CI test
UserName:   my_gitlabci_test_bot
pip install pytelegrambotapi
pip3 install pytelegrambotapi --upgrade
"""
import telebot
import random

bot = telebot.TeleBot('{{ api_token}}')
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('hi', 'bye', 'can I help you', 'entertain me', '/start')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "What's up with it, Vanilla face?", reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'hi':
        bot.send_message(message.chat.id, 'hail to my lord')
    elif message.text.lower() == 'bye':
        bot.send_message(message.chat.id, 'Hasta la vista, baby')
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIFY19E_R2yAAFPkepr4x-vGf15DIV4TQACDA0AApI2owvVLwQ-v0VBOBsE')
    elif message.text.lower() == 'can i help you':
        bot.send_message(message.chat.id, "Me and my homies just parked our slab outside. We're looking for somewhere to post up our Black asses for the night.")
    elif message.text.lower() == 'entertain me':
        bot.send_sticker(message.chat.id, get_random_sticker())
    elif message.text.lower() == 'love you':
        bot.send_sticker(message.chat.id, 'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')
    elif message.text.lower() == '/start':
        bot.send_sticker(message.chat.id, 'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')
    else:
        bot.send_message(message.chat.id, 'could you please repeat that')

@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)

sticker_list = ['CAACAgIAAxkBAAIFXV9E-mJwwRG-Gqn8gtp7SUbTLBrrAALVAQACFnxoA4t1RoV0EGq3GwQ',
                'CAACAgIAAxkBAAIFWV9E-dTUmCu9okh2A0HGfz9n_ljrAAKKAQACFnxoA1qPWYmQI1VvGwQ',
                'CAACAgIAAxkBAAIFX19E_PDJjl3VXXfiBFmH42-sVnYFAALTAQACFnxoA1mYVs_jlKjXGwQ'
                ]

def get_random_sticker():
    return random.choices(sticker_list)[0]

bot.polling()