from elasticsearch import Elasticsearch
from coin.models import Coin
import requests
import os

es = Elasticsearch()

def build_coin_index():
    es.indices.create(index='coins', ignore=400)
    response = es.search()
    for coin in Coin.objects.all():
        es.index(index="coins",
                doc_type="coin",
                id=coin.id,
                body={
                    "id": coin.pk,
                    "name": coin.name,
                    "ticker": coin.ticker,
                    "pair": coin.pair,
                    "price": coin.price,
                    "btc_price": coin.btc_price,
                    "icon_url": coin.icon_url
                    }
                )

def search(querystring):
    ES_COIN_SEARCH_URL = os.environ.get("ES_COIN_SEARCH_URL") + """size=10&q=pair:*{0}*""".format(querystring)
    res = requests.get(ES_COIN_SEARCH_URL).json()
    return res
