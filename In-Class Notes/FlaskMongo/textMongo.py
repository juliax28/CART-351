#we start with connecting to the database
#we have to svae and load our environment variabkles from a .env varibale
from dotenv import load_dotenv
import os
from flask import Flask,render_template,request,redirect, url_for,session
# use flask_pymongo instead of  normal pymongo (simplifies integration)
from flask_pymongo import PyMongo
load_dotenv()  # Load variables from .env and .flaskenv
db_user = os.getenv('MONGODB_USER')
db_pass = os.getenv('DATABASE_PASSWORD')
db_name = os.getenv('DATABASE_NAME')

app = Flask(__name__)
app.secret_key = 'BAD_SECRET_KEY'
# set a config var
# uri = f"mongodb+srv://{db_user}:<{db_pass}>@cluster0.clsm9nu.mongodb.net/?appName=Cluster0"
uri = f"mongodb+srv://{db_user}:{db_pass}@cluster0.clsm9nu.mongodb.net/{db_name}?retryWrites=true&w=majority"
app.config["MONGO_URI"] = uri
mongo = PyMongo(app)
# try:
#     #get details of the client
#     print (mongo.cx)
#     print("You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)

db_name = os.getenv('DATABASE_NAME')
# try:
#     #get details of the client
#     # print (mongo.cx)
#     # #get db
#     # print (mongo.db)
#     # #get collection
#     # print (mongo.db.plantRepo)
#     # print("You successfully connected to MongoDB!")
#     result = mongo.db.plantRepo.insert_one({"testKeyMon":"testValueMon"})
#     print(result)
# except Exception as e:
#     print(e)



#saving data to a databse you need a SCHEMA
#how amny users, databases, etc,. do nyou need?
#for now we are working with only one collection, but you can ahve very complex relationships between your data if you want
#at the abse level, scheme is a collection with a record/document per each plant item
#need minimum name of each item, but we also want all tne data that we input in HTML., including geo location, birthdya, decription
#we also have the issue with the image - we don't recomment saving binary data into Mongo, you can save a BLOB into mongo, but that'ts a large amount of DATA - GETS HEAVY
#therefore, we will upload images to our web0server folder, and the name of the image will be stored in the databse instead

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/insertTestPage')
def insertTest():
    session.pop('ids', default=None)
    return render_template("testInsert.html")

# a route
@app.route('/insertMany')
def insertMany():
    data = [
{'owner_name': 'Sarah',
'plant_name' : 'Snake Plant',
'birthDate':'2002-06-12',
'geoLoc': 'Montreal',
'descript': 'Description for the plant',
'imagePath': 'images/one.png'
},
{
'owner_name': 'Sarah',
'plant_name' :'Cactus',
'birthDate' :'2005-06-13',
'geoLoc':'Toronto',
'descript':'Description for the plant',
'imagePath': 'images/seven.png'
},
 
 {
'owner_name': 'Sarah',
'plant_name' : 'Agapanthus',
'birthDate': '2003-03-19',
'geoLoc': 'Halifax',
'descript': 'Description for the plant',
'imagePath': 'images/seventeen.png'
},
 {
'owner_name': 'Stephen',
'plant_name' : 'Baby Rubber Plant',
'birthDate ': '1999-07-18',
'geoLoc': 'Edinborough',
'descript':'Description for the plant',
'imagePath': 'images/ten.png'
},
 
{
'owner_name': 'Stephen',
'plant_name' : 'Dahlia',
'birthDate' :'2000-05-06',
'geoLoc':'London',
'descript':'Description for the plant',
'imagePath': 'images/thirteen.png'
},
 
{
'owner_name' : 'Harold',
'plant_name' : 'Daphne',
'birthDate': '2012-10-21',
'geoLoc':'New York',
'descript':'Description for the plant',
'imagePath': 'images/three.png'
},
{
'owner_name' : 'Martha',
'plant_name' : 'Daylily',
'birthDate' :'2017-08-21',
'geoLoc':'Paris',
'descript':'Description for the plant',
'imagePath': 'images/nine.png'
}
]
    try:
        # insert many works :)
        result = mongo.db.plantRepo.insert_many(data)
        session['ids'] = result.inserted_ids
        return redirect(url_for('testIds'))
    except Exception as e:
        print(e)

@app.route('/testIds')
def testIds():
    print(session['ids'])
    return render_template("testIds.html")

# a route
@app.route('/viewResults')
def viewResults():
    # result = mongo.db.plantRepo.find_one({})
    # find somthing with the key POINTS and "$gt" means GREATER THAN 5
    result = mongo.db.plantRepo.find({'points':{'$gt':5}})
    return render_template("viewResults.html",result=result)
    print(result)


@app.route('/updateOne')
 def updateOne():
     try:
        updatedRepoItem= mongo.db.plantRepo.find_one_and_update(
            {'plant_name' :'Agapanthus'},
            {'$set':{'descript':'a more precise description'}}
            )
        return redirect(url_for("insertTest"))
     except Exception as e:
        print(e)

@app.route('/updatePoints')
def updatePoints():
     try:
        updatedRepoItem= mongo.db.plantRepo.find_one_and_update(
            {'user' :'maria'},
            {'$inc':{'points':2}}
            )
        return redirect(url_for("insertTest"))
     except Exception as e:
        print(e)



@app.route('/updateMany')
def updateMany():
     try:
        updatedRepoItem= mongo.db.plantRepo.update_many(
            {'owner_name' :'Sarah'},
            {'$set':{'descript':'a more precise description for all sarahs','title':'testALL'}}
            )
        return redirect(url_for("insertTest"))
     except Exception as e:
        print(e)
app.run(debug = True)