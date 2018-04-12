# Twitter Sentiment Analysis using NLP

# Install tweepy - pip install tweepy

# Importing the libraries
import tweepy
import re
import pickle

from tweepy import OAuthHandler

# Please change with your own consumer key, consumer secret, access token and access secret
consumer_key = 'PglM3T2NoBzq0ktWTUBelJTHg'
consumer_secret = 'aDKWrqZQAwje0fJBBVufrxJWE5KY3T8cSlUUGuRyvuvYznGQOC'
access_token = '624310916-N9aUtUrr1BjnNhOPV6vPz0Aty1OZ1utIyF3hm4Cm'
access_secret = 'VyJCNbvceb6RpPXRLVo8e2sysJXwQ59AEc9KAQfQfNRoO'

# Initializing the tokens
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
args = ['trump'];
api = tweepy.API(auth,timeout=10)

# Fetching the tweets
list_tweets = []

query = args[0]
if len(args) == 1:
    for status in tweepy.Cursor(api.search,q=query+" -filter:retweets",lang='en',result_type='recent',geocode="22.1568,89.4332,500km").items(100):
        list_tweets.append(status.text)
        
# Loading the vectorizer and classfier
with open('classifier.pickle','rb') as f:
    classifier = pickle.load(f)
    
with open('tfidfmodel.pickle','rb') as f:
    tfidf = pickle.load(f)    