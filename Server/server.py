from flask import Flask, request, jsonify
from flask import render_template
from flask_cors import CORS 
from flask import request
import util 

import pickle
# from model_files
app = Flask(__name__,template_folder='../templates',static_folder='../static')
CORS(app)
@app.route('/get_location_names',methods=['GET'])
def get_locations_names():
    response = jsonify({
        'locations':util.get_location_names()
        })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location,total_sqft,bhk,bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response 


@app.route('/')
def hell_world():
    return render_template("app.html")
if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()
