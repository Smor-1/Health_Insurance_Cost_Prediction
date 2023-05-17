from flask import Flask, jsonify, request
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app, supports_credentials=True)

# Load the model
model = joblib.load('testRF_model.sav')

@app.route('/predict', methods=['POST', 'OPTIONS'])
def predict():
    if request.method == 'OPTIONS':
        return {}
    else:
        # Read the data from the JSON body of the request
        data = request.get_json()
        age = data['age']
        bmi = data['bmi']
        smoker = data['smoker']
        # Prepare the feature vector for prediction
        features = [[age, bmi, smoker]]
        # Make a prediction
        prediction = model.predict(features)
        # Prepare the prediction for JSON serialization
        insurance_cost = prediction[0]
        response = jsonify(insurance_cost=insurance_cost)
        return response

if __name__ == '__main__':
    app.run(debug=True, port=5001)
