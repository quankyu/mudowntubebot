import requests
import os
import ffmpeg
import urllib
import telebot
bot = telebot.TeleBot('1329199771:AAElvyW_AT21Jui9p_quXuH3VnC0jAu5oxw')
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,"i download your videos in mp3 format")
@bot.message_handler(content_types=['text'])
def send_audio(message):
    lurl=urllib.parse.quote(message.text())
    print(lurl)



bot.polling()



