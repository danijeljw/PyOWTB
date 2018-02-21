#!/usr/bin/env python3

import tweepy
import urllib.request
import urllib.parse
import urllib.error
import requests
from time import sleep as snooze

from tweepy import OAuthHandler
from geopy.geocoders import Nominatim

from keys2 import TwitterKeys
from OW_API_KEY import OpenWeather_SECRET_KEY

""" Twitter API credentials from keys """
CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

""" Create connection to Twitter API via Tweepy """
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


""" OpenWeather API credentials from OW_API_KEY """
OW_SECRET = OpenWeather_SECRET_KEY['secret_key']

"""
OpenWeather API URL for latitude and longitude full string:
http://api.openweathermap.org/data/2.5/uvi?appid={appid}&lat={lat}&lon={lon}
"""

# URI as list, join later
OW_URI_JSON = []

OPENWEATHER_URI = 'http://api.openweathermap.org/data/2.5/uvi?appid='

AND_LAT = '&lat='
AND_LON = '&lon='
LAT_REF = float(0)
LON_REF = float(0)


# get user details from username function
def get_user_details(username):
    userobj = api.get_user(username)
    return userobj

# array of usernames passed in
listofUsers = ['thinkgeek','PyOpenWeather']

# for 'x' (each user) in listofUsers
for x in listofUsers:
    geolocator = Nominatim()

    # assign the username to 'x'
    username = x

    # get the details of the username (assigned to 'x')
    userOBJ = get_user_details(username)

    # print the username, break line, the city of the account
    print('Twitter UserID: @' + username + '\nLocation: ',userOBJ.location)

    # convert location to geocode as location
    location = geolocator.geocode(userOBJ.location)

    # print latitude and longitude from account location conversion
    print('Latitude: ' + str(location.latitude) + ', Longitude: ' + str(location.longitude))

#   print(type(location.latitude))
    # convert latitude, longitude to 2 decimal points only (format is float)
    print(str(round((location.latitude),2)) + ', ' + str(round((location.longitude),2)))

    # assign variables to LAT and LONG (local variables in function)
    LAT_REF = round(location.latitude,2)
    LON_REF = round(location.longitude,2)

    # create new URI completed
    OW_URI_JSON.append(OPENWEATHER_URI)
    OW_URI_JSON.append(OW_SECRET)
    OW_URI_JSON.append(AND_LAT)
    OW_URI_JSON.append(str(LAT_REF))
    OW_URI_JSON.append(AND_LON)
    OW_URI_JSON.append(str(LON_REF))
    OW_API_URL = ''.join(OW_URI_JSON)

    # Print a copy of the URL that is being accessed by Python
#   print(OW_URI_JSON)
    print('OpenWeahter API URL: ' + OW_API_URL)
    JSON_DATA = requests.get(OW_API_URL).json()

    # print JSON_DATA return as string
    print('JSON Data Return: ' + str(JSON_DATA))

    # obtain UV Index and assign to var as float
    UV_INDEX = JSON_DATA['value']

    # print UV Index as string
    print('UV Index: ' + str(UV_INDEX))
    snooze(5)

    # clear variables
    OW_URI_JSON = []

    OPENWEATHER_URI = 'http://api.openweathermap.org/data/2.5/uvi?appid='

    AND_LAT = '&lat='
    AND_LON = '&lon='
    LAT_REF = float(0)
    LON_REF = float(0)



"""
if __name__ == "__main__":
    main()
"""
