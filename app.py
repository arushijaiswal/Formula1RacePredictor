"""
app.py

Flask web application for predicting F1 race outcomes
based on driver, track, weather, and starting grid position.

Features:
- Loads a trained regression model (model.pkl)
- Uses user input from a form to make a prediction
- Compares predicted result with historical average
- Displays an interactive bar chart for comparison
"""

from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
import plotly.graph_objs as go
import plotly.io as pio
import joblib  # for loading the saved model

# -------------------------------------
# Initialize Flask app
# -------------------------------------
app = Flask(__name__)

# -------------------------------------
# Load the trained regression model
# -------------------------------------
# The model is trained and saved using model.py
model = joblib.load('model.pkl')

# -------------------------------------
# Load historical race data
# Used to:
#  - Provide dropdown options for drivers, tracks, weather
#  - Calculate historical average for each driver
# -------------------------------------
df = pd.read_csv('data/race_results_2015_2025.csv')

# Extract unique drivers, tracks, weather conditions
drivers = sorted(df['driver'].unique())
tracks = sorted(df['track'].unique())
weathers = sorted(df['weather'].unique())

# -------------------------------------
# Route: Home Page
# Renders the index.html template with dropdown options
# -------------------------------------
@app.route('/')
def index():
    return render_template(
        'index.html',
        drivers=drivers,
        tracks=tracks,
        weathers=weathers
    )

# -------------------------------------
# Route: Predict
# Handles POST requests from the form
# Processes user input, encodes features,
# calls the trained model, generates a comparison chart,
# and returns the prediction + chart as JSON.
# -------------------------------------
@app.route('/predict', methods=['POST'])
def predict():
    # -------------------------------------
    # 1) Retrieve user inputs from the form
    # -------------------------------------
    driver = request.form['driver']
    track = request.form['track']
    weather = request.form['weather']
    grid_position = int(request.form['grid_position'])

    # -------------------------------------
    # 2) Prepare a single-row DataFrame 
    # exactly like your training data
    # -------------------------------------
    input_df = pd.DataFrame({
        'grid_position': [grid_position],
        'driver': [driver],
        'track': [track],
        'weather': [weather]
    })

    # -------------------------------------
    # 3) One-hot encode the input 
    # to match the training features
    # -------------------------------------
    input_encoded = pd.get_dummies(input_df)

    # The model expects the exact same columns,
    # so we add any missing columns with zeros
    for col in model.feature_names_in_:
        if col not in input_encoded.columns:
            input_encoded[col] = 0

    # Ensure columns are in the same order
    input_encoded = input_encoded[model.feature_names_in_]

    # -------------------------------------
    # 4) Make a prediction using the trained model
    # -------------------------------------
    predicted_position = model.predict(input_encoded)[0]

    # -------------------------------------
    # 5) Calculate this driver's historical average position
    # -------------------------------------
    historical_avg = df[df['driver'] == driver]['finishing_position'].mean()

    # -------------------------------------
    # 6) Create an interactive bar chart with Plotly
    # - Bar 1: Predicted Position
    # - Bar 2: Historical Average
    # -------------------------------------
    chart = go.Figure(data=[
        go.Bar(
            name='Predicted Position',
            x=['Position'],
            y=[predicted_position],
            marker_color='blue'
        ),
        go.Bar(
            name='Historical Average',
            x=['Position'],
            y=[historical_avg],
            marker_color='orange'
        )
    ])

    chart.update_layout(
        title=f"{driver}: Predicted vs Historical Average",
        barmode='group',
        yaxis_title='Finishing Position',
        xaxis_title='Metric',
        legend_title='Result'
    )

    # Convert the Plotly chart to HTML (for embedding)
    chart_html = pio.to_html(chart, full_html=False)

    # -------------------------------------
    # 7) Return the prediction and chart as JSON
    # This is handled by the JS in index.html
    # -------------------------------------
    return jsonify({
        'prediction': round(predicted_position, 2),
        'chart': chart_html
    })

# -------------------------------------
# Entry point: run the Flask server
# -------------------------------------
if __name__ == '__main__':
    # debug=True is helpful during development;
    # turn this off for production deployment.
    app.run(debug=True)
