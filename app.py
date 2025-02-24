from flask import Flask, render_template, request, jsonify
import numpy as np
import pickle

app = Flask(__name__)

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


if __name__ == '__main__':
    app.run(debug=True)
