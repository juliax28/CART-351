from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def default():
    return render_template("base.html")
@app.route("/index")
def index():
    
    passedDictionary={
"fav_color":"fuscia", 
"fav_veg":"cauliflower",
"fav_fruit":"kiwi",
"fav_animal":"toucan"
}
 
    return render_template("index.html", user={"username":"sabine"}, 
                            passedDictionary = passedDictionary)



app.run(debug=True)


