#!/usr/bin/env python3

import tweepy
import random
import json
import time
import pprint

# from our keys module (keys.py), import the keys dictionary
from keys2 import keys

# Tweepy connects to Twitter using API
CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

# create connection to Twitter via API
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# search Twitter for tweets matching
twts = api.search(q="Hello World!")


for status in api.user_timeline('PyOpenWeather'):
    api.retweet(status.id)


# If debug_mode is True then the bot won't actually tweet
# set debug_mode is False to enable tweets
debug_mode = True



# Functions that allow the bot to tweet or reply to tweets
def tweet(status):
    print ("JUST TWEETED: "), status
    # Only *actually* send the tweet on twitter if we're not in debug mode
    if debug_mode == False:
        api.update_status(status)


def tweet_with_probability(status, probability):
    # Change the probability of tweeting variable to affect how often the bot tweets
    rand = random.random()
    if rand <= probability:
        print ("JUST TWEETED: "), status
        # Only *actually* send the tweet on twitter if we're not in debug mode
        if debug_mode == False:
            api.update_status(status)


#Tweet when keyword is picked up

















