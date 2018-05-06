from cassandra.cluster import Cluster
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table
from coins import Coin
CQLENG_ALLOW_SCHEMA_MANAGEMENT='CQLENG_ALLOW_SCHEMA_MANAGEMENT'

cluster=Cluster()
connection.setup(['127.0.0.1'], "cassy", protocol_version=3)

class CoinPrice
a = Coin()




##Cassandra coin model syncs to default cassandra connection under cassy keyspace.
##row key for time series data  https://academy.datastax.com/resources/getting-started-time-series-data-modeling

#row partitioning:
# In some cases, the amount of data gathered for a single device isn’t practical to fit onto a single row. Cassandra can store up to 2 billion columns per row, but if we’re storing data every millisecond you wouldn’t even get a month’s worth of data. The solution is to use a pattern called row partitioning by adding data to the row key to limit the amount of columns you get per device. Using data already available in the event, we can use the date portion of the timestamp and add that to the weather station id. This will give us a row per day, per weather station, and an easy way to find the data. (figure 2)


# day = datetime.date.today().strftime('%m-%d-%Y')
# name = "XRP"
# ticker="XRPUSD"
# pair="XRPUSD"
# icon_url="https://www.google.com"
# price="0.8934"
# price=0.8934
# btc_price=0.00001
# created_at=datetime.datetime.now()
# source = "binance"
# a = Coin.create(day=day, name=name, ticker=ticker, pair=pair, icon_url=icon_url, price=price, btc_price=btc_price, source="binance", created_at=created_at)
