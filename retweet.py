import tweepy
import time
import os
from dotenv import load_dotenv

load_dotenv()

consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')
query = os.getenv('QUERY')
tweets_per_query = os.getenv('TWEETS_PER_QUERY')
tweets_language = os.getenv('TWEETS_LANGUAGE')
sleeping_time = os.getenv('SLEEPING_TIME')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

already = []

print(tweets_language)

for tweet in tweepy.Cursor(api.search, q=query, lang=tweets_language, result_type="recent").items(int(tweets_per_query)):
	if(tweet.id not in already):

		user = tweet.user.screen_name
		id = tweet.id
		url = 'https://twitter.com/' + user +  '/status/' + str(id)
		print(url)
	
		try:
			tweet.retweet()
			print("Retweeted.")
			already.append(tweet.id)
			time.sleep(5)
		except Exception as e: 
			print (str(e))
			print("skipped" + str(tweet.id))
			already.append(tweet.id)

time.sleep(int(sleeping_time))
print("Next Tweet...")

