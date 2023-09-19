from flask import Flask,render_template,request,jsonify,redirect, url_for
import pickle
import pandas as pd
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
model = pickle.load(open('used_car_price_model.pickle','rb'))
@app.route('/',methods=['GET'])

@app.route('/')
def home():
   return render_template('home.html')
   

@app.route('/index')
def index():
   return render_template('index.html')


@app.route('/about')
def about():
   return render_template('about.html')

@app.route('/card')
def card():
   return render_template('card.html')

standard_to = StandardScaler()
@app.route("/predict", methods=['POST','GET'])
def predict():
    Fuel_Type_Diesel=0
    if request.method == 'POST':
        Year = int(request.form['year'])
        Transmission_Mannual=request.form['transmission']
        Fuel_Type=request.form['fuel']
        Owner=int(request.form['owner'])
        if (request.form['km_driven']==''):
           Kms_Driven=int('0')
        else:
            Kms_Driven=int(request.form['km_driven'])
        
        in_put = [Year, Transmission_Mannual, Fuel_Type, Owner, Kms_Driven]
        prediction=model.predict([in_put])
        output=round(prediction[0],2)

        if output<0:
            return jsonify({'prediction_text':"Sorry you cannot sell this car"})
        else:
            return jsonify({'prediction_text':str(output)})

    else:
        return render_template('index.html')
 
if __name__ == '__main__':
  
   app.run(debug=True, port = 3050)