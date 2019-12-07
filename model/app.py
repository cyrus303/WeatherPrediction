import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import TempPrediction
import csv

app = Flask(__name__)
model = pickle.load(open('TempPrediction.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index1.html')
#
# @app.route('/predict',methods=['POST'])
# def predict():
#     '''
#     For rendering results on HTML GUI
#     '''
#     int_features = [str(x) for x in request.form.values()]
#     final_features = [np.array(int_features)]
#     prediction = model.predict(final_features)
#     #prediction= TempPrediction(final_features)
#     output = round(prediction[0], 2)
#
#     return render_template('index1.html', prediction_text='Employee Salary should be $ {}'.format(output))

@app.route('/predict',methods=['POST'])
def predict():
    int_features =request.form['interview_score']
    #final_features = [np.array(int_features)]
    #prediction = TempPrediction
    #print("xxxxxxxxxxxxxxxxxxxxxxxxx")
    with open(r'C:/Users/Reddy/Desktop/PROJECT/flas/mout.csv','rt') as f:
        reader = csv.reader(f)
        #print("4444444444444444444444444444444444")
        for row in reader:
            if row[0] == int_features:
                output = row[1]

                return render_template('index1.html', output= output)

    #print("2222222222222222222222222222222222")


    #prediction= TempPrediction(final_features)
    #output = round(prediction[0], 2)
        #return render_template('index.html', prediction_text='Temperature is $ {}'.format(output))


@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = TempPrediction.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)
