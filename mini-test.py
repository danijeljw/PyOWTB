#!/usr/bin/env python3
#!/usr/bin/env python3

import tweepy

from tweepy import OAuthHandler
from geopy.geocoders import Nominatim
from urllib2 import Request, urlopen, URLError

from keys2 import keys
from OWAppID import OWappidKey


# Tweepy connects to Twitter using API
CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

# OpenWeather API Key secret
OWAPPIDKEY_SECRET = OWappidKey['secret_key']

# OpenWeather API URL
# THIS NEEDS TO BE SHORTENED, TOO LONG
owURL = 'http://api.openweathermap.org/data/2.5/uvi?appid=' + OWAPPIDKEY_SECRET + '&lat=' + format(location.latitude, '.2f') + '&lon=' + format(location.longitude, '.2f'))

# create connection to Twitter via API
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

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
    print('@' + username + ': \n',userOBJ.location)
    # convert location to geocode as location
    location = geolocator.geocode(userOBJ.location)
    # print latitude and longitude from account location conversion
    print((location.latitude,location.longitude))
#   print(type(location.latitude))
    # convert latitude, longitude to 2 decimal points only (format is float)
    print(format(location.latitude, '.2f'),format(location.longitude, '.2f'))
    # run API against OpenWeather to get current UV index
    #
    # MAY NEED TO REASSIGN LAT AND LONG TO VARIABLES AND USE THEM BELOW ONCE THEY HAVE BEEN SHRUNK DOWN FIRST!!!
    request = Request('http://api.openweathermap.org/data/2.5/uvi?appid=' + OWAPPIDKEY_SECRET + '&lat=' + format(location.latitude, '.2f') + '&lon=' + format(location.longitude, '.2f'))
    try:
        response = urlopen(request)
        UVIndex = response.read()
    except URLError, e:
        print 'Unable to get UV Index. Error code: ', e

