from cassandra.cluster import Cluster
import uuid
from cassandra.cqlengine import columns
from cassandra.cqlengine import connection
from datetime import datetime
from cassandra.cqlengine.management import sync_table
from cassandra.cqlengine.models import Model
cluster=Cluster()

class Coin(Model):
    coin_id=columns.UUID(primary_key=True, default=uuid.uuid4)
    name=columns.Text(required=True)
    ticker=columns.Text(required=True)
    pair=columns.Text(required=True)
    icon_url=columns.Text(required=False)
    price=columns.Decimal(required=False)
    btc_price=columns.Decimal(required=False)
    created_at=columns.DateTime()


connection.setup(['127.0.0.1'], "cassy", protocol_version=3)
sync_table(Coin)


##Cassandra coin model syncs to default cassandra connection under cassy keyspace.
