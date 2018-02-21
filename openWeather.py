from keys2 import OpenWeather_key

APIkey = OpenWeather_key['secret']

class UVIndex:

    def __init__(self, latitude, longitude):
        if type(latitude) == float or type(longitude) == float:
            self.latitude = str(round(latitude),2)
            self.longitude = str(round(longitude),2)
            self.URL = ['http://api.openweathermap.org/data/2.5/uvi?appid=']
        else:
            print('Error: only float value accepted\n',
                  '\n',
                  'USE: UVIndex(atitude {as float},longitude {as float})')

    def jsonURL(self):
        self.URL.extend(APIkey, '&lat=', self.latitude, '&long=', self.longitude)
        self.URL = ''.join(self.URL)
        return str(self.URL)


"""
From here, using the requests.get function, can assign the value of UVIndex.returnURL 
and convert to JSON. The value wanted is 'value'

Example:

    UVIndex(32.233, -38.274)
    UV_json_data = requests.get(UVIndex.jsonURL).json
    print('UV Index: ' + UV_json_data['value'])


This will print text with the UV Index for location specified by lat & lon

Example:

    UV Index: 4.2
"""
