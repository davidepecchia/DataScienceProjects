from kafka import KafkaConsumer
from pymongo import MongoClient
import time
import json


consumer = KafkaConsumer(bootstrap_servers='<server>',
								auto_offset_reset='earliest',					#remove auto_offset_reset='earliest' if you don't want to put all the data of a topic (from the beginning) in a collection
								consumer_timeout_ms=1000)
								
consumer.subscribe('<topic_name>')


client = MongoClient()
db = client.<DB_name>


while(True):
	for msgJ in consumer:
		tweet = json.loads(msgJ.value)
		row = { "Screen_name" : tweet[0] , 
                	"Name" : tweet[1] , 
                        "Text" : tweet[2] , 
                            "Followers" : tweet[3] ,
                                "Number_Retweet" : tweet[4] ,
                                    "Position" : tweet[5],
                                    	"Date_time" : tweet[6] }
		print (row)
		result = db.<collection_name>.insert_one(row)
	time.sleep(5)

	