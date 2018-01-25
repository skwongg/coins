import os
import requests
from coin.models import Coin

BINAN_API_KEY=os.environ.get("BINAN_API_KEY")
BINAN_SECRET_KEY=os.environ.get("BINAN_SECRET_KEY")
BINAN_BASE_URL=os.environ.get("BINAN_BASE_URL")

class BinancePoll(Coin):
    def pollo_world(self):
        return self.get_all_coins()

    def check_heartbeat(self):
        r = requests.get("{0}/ping".format(BINAN_BASE_URL))
        if r.status_code:
            return True
        else:
            raise

    def get_all_coins(self):
        r = requests.get(BINAN_BASE_URL + "/ticker/allPrices")
        all_coins = r.json()
        for coin in all_coins:
            if coin['symbol'] == 'BTCUSDT':
                big_btc = float(coin['price'])
        if not big_btc:
            return

        for coin in all_coins:
            if 'USDT' in coin['symbol']:
                try:
                    basepair = Coin.objects.get(pair=coin['symbol'])
                except:
                    basepair = Coin(pair=coin['symbol'])
                basepair.ticker = coin['symbol'].split('USDT')[0]
                basepair.name = coin['symbol'].split('USDT')[0]
                basepair.price = (coin['price'])
                basepair.btc_price = (float(coin['price']) / big_btc)
                basepair.save()
                print (coin)
        return all_coins, len(all_coins)

    def update_coins(self):
        r = requests.get(BINAN_BASE_URL + "/ticker/allPrices")
        all_coins = r.json()
        for coin in all_coins:
            if 'USDT' in coin['symbol']:
                # Coin.objects.find_or_create()
                print (coin['symbol'].split('USDT')[0], float(coin['price']))
            else:
                print (coin['symbol'], coin['price'])
                continue
        return "finished"
