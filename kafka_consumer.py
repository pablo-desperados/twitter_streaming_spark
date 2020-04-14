from kafka import KafkaConsumer
import json
from json import loads
import clean_tweet 


consumer= KafkaConsumer('corona_virus',bootstrap_servers=['localhost:9092'],auto_offset_reset='earliest',enable_auto_commit=True,group_id='my-group',value_deserializer= (lambda x: json.loads(x.decode('utf-8'))))

for message in consumer:
    twitter_message = message.value

    clean_tweet.get_hashtags(twitter_message)
    
