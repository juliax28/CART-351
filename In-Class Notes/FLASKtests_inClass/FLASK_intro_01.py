

from flask import Flask
#convention to name 
app = Flask(__name__)
#anytime you see a word with __ __ on tierh side, it is a variable defined by python. 
# In this case it is a preset variable used iwthin the module in which its used. 
# Its Settign the home name, the route of you porject is "here".

#next we will have a funciton that will run wehn you use the default FLASK route
@app.route("/")
def index():
    return'<h1> I love coding <h1>'
#This will return an HTML strip
#we are defining what will happen, what the default route of the web server will be.

#app is a FLASk objct abd we are using the route function to show where it goes. 
# Think of this as en 'event', IF deault path is called, what will run automatically?


#What happens in python --- pythin takes index, adds extra functonality to that function, and returns it with more functionality.
# @.route DECORATED it, meaning it ADDED the extra functionality as something called a DECORATOR
#A decorator function adds a bunch fo extra functionality to your own function basically
@app.route("/about") # you can define your own routes HOWEVER you like. we are just using /about for convenience
def about():
    return'<h1 style = color:purple"> About CART 351 </h1>'

@app.route("/user/<name>")
def user_profile(name):
    return f"<h2> This is <span style = 'color: orange'>{name}'s></span> profile page </h2>"
#dynamic routing, basically creates a variable using <> within the routed URL in order for it tos tand in for every user on the webpage, 
#instead of having a separate user URL variable per each person

#FLASK DEBUG MODE!
#How do you do that, interact with errors in yur actual browser?

#faulty route
@app.route("/another/<dynamicVar>")
def another_route(dynamicVar):
    return f"<h2> This is the 100th letter SPOILER it doesnt exist <span style = 'color: orange'>{dynamicVar[99]}'s></span> profile page </h2>"
#in the terminal it says already 'string index out of range", but sometimes there are more complex issues.
#We can't tell also by just looking at the web server, looks like it just crashed!
#So let's get some debug info
#Console on google will only show frontend errors - this is a backend error! USELESS
#also not javascript

#DEBUG MODE
#in debug mode --- 
#app.run(debug=true)
#debugger active ill appear in the terminal and you will get a debugger PIN as a security feature.
#You will now see in the browser more information, and you can use your PIN to open the interactive console in the browser.
#Good practice to keep debugging (and turning it off) as you're developing




app.run()