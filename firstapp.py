# from flask import Flask,render_template
# from flask_scss import Scss
# from flask_sqlalchemy import SQLAlchemy


# app= Flask(__name__)

# @app.route("/")
# def index():
#     return render_template("index.html")

# if __name__ in "__main__":
#     app.run(debug=True)
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)
   

    return render_template('index.html', prediction_text="Credit Risk Prediction:"+"High Risk" if output == 1 else "Low Risk")

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)