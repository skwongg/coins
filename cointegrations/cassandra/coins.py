from cassandra.cluster import Cluster
from cassandra.policies import DCAwareRoundRobinPolicy
from cassandra.cqlengine.models import Model, columns

cluster=Cluster()

class Coin(Model):
    __keyspace__ = "cassy"
    __table_name__ = "coins"
    id = columns.UUID(primary_key=True)
    name = columns.Text()
    ticker = columns.Text()
    pair = columns.Text()
    icon_url = columns.Text()
    price = columns.Decimal()
    btc_price = columns.Decimal()
