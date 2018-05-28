from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from kafka import KafkaProducer
import tweepy
import time
import json

consumer_key = '<your consumer key>'
consumer_secret = '<your consumer secret>'
access_token = '<your access token>'
access_secret = '<your access secret>'

producer = KafkaProducer(bootstrap_servers='<server>')

myTopic = '<topic_name>'

class listener(StreamListener):

     def on_status(self, status):
        msg = [status.user.screen_name, status.user.name, status.text, status.user.followers_count, status.retweet_count, status.user.location, status.created_at]
        msgJ = json.dumps(msg, indent=4, sort_keys=True, default=str)
        producer.send(myTopic,msgJ)
        print ("Got it!")

     def on_error(self, status):
        print('Got an error with status code: ' + str(status_code))
        return True 

if __name__ == '__main__':
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_secret)
	api = tweepy.API(auth)
	stream = listener
	stream = Stream(auth = api.auth, listener=stream())
	stream.filter(track=['<#hashtag>', '<keywords>'], languages=["en", "<language>"])
	
