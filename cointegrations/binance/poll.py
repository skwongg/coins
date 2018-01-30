import os
import requests
from coin.models import Coin

BINAN_API_KEY=os.environ.get("BINAN_API_KEY")
BINAN_SECRET_KEY=os.environ.get("BINAN_SECRET_KEY")
BINAN_BASE_URL=os.environ.get("BINAN_BASE_URL")

class BinancePoll(Coin):
    btc_price = ''
    maincoins=dict()

    def poll_prices(self):
        return self.update_all_coins()

    def ping_binance(self):
        r = requests.get("{0}/ping".format(BINAN_BASE_URL))
        if r.status_code:
            return True
        else:
            raise

    def get_binance_time(self):
        r = requests.get("{0}/time".format(BINAN_BASE_URL)).json()
        if 'serverTime' in r:
            return r['serverTime']
        else:
            return False


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
            ticker = coin_obj['symbol'].split('USDT')[0]
            price = coin_obj['price']
            basepair.ticker = ticker
            basepair.name = ticker
            basepair.price = price
            basepair.btc_price = self.btc_price
            basepair.save()
            return ticker, price
        else:
            return False

    def write_tradepairs(self, coin_obj):
        if 'USDT' in coin_obj['symbol']:
            return False
        else:
            for maincoin in self.maincoins.keys():
                if maincoin in coin_obj['symbol'] and coin_obj['symbol'].index(maincoin) > 0:
                    cutoff = coin_obj['symbol'].index(maincoin)
                    ticker = coin_obj['symbol'][0:cutoff]
                    in_terms_of = coin_obj['symbol'][cutoff:]
                    price = float(self.maincoins[in_terms_of]) * float(coin_obj['price'])

                    try:
                        cryptopair = Coin.objects.get(pair=coin_obj['symbol'])
                    except:
                        cryptopair = Coin(pair=coin_obj['symbol'])
                    cryptopair.ticker = ticker
                    cryptopair.name = ticker
                    cryptopair.price = price
                    cryptopair.btc_price = (price / self.btc_price)
                    cryptopair.save()

                    print(price, ticker, coin_obj['price'], in_terms_of)
                    print("Coin {0} saved successfully.".format(ticker))
                    print ("*" * 100)
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




    def poll_volume(self):
        r = requests.get(BINAN_BASE_URL + "/aggTrades?symbol=PIVAXBNB")
        agg_trades = r.json()

        if ('code' in agg_trades) and ((agg_trades['code'] == -1121) or (agg_trades['code'] == -1100)):
            return False
        print(agg_trades)
        return agg_trades
