from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import numpy as np
import pickle

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the trained model
model_path = 'model/sonar_model.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from form
        input_data = request.form['features']
        
        # Convert input data into a list of floats
        input_values = np.array([float(x.strip()) for x in input_data.split(',')]).reshape(1, -1)

        # Ensure exactly 60 features are entered
        if len(input_values[0]) != 60:
            return render_template('index.html', prediction_text="❌ Please enter exactly 60 numerical values.")

        # Predict using the model
        prediction = model.predict(input_values)

        # Display result
        result = "Mine" if prediction[0] == 'M' else "Rock"
        return render_template('index.html', prediction_text=f"🔍 The detected object is: {result}")

    except ValueError:
        return render_template('index.html', prediction_text="❌ Invalid input! Please enter only numbers separated by commas.")

@app.route('/api/predict', methods=['POST'])
def api_predict():
    """JSON API endpoint for Next.js frontend"""
    try:
        # Get JSON data
        data = request.get_json()
        
        if not data or 'features' not in data:
            return jsonify({'error': 'No features provided'}), 400
        
        # Convert input data into a list of floats
        if isinstance(data['features'], str):
            input_values = np.array([float(x.strip()) for x in data['features'].split(',')]).reshape(1, -1)
        elif isinstance(data['features'], list):
            input_values = np.array(data['features']).reshape(1, -1)
        else:
            return jsonify({'error': 'Invalid features format'}), 400

        # Ensure exactly 60 features are entered
        if len(input_values[0]) != 60:
            return jsonify({'error': f'Please enter exactly 60 values. Received {len(input_values[0])} values.'}), 400

        # Predict using the model
        prediction = model.predict(input_values)
        probability = model.predict_proba(input_values) if hasattr(model, 'predict_proba') else None

        # Return result
        result = "Mine" if prediction[0] == 'M' else "Rock"
        
        response = {
            'prediction': result,
            'success': True
        }
        
        if probability is not None:
            response['confidence'] = {
                'rock': float(probability[0][0]) if result == 'Rock' else float(probability[0][1]),
                'mine': float(probability[0][1]) if result == 'Mine' else float(probability[0][0])
            }
        
        return jsonify(response)

    except ValueError as e:
        return jsonify({'error': f'Invalid input: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': f'Prediction failed: {str(e)}'}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)

