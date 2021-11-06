import telebot
import config
from telebot import types
 
bot = telebot.TeleBot(config.TOKEN)

JoinedFile = open("F:\BOOT\join.txt", "r")
JoinedUsers = set()
for line in JoinedFile:
    JoinedUsers.add(line.strip())
JoinedFile.close()

@bot.message_handler(commands=['start'])
def startJoin(message):
    if not str(message.chat.id) in JoinedUsers:
        JoinedFile = open("F:\BOOT\join.txt", "a")
        JoinedFile.write(str(message.chat.id) + "\n")
        JoinedUsers.add(message.chat.id)

@bot.message_handler(commands=['special'])
def mess(message):
    for user in JoinedUsers:
        bot.send_message(user, message.text[message.text.find(' '):])
