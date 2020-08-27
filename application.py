from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
from flask_session import Session
##ash
import os

app = Flask(__name__)

##ash
templates= os.path.join('static')
app.config['UPLOAD_FOLDER'] = templates

@app.route("/")
def index():
    ## Call principal page
    ##return render_template("index.html")
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'LogoIcono.png')
    return render_template("index.html", user_image = full_filename)



