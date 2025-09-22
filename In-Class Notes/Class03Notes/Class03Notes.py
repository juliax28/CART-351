
#Class 03 Notes
#make a dictionary

class_professors = {
    'Cart_253_A':'Pippin Bar',
    'Cart_211':'Brad Todd',
    'Cart_214':'Joanna Berzowska', 
    'Cart_215':'Jonathan Lessard'
}

#test if the dictionary works using 'type' by giving a variable to the function
print(type(class_professors))
# run it in the Terminal, it should say <class 'dict'> !

#A KEY doesn't have to be a string, it can be anything, although it s recommended

#Create en empty dictionary
dict_2 = {}

print(type(dict_2))

#a key can show you the value AT THAT KEY for example
print(class_professors['CART_253_A']) #should return 'Pippin Barr'
# If you try to output a key that doesn't work... it'll just give you an error in the terminal!
#If you have a variable as a key
cart_key = 'CART_215' 
print(class_professors[cart_key])
#No Problem!

#Now...is there a function that can give you ALL the eys withina. dictionary?
print(class_professors.keys())
#The keys come back as a LIST!
#What can you do with the list... ITERATE, and get the value for that key using a FOR loop
for key in class_professors.keys():
    print(class_professors[key])
    #can also work by maing a standard FOR loop
for key in class_professors:
    print(key) #However, you will get the keys, not the values. TO get the values, you need to ...
    print(class_professors[key])

print(class_professors.values())
print(class_professors.items())
#to check if a key is in a dictionary...
print('CART_253_A' in class_professors)
#This will return either TRUE or FALSE
#The value at a particular key doesn"t have to be a single value, they can be more lists, dictionaries etc.
#So... how to access something more than a string?
#See Class03Notes part02!
