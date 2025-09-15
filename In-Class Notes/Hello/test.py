#!/usr/bin/python3
# print("HEY")

# '''this is how to
# make a multi-line comment'''

# print(30+5)

# if you want to avoid float divisions, add // to round down
# Example:
# print(30.7//5)


# Algebra rules apply, Ex:
# print(100 - 25 * 4)

# using % is a modular and will give you the remainder of a division
# you can mulpti things to the power of with two **
# print(5**3)

# comparison operators <,>,=,!, ==., >=, <=
# print(3 > 5) #returns false

# logical operators: and, or , not
# print(True and True) #results in true
# print(True and False) 
# print(False and False)

#ctrl + / will comment out all selected

# cars = 100 #create a variable
# #automatically makes variables an interger
# space_in_car = 3
# drivers = 30
# possible_passengers = 90
# cars_not_driven = cars - drivers
# cars_driven = drivers
# car_pool_capacity = cars_driven * space_in_car
# print (car_pool_capacity)

# car_name = "subaru" #strings are in quotes
# print the string
# print("the car's name is", car_name)

# f-string
# print(f"the car's name is {car_name}")

# you can also put f-trings AS a value for a variable, like so!
# car_statement = f"the car's name is {car_name}"
# print(car_statement)

# my_name = input("Julia")
# won't assign anything until you input it
# print(my_name)
# my_fav_color = input("type your fav color: ")
# print(my_fav_color)

# help(input)
#using help on any in-bult function in python will give you more info on it 

# #making a new function
# def least_diff(x1, x2, x3): 
#     #body of function
#     """
#     GOOD IDEA: If you're making an important function, use a descriptive 
#     multi-line comment like this to keep organized!
#     Now, if you use 'help' on this function, the 'help' description will include this desription! It's called
#     a 'DOC string'
#     """
#     diff_1 = abs(x1-2)
#     diff_2 = abs(x2-x3)
#     diff_3 = abs(x1-x3)
#     return min(diff_1,diff_2,diff_3)

# #diff, abs and min are in-built python functions
# #now how do we use this function? We would use the name of the function

# least_diff_a = least_diff(20,60,6)
# print(least_diff_a)

#passing functions as parameters
#We can say "when THIS function runs, you will do something with it"

#EX:
# def process(alteringFunction, text):
#     newText = alteringFunction(text)
#     return newText

# def textToUpper(text):
#     return text.upper()
# #text.upper is an inbuilt python function to make smth upper case

# def textToLower(text):
#     return text.lower()

#We could all both seprately as in 
# textToLower(("JULIA"))
# textToUpper(("banana"))

#HOWEVER
# print(process(textToLower,"cantEloupe"))
# print(process(textToLower,"Test"))

#using if, else if (elif) and else

# var_one = 2
# var_two = 2
# if (var_one > var_two):
#     print("var one is greater!")
# else: 
#     print ("var two is greater!")

# if (var_one > var_two):
#     print("VAR ONE IS GREATER!")
# elif (var_one == var_two):
#     print("THEY ARE THE SAME")
# else: 
#     print("They aren't the same")

#FOR LOOPS
#in Javascript....
# num = 5
# for(i = 0; i > 5; i++)

#in Python

# num = 5
# for i in range(num): #default going from 0 to 5, i is the changing value
#     print(i)


# #if I wanted I to start at a different number... 
# for i in range(1,num,2): #default going from 0 to 5, i is the changing value
#     print(i)

# # range(where i starts, condition test, how many steps it's taking)

#There's also lots of stuff you can do with string using in-built pythn functions --> See "Query Things in Strings on class notes"