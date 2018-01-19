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
        acceptable_exchanges = ('binance','bittrex','gdax','kucoin','kraken')
        if exch in acceptable_exchanges:
            if exch == 'binance':
                a = BinancePoll()
                a.pollo_world()
                return "exchange poll for: <<{0}>> completed".format(exch)
        else:
            return 'Error: {0} exchange not found'.format(exch)
        return options['exchange_name']
