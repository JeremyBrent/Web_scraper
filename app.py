from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scraper

# Create an instance of Flask
app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
# Use PyMongo to establish Mongo connection
mongo = PyMongo(app)


@app.route("/")
def home():

    # Find one record of data from the mongo database
    mars = mongo.db.mars.find_one()
    # try: 
    #     hemispheres = mars.get("hemispheres",[])
    # except:
    #     hemispheres = []
    # Return template and data
    return render_template("index.html", mars=mars)

@app.route("/scrape")
def scrape():
    mars_data = scraper.scrape()

    # Update the Mongo database using update and upsert=True
    mongo.db.mars.update({}, mars_data, upsert=True)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
