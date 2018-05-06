import os
import requests
from pymongo import MongoClient
from coin.models import Coin
from multiprocessing import Pool
from coinds.cassandra.coins import Coin as CassandraCoin

BINAN_API_KEY=os.environ.get("BINAN_API_KEY")
BINAN_SECRET_KEY=os.environ.get("BINAN_SECRET_KEY")
BINAN_BASE_URL=os.environ.get("BINAN_BASE_URL")
MONGO_URL=os.environ.get("MONGO_URL")
mongo = MongoClient(MONGO_URL)
from datetime import datetime

class BinancePoll(Coin):
    btc_price = 0
    maincoins=dict()
    day =  datetime.now().strftime('%m-%d-%Y')
    time = datetime.now()

    def write_prices(self):
        return self.update_all_coins()

    def find_btc(self, all_coins):
        for coin in all_coins:
            if coin['symbol'] == 'BTCUSDT':
                return float(coin['price'])
        raise ValueError('Bitcoin USD pair not found.')

    def write_basepairs(self, coin_obj):
        if 'USDT' in coin_obj['symbol']:
            try:
                basepair=Coin.objects.get(pair=coin_obj['symbol'])
            except:
                basepair=Coin(pair=coin_obj['symbol'])
                print("NEW COIN: {0}".format(coin_obj['symbol']))
                print("@" * 100)
            ticker = coin_obj['symbol'].split('USDT')[0]
            price = float(coin_obj['price'])
            btc_price = price / self.btc_price
            basepair.ticker = ticker
            basepair.name = ticker
            basepair.price = price
            basepair.btc_price = btc_price
            basepair.save()
            #this Cassandra call doesnt belong here, i just needed a way to get more than one row in so i could test my graph on the frontend. im sorry.
            CassandraCoin.create(day=self.day, name=ticker, ticker=ticker, pair=coin_obj['symbol'], icon_url="None", price=price, btc_price=btc_price, source="binance", created_at=self.time)

            return ticker, price
        else:
            return False

    def write_tradepairs(self, coin_obj):
        pair = coin_obj['symbol']
        if 'USDT' in pair:
            return False
        else:
            for maincoin in self.maincoins.keys():
                if maincoin in pair and pair.index(maincoin) > 0:
                    cutoff = pair.index(maincoin)
                    ticker = pair[0:cutoff]
                    in_terms_of = pair[cutoff:]
                    price = float(self.maincoins[in_terms_of]) * float(coin_obj['price'])
                    btc_price = price / self.btc_price
                    try:
                        cryptopair = Coin.objects.get(pair=pair)
                    except:
                        cryptopair = Coin(pair=pair)
                    cryptopair.ticker = ticker
                    cryptopair.name = ticker
                    cryptopair.price = price
                    cryptopair.btc_price = btc_price
                    cryptopair.save()
                    #this Cassandra call doesnt belong here, i just needed a way to get more than one row in so i could test my graph on the frontend. im sorry.
                    CassandraCoin.create(day=self.day, name=ticker, ticker=ticker, pair=pair, icon_url="None", price=price, btc_price=btc_price, source="binance", created_at=self.time)
                    print(price, ticker, coin_obj['price'], in_terms_of)
                    print("Coin {0} saved successfully.".format(ticker))
                    print("*" * 100)
                else:
                    continue

    def update_all_coins(self):
        all_coins = requests.get(BINAN_BASE_URL + "/ticker/allPrices").json()
        self.btc_price = self.find_btc(all_coins)
        #BASE COINS: BTC, ETH, LTC, NEO, BNB
        for coin in all_coins:
            if self.write_basepairs(coin):
                self.maincoins[self.write_basepairs(coin)[0]] = self.write_basepairs(coin)[1]
        ##TRADING pairs
        for coin in all_coins:
            self.write_tradepairs(coin)
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
