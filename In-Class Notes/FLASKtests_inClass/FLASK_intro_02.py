#TEMPLATES IN FLASK
#NOTES HTML FILES R MISSING DOCTYPE AND LAN=ENG SO DO THAT BEFORE TESTING AT HOME
# 1 ---IMPORT YOUR FLASK
#W also import the render_template function to use our wonderful pineapple template
from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("Pineapples.html")
#these are awesome because they're DYNAMIC, so we can add stuff whenever, but they gotta be rendered by FLASK
#typing Pineapples.html as the url won't work, this is a security feature, files on the server are private unless the developper decides otherwise. 
# This is done by FLASK, otherwise we'd have to configure all this ourselves!

@app.route("/another")
def another():
    return render_template("Pineapples02.html")
#You CANNOT have the same function leading to two different routes

#BUT what if I got javascript and stuff, like static things? Photos, images, sounds!?
#These are not TEMPLATES, we make a folder called STATIC

#TEMPLATE VARIABLES
#JINJA templating allows u to directly input variable codes from Python to HTML
#from same creators as FLASK
@app.route("/three")
def three():
    #We are going to pass a variable INTO the template
    # We make a KEY VALUE PAIR
    #LEFT is the Key, RIGHT is the template
    #How do we access it inside Pineapples03? INJECTING VARIABLES -- see Pineapples 03
    #"strawberries" should now appear written in the HTML page
    #BUT we can also PASS A LIST and a DICTIONARY and so much MORE
    someNewVar = "strawberries"
    someNewList = ["cat", "dog", "mouse"]
    someDict = {"color":"yellow", "feature":"spiky","taste":"delicious"}
    return render_template("Pineapples03.html", someHTMLVar = someNewVar, someHTMLList = someNewList, someHTMLDict = someDict)


#you can EVEN have FOR LOOPS in JINJA





app.run(debug=True)
 