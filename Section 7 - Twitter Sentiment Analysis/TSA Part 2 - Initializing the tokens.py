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