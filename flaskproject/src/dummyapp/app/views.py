from flask import render_template
from systeminfo.main import main
from app import app

@app.route('/')

def index():
 returnDict = {}
 returnDict['user'] = 'COMP30670' # Feel free to put your name here!
 returnDict['title'] = 'Home'
 returnDict['info'] = main()
 return render_template("index.html", **returnDict)
