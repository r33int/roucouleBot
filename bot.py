# coding=UTF-8

import os
import telebot
  
bot = telebot.TeleBot(os.environ['BOT_API_TOKEN'])

import logging

logger = telebot.logger
telebot.logger.setLevel(logging.INFO) # Outputs debug messages to console.

@bot.message_handler(commands=['clean'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'broken, do not use');

@bot.message_handler(commands=['shrug'])
def send_welcome(message):
    bot.send_message(message.chat.id, '¯\_(ツ)_/¯');

@bot.message_handler(func=lambda m: 'hifumin' in m.text.lower())
def handle_test(message):
    bot.send_message(message.chat.id, '<3');
	
@bot.message_handler(func=lambda m: 'sfr' in m.text.lower())
def handle_test(message):
    bot.send_message(message.chat.id, 'Bonjour, votre demande concerne bien votre IBAN FR42904290489FE ?');

@bot.message_handler(func=lambda m: "sdchachaze" in m.text.lower())
def command_text(message):
    bot.send_message(message.chat.id, "on voit au nom que c'est nul");

@bot.message_handler(func=lambda m: "artv" in m.text.lower())
def command_text(message):
    bot.send_message(message.chat.id, "Y'a les flics chez moi wtf");

@bot.message_handler(func=lambda m: "test" in m.text.lower())
def command_text(message):
    bot.send_message(message.chat.id, "reçu");

@bot.message_handler(func=lambda m: "nenuit" in m.text.lower())
def command_text(message):
    bot.send_message(message.chat.id, "Bonne nuit !");

@bot.message_handler(func=lambda m: "ur mom gay" in m.text.lower())
def command_text(message):
    bot.send_message(message.chat.id, "no u");

@bot.message_handler(func=lambda m: "tg" in m.text.lower())
def command_text(message):
    bot.send_message(message.chat.id, "tg");

@bot.message_handler(func=lambda m: "jpp" in m.text.lower())
def command_photo(message):
    #Replace by image path
	bot.send_photo(message.chat.id, open('jpp.jpg', 'rb'));

bot.polling(none_stop=1, interval=0, timeout=100000)
Loop()