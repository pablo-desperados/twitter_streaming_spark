from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import KafkaProducer, KafkaClient

access_token = "PUT YOUR OWN CREDENTIALS HERE"
access_token_secret =  "PUT YOUR OWN CREDENTIALS HERE"
consumer_key =  "PUT YOUR OWN CREDENTIALS HERE"
consumer_secret =  "PUT YOUR OWN CREDENTIALS HERE"




class TwitterListener(StreamListener):
    def on_data(self, raw_data):
        producer.send("corona_virus", raw_data.encode('utf-8'))

        return True
    def on_error(self, status_code):
        print(status_code)

producer = KafkaProducer(bootstrap_servers='localhost:9092')
l = TwitterListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, l)
stream.filter(track=["corona virus","COVID-19","pandemic"])
