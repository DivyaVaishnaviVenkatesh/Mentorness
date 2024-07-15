from flask import Flask, render_template, request
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib

app = Flask(__name__)

# Load your trained machine learning model
model = joblib.load('Ml-Model/best_model_xgb.pkl')  # Replace with your actual model path

# Routes
@app.route('/')
def index():
    return render_template('index.html')  # Render the form

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from the form
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    gender = request.form['gender']
    doj = request.form['doj']
    current_date = request.form['current_date']
    designation = request.form['designation']
    age = int(request.form['age'])
    unit = request.form['unit']
    leaves_used = int(request.form['leaves_used'])
    leaves_remaining = int(request.form['leaves_remaining'])
    ratings = int(request.form['ratings'])
    past_exp = int(request.form['past_exp'])
    
    # Dummy value for TENURE if not provided from form
    tenure = 0  # Adjust this based on what makes sense in your context

    # Prepare input data for prediction
    input_data = pd.DataFrame({
        'AGE': [age],
  # Add this line for compatibility
        'LEAVES USED': [leaves_used],
        'LEAVES REMAINING': [leaves_remaining],
        'RATINGS': [ratings],
        'PAST EXP': [past_exp],
        'TENURE': [tenure]  # Add this line
    })

    # Predict the salary using your model
    predicted_salary = model.predict(input_data)[0]

    # Render the result page with the predicted salary
    return render_template('result.html', first_name=first_name, last_name=last_name, predicted_salary=predicted_salary)

    # Example: Predict the salary using your model
    predicted_salary = model.predict(input_data)[0]  # Adjust based on how your model predicts salary

    # Render the result page with the predicted salary
    return render_template('result.html', first_name=first_name, last_name=last_name, predicted_salary=predicted_salary)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
