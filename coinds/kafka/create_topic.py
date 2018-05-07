from pykafka import KafkaClient
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import json
import os

# client = KafkaClient(hosts='127.0.0.1:9092')

#load dependencies for spark streaming kafka
os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.0.2 pyspark-shell'
sc = SparkContext(appName="pythonSparkStreamingKafka")
sc.setLogLevel("WARN")
ssc = StreamingContext(sc, 60)
kafkaStream = KafkaUtils.createStream(ssc, \
    'localhost:2181', 'consumergroup', {'coins': 1})
#localhost:2181 is the cluster address
#consumergroup would be consumer group
#coins would be the topic
