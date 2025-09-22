#setup

import requests
#Assigning a variable to the API Key
token = "5f86f11d709364014dc941832b05e60a2ce498d3"
#Point it to the world air quality index
url = "https://api.waqi.info/search/"
#Sets 'montreal' to 'keyword' to indicate Montreal as the station.
response = requests.get(url, params={"token": token, "keyword": "montreal"})
#Give back the information as a JSON format
results = response.json()
#Prints the result in the terminal
print(results)

#getting the TYPE of RESULTS
print(type(results))
#The TYPE of RESULTS is 'dict' or 'dictionary'

#Getting the KEYS of RESULTS
print(results.keys())
#The keys are 'status' and 'data'

#Code of data field and storing it

responseData = results["data"]
print(type(responseData))
#the 'type' of 'responseData' is 'list'
for item in responseData:
    print(item)
#represents the station, time, timezone, name, coordinates, country
    print(type(item))
    
    #'type' of 'item' is dictonary'
    print(item.keys())
    #the keys associated with 'item' are uid, aqi, time, station
    print(item["station"]["name"])
    #
    print("lat:"f'{item["station"]["geo"][0]}' , "long:" f'{item["station"]["geo"][1]}')
    #Sainte-Anne-de-Bellevue, Montreal, Canada
    #[45.426509, -73.928944]
    print("Aqi:"f"{item["aqi"]}", "UID:" f"{item["uid"]}")