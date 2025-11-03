
import json

#how to read and write to files!
#You can read and write to text files - normal characters 
#Each line of text is terminated with a END OF LINE character
# WE will focus on TEXT files



#open file for reading
rainbowFile_r = open("files/rainbow.txt", "r")
#read first 4 bytes (1 char per byte)
out4 = rainbowFile_r.read(4)
print(out4)
#read entire text - but note if we read before... 
# then we will be reading from where we read last...
#and once it has consumed the entire file - you can no longer read...
out_all = rainbowFile_r.read()
print(out_all)
#so to go back to start then - > use the seek function...
rainbowFile_r.seek(0)
out_all_a = rainbowFile_r.read()
print(out_all_a)
#good idea to close it 
rainbowFile_r.close()
#Always a good idea to close the files to limit the memory and resources used, python does this on it's own to a certain point but this is good practice.

rainbowFile = open("files/rainbow.txt", "r")
outline = rainbowFile.readline()
print(outline)

#writing to a file
#If we wanna write toa file, we have to OPEN a file for WRITING, using first a file that already exists

sampleFile = open ("files/sample_text.txt", "w")
# for i in range(30):
#     a_name = input("enter animal: ")
#     #this specifies to make every line a new LINE
#     sampleFile.write("\n")
# sampleFile.close()

# #ANOTHER WAY
# animalList = []
# for i in range(3):
#     a_name = input("enter animal: ")
#     animalList.append(a_name="\n")
#     sampleFile.write(a_name)
#     sampleFile.write("\n")
# sampleFile.writelines(animalList)
# sampleFile.close()

# samplefile = open("files/sample_text.txt","a")
# nameList = []
# for i in range(3)
#     name = inpt("type name")
#     nameList.append(name+"\n")
# sampleFile_a.writeLines(nameList)
# sampleFile_a.close()

# Read from file and parse JSON
# jsonFile = open("files/test.json", "r")
# data = json.load(jsonFile)
# print(data)
# print(type(data)) # a list

#from STRING to DICT
# json_str = '{"name":"Sabs", "fav_col":"red", "fav_city":"montreal"}'
# data_2 = json.loads(json_str) 
# print(data_2)
# print(type(data_2))#converts to a dict

#from DICT to STRING
# data_toSave = {"name":"mandy", "fav_col":"blue", "fav_city":"winnipeg"}
# data_s = json.dumps(data_toSave, indent=4)
# fileToOpen = open("files/new_sample.json", "w")
# fileToOpen.write(data_s)

# data_toSave = {"name":"mandy", "fav_col":"blue", "fav_city":"winnipeg"}
# fileToOpen = open("files/new_sample.json", "w")
# json.dump(dataToSave_2,fileToOpen, indent =4)
# fileToOpen.close()

jsonFile = open("files/new_sample.json", "r+")
data = json.load(jsonFile)
print(data['fav_city'])
print(type(data['fav_city']))
# #go to beginning of file
jsonFile.seek(0)
data['fav_city'].append("another element")
data["newKey"] = 1234
#output to the file
json.dump(data,jsonFile, indent =4)

