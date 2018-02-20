    try:
        response = urlopen(request)
        UVIndex = response.read()
    except URLError, e:
        print 'Unable to get UV Index. Error code: ', e





# assign the return of the data in the URL and format as JSON to the var json_data
json_data = requests.get(url).json()
# print(json_data)

# get the 'status' dictionary key value from data returned
json_status = json_data['status']
print('API Status: ' + json_status)

# from the results dictionary value, get the first key in the list, then identify the formatted_address value from the dictionary and assign it to the var 
'formatted_address'
formatted_address = json_data['results'][0]['formatted_address']

print(formatted_address )



