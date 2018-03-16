# coding=UTF-8

import os
import telebot
  
bot = telebot.TeleBot(os.environ['BOT_API_TOKEN'])

import logging

logger = telebot.logger
telebot.logger.setLevel(logging.INFO) # Outputs debug messages to console.

@bot.message_handler(func=lambda m: 'nyo' in m.text.lower())
def handle_test(message):
    bot.send_message(message.chat.id, 'success')
	
@bot.message_handler(func=lambda message: "hifumin" in message.text.lower())
def command_text(m):
    bot.send_message(m.chat.id, "<3")

@bot.message_handler(func=lambda message: "sfr" in message.text.lower())
def command_text(m):
    bot.send_message(m.chat.id, "Bonjour, votre demande concerne bien votre IBAN FR42904290489FE ?")

@bot.message_handler(func=lambda message: "sdchachaze" in message.text.lower())
def command_text(m):
    bot.send_message(m.chat.id, "on voit au nom que c'est nul")

@bot.message_handler(func=lambda message: "jpp" in message.text.lower())
def command_photo(m):
	#Replace by image path
	bot.send_photo(m.chat.id, open('/home/r33int/Git/roucouleBot/jpp.jpg', 'rb'))

bot.polling(none_stop=1, interval=0, timeout=100000)
Loop()