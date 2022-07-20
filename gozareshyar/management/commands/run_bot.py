from django.core.management.base import BaseCommand
from gozareshyar.bot import *
import telebot


class Command(BaseCommand):
    help = 'run bot.py'

    def handle(self, *args, **kwargs):
        bot.infinity_polling()