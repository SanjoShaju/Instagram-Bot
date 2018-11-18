# Use this trainer first to train the commenting bot
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import pickle

bot = ChatBot('instabot')
bot.set_trainer(ListTrainer)

#Loading pickle commments
f = open('./dataset/InstagramComments_.p', 'rb')
comments = pickle.load(f)
f.close()

#Training Bot with existing comments
for convo in comments[:10000]:
    bot.train(convo)
