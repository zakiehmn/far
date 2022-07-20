import telebot
from telebot import *
from consts import Environmnets



def get_bot(env):
  if env == Environmnets.PRODUCTION:
    API_TOKEN = ''
  else:
    API_TOKEN = '5548207177:AAH-rGSWa96rxsTU22RoGqUMJt0taO_1bBM'
  return telebot.TeleBot(API_TOKEN, threaded=False)


def get_admin_bot(env):

  if env == Environmnets.PRODUCTION:
    API_TOKEN = ''
  else:
    API_TOKEN = ''
  return telebot.TeleBot(API_TOKEN)
