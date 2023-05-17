from flask import Flask, jsonify
import joblib
from flask_cors import CORS

app = Flask(__name__)
# enable CORS
CORS(app)

# Load the model
model = joblib.load('finalized_model.sav')

@app.route('/predict/<int:age>/<float:bmi>/<int:smoker>', methods=['GET'])
def predict(age, bmi, smoker):
    # Prepare the feature vector for prediction
    features = [[age, bmi, smoker]]

    # Make a prediction
    prediction = model.predict(features)

    # Prepare the prediction for JSON serialization
    insurance_cost = prediction[0]

    return jsonify(insurance_cost=insurance_cost)

if __name__ == '__main__':
    app.run(debug=True)

