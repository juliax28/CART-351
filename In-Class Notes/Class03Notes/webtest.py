#HEY HEY! Here's a note, important.Make sure you're using the right version of CONDA, to be safe wehn suing APIs use 
# conda create --name webAPisenv python=3.13.  [click Y]
#conda activate webAPisenv

#You can use different package managers, but in this class we use 'pip'
# type: pip install requests into the terminal

#import the lib - we need to use import and library name to use a library
import requests
 
#city arg
city = "Montreal" 
 
#my api key -> you should add yours
api_key = "2ba267fc5ab5b4c99201b8efab509d99" 
 
#url to get results with the city added
url_with_city ="http://api.openweathermap.org/data/2.5/weather?q=" +city 
 
#url with the api key appeneded
url_to_send = url_with_city + "&APPID=" + api_key 
 
#BTW you don't need to buid your URL this way, you can instead:
bare_url = 'http://api.openweathermap.org/data/2.5/weather'
response = requests.get(bare_url , params={"q": city, "APPID":api_key })

#make the request
response = requests.get(url_to_send) 
 #this is a 'get' request!

#get the response as json #this is a special request library, so it will output this specifci response as a JSON.
#adn then you cna PRINT it and SEE it
data = response.json() 
 
#print
# print(data)
#BUT we can also see WHAT TYPE OF DATA we got
#and we can keeps searching and specifying specific information
print(type(data))
print(data.keys())
print(data["weather"])
print(type(data["weather"]))
print(data["weather"][0])
#to make it esier for us we can put this into a variable
weather_item = data["weather"][0]
for item in weather_item:
    print(weather_item[item])

