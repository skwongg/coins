import os
import requests
from django.conf import settings
from django.core.management.base import BaseCommand
from cointegrations.binance.poll import BinancePoll

class Command(BaseCommand):
    help = 'Polls exchange API for trading data'
    args = 'Takes no argument'
    def add_arguments(self, parser):
        parser.add_argument('exchange_name', type=str)


    def handle(self, *args, **options):
        exch = options['exchange_name']
        a = BinancePoll()
        if exch =='poll':
            a.poll_prices()
            return "binance price polling complete"

        elif exch == 'volume':
            a.poll_volume()
            return "binance volume polling complete"
        else:
            return 'Error: {0} exchange not found'.format(exch)
        return options['exchange_name']
