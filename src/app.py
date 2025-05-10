from flask import Flask, render_template, request
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler


app = Flask(__name__)
with open('random_forest_classifier.pkl', 'rb') as f:
    rfc_pkl = pickle.load(f)

def predict_sepsis(HR, O2Sat, Temp, SBP, MAP, DBP, Resp, Glucose, Age, Gender, HospAdmTime, ICULOS):

    # One-hot encode gender
    gender_female = 1 if Gender == "Female" else 0
    gender_male = 1 if Gender == "Male" else 0

    # Create inputs for each classifier
    inputs_array = np.array([float(HR), float(O2Sat), float(Temp), float(SBP), float(MAP), float(DBP), float(Resp), float(Glucose), float(Age), float(HospAdmTime), float(ICULOS), gender_female, gender_male])

    # Standardize numeric features
    df = pd.DataFrame(inputs_array[:-2], columns=['Original'])
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df)

    # Concatenate scaled data with the last two values
    final_data = np.concatenate((scaled_data, inputs_array[-2:].reshape(2, 1)), axis=0).reshape(1, -1)

    # Make predictions using the trained classifier
    probability = rfc_pkl.predict_proba(final_data)[0]

    # Adjusting the weight for sepsis
    weight_factor = 0.5 / 0.15

    # Adjusting probabilities
    non_sepsis_prob = probability[0]
    sepsis_prob = probability[1] * weight_factor

    # Normalizing probabilities
    total_prob = non_sepsis_prob + sepsis_prob
    normalized_non_sepsis_prob = non_sepsis_prob / total_prob
    normalized_sepsis_prob = sepsis_prob / total_prob

    results = {
        'Non-Sepsis': normalized_non_sepsis_prob,
        'Sepsis': normalized_sepsis_prob
    }


    return results



@app.route('/')

def home():
    return render_template('home.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':

        HR = float(request.form['HR'])
        O2Sat = float(request.form['O2Sat'])
        Temp = float(request.form['Temp'])
        SBP = float(request.form['SBP'])
        MAP = float(request.form['MAP'])
        DBP = float(request.form['DBP'])
        Resp = float(request.form['Resp'])
        Glucose = float(request.form['Glucose'])
        Age = float(request.form['Age'])
        Gender = request.form['Gender']
        HospAdmTime = float(request.form['HospAdmTime'])
        ICULOS = float(request.form['ICULOS'])

        model_prediction = predict_sepsis(HR, O2Sat, Temp, SBP, MAP, DBP, Resp, Glucose, Age, Gender, HospAdmTime, ICULOS)

    return render_template('predict.html',prediction = model_prediction)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)