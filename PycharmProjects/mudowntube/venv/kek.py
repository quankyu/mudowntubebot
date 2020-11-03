import requests
import os
import telebot
import subprocess
import time
from pytube import YouTube
bot = telebot.TeleBot('1329199771:AAElvyW_AT21Jui9p_quXuH3VnC0jAu5oxw')
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,"i download your videos in mp3 format")
@bot.message_handler(content_types=['text'])
def send_audio(message):
    try:
        response = requests.get(message.text)
        yt = YouTube(message.text)
        t = yt.streams.filter(only_audio=True)
        _filename=yt.streams[0].title
        audio=t[0].download(filename=_filename)
        time.sleep(1)
        mp4 = "'%s'.mp4" % _filename
        mp3 = "'%s'.mp3" % _filename
        ffmpeg = ('ffmpeg -i %s ' % mp4 + mp3)
        subprocess.call(ffmpeg, shell=True)
        bot.send_audio(message.chat.id, audio=open(audio, 'rb'), title=_filename)
    except requests.ConnectionError as exception:
        bot.send_message(message.chat.id, "String is not valid URL")


bot.polling()



