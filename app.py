import pickle
from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)


# @app.route('/u')
# def hello_world():  # put application's code here
#     data = request.args.get('x')
#     return data

# m=pickle.load(open(""))


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predictdata",methods=['GET','POST'])
def predict_datapoint():
    if request=="POST":
        # get all the data entered by the user on the website
        temperature=float(request.form.get('Temperature'))  #temperature is the name inside the form tag inn home.html file
        #take more inputs and gives  the  prediction
        #prediction is then displayed on home.html
        #result is the predicted  value in list form
        return render_templlate('home.html',result=result[0])
        # take {{result}} in home.html file
    else :
        return render_template("home.html")


if __name__ == '__main__':
    app.run(host="0.0.0.0")   #it maps the ip to wherever this app is  running
