
# shopping = {'vegetables':['spinach', 'carrots', 'brocolli', 'lettuce'], 
#             'fruit': ['cantaloupe', 'bananas'], 
#             'bakery':['bagels', 'rye bread']}

# print(shopping['fruit']) #is gonna show you everything with the KEY 'fruit'
# #you can go through it with a normal FOR loop
# for item in shopping['fruit']:
#     print(item)

# #DICTIONARIES are a lot more like JSON files than LISTS

# #but what if we want to access a particular item in a list, such as 'spinach'
# shopping['vegetables'][0] #access the first element in 'vegetables'
# print(shopping['vegetables'][0])

# shopping_rev = {'vegetables':{"green": ['spinach', 'brocolli', "lettuce"],
#                               "orange":["carrots"]
#                               },
#                              'fruit': ['cantaloupe', 'bananas'], 
#                              'bakery':['bagels', 'rye bread']}
# print(shopping_rev['vegetables'],['green'][0]) #print out spinach
# print(shopping_rev['vegetables'],['orange'][0]) #print out carrots
# #Append an item to a dictionary
# shopping_rev['cleaning_items'] = ['dishsoap', 'sponges']
# print (shopping_rev)

# #WEB APIs
#APIs r NOT free
#If you try to do everything CLIENT side, you may run into security issues, so it's better to do some things SERVER side
#URL - Everything you're trying to access from an API is frmo a specific URL
#Manipulating URLs!
#EXAMPLE http://www.example.com/categories/test?arg1=apples&arg2=winter
# http: scheme
# www.example.com: host
# categories/test: path
# ?arg1=apples&arg2=winter: query string
#You can pass variables through your URL, the '&' divides key value pairs

#BUT HOWWW DO WE USE IT!?

#DOCUMENTATON for the API you're using is so important, that's how you know how to access certain things
#Normally, we use URLs, but these are not good at describing structured DATA, because ists inside lists isnide this inside that.. too complicated for HTML
#you can get the JSON data out of a API's page and manipulate it

#EXAMPLE: SAy I wanna make a weather app,  ca sue the WEATHERAPI in order to get data for my app, and also accesing different areas

#How do we make web API requests? USually, we make requests thourgh our browser, but we can't do anything with it. 
#We can instead make requests directly through python!

#Python has its own built-in request functions

#CONITNUED IN WEBTEST

