from cassandra.cluster import Cluster
import uuid
from cassandra.cqlengine import columns
from cassandra.cqlengine import connection
from datetime import datetime
from cassandra.cqlengine.management import sync_table
from cassandra.cqlengine.models import Model
cluster=Cluster()

class Coin(Model):
    id=columns.UUID(partition_key=True, default=uuid.uuid4)
    day=columns.Text()
    name=columns.Text(required=True)
    ticker=columns.Text(required=True)
    pair=columns.Text(required=True)
    icon_url=columns.Text(required=False)
    price=columns.Decimal(required=False)
    btc_price=columns.Decimal(required=False)
    source=columns.Text()
    created_at=columns.DateTime()


connection.setup(['127.0.0.1'], "cassy", protocol_version=3)
sync_table(Coin)




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
# a = Coin.create(day=day, name=name, ticker=ticker, pair=pair, icon_url=icon_url, price=price, btc_price=btc_price, created_at=created_at)
