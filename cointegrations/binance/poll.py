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
        main_coins = dict()
        r = requests.get(BINAN_BASE_URL + "/ticker/allPrices")
        all_coins = r.json()
        for coin in all_coins:
            if coin['symbol'] == 'BTCUSDT':
                big_btc = float(coin['price'])
                break
        if not big_btc:
            raise

        for coin in all_coins:
            if 'USDT' in coin['symbol']:
                try:
                    basepair = Coin.objects.get(pair=coin['symbol'])
                except:
                    basepair = Coin(pair=coin['symbol'])
                ticker = coin['symbol'].split('USDT')[0]
                price = coin['price']
                basepair.ticker = ticker
                basepair.name = ticker
                basepair.price = price
                basepair.btc_price = (float(price) / big_btc)
                basepair.save()

                ##turn into dictionary entry
                main_coins[ticker] = price

        ##TRADING pairs
        for coin in all_coins:
            if 'USDT' in coin['symbol']:
                continue
            else:
                for maincoin in main_coins.keys():
                    if maincoin in coin['symbol']:
                        if coin['symbol'].index(maincoin) > 0:
                            cutoff = coin['symbol'].index(maincoin)
                            ticker = coin['symbol'][0:cutoff]
                            in_terms_of = coin['symbol'][cutoff:]
                            price = float(main_coins[in_terms_of]) * float(coin['price'])


                            # print(ticker, in_terms_of)

                            try:
                                cryptopair = Coin.objects.get(pair=coin['symbol'])
                            except:
                                cryptopair = Coin(pair=coin['symbol'])
                            cryptopair.ticker = ticker
                            cryptopair.name = ticker
                            cryptopair.price = price
                            cryptopair.btc_price = (price / big_btc)
                            cryptopair.save()

                            print(price, ticker, coin['price'], in_terms_of)
                            print("Coin {0} saved successfully.".format(ticker))
                            print ("*" * 100)


                # print (coin['symbol'], coin['price'])
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
