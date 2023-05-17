from flask import Flask, jsonify
import joblib
from flask_cors import CORS

app = Flask(__name__)
# enable CORS
CORS(app)

# Load the model
model = joblib.load('finalized_model.sav')

@app.route('/predict', methods=['POST', 'OPTIONS'])
def predict():
    #test
    response = jsonify(message='Hello, CORS is enabled!')
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
    return response

    # OG code
   #if request.method == 'OPTIONS':
   #    # CORS preflight
   #    response = jsonify()
   #else:
   #    # Read the data from the JSON body of the request
   #    data = request.get_json()
   #    age = data['age']
   #    bmi = data['bmi']
   #    smoker = data['smoker']
   #    # Prepare the feature vector for prediction
   #    features = [[age, bmi, smoker]]

   #    # Make a prediction
   #    prediction = model.predict(features)

   #    # Prepare the prediction for JSON serialization
   #    insurance_cost = prediction[0]

   #    # CORS headers
   #    response = jsonify(insurance_cost=insurance_cost)
   #    response.headers.add('Access-Control-Allow-Origin', '*')
   #    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
   #    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')

   #    return response

   #    #return jsonify(insurance_cost=insurance_cost)

if __name__ == '__main__':
    app.run(debug=True, port=5500)
