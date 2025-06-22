"""
model.py

This script trains a simple regression model to predict 
F1 race finishing position based on:
- Driver
- Track
- Weather condition
- Starting grid position

It saves the trained model as 'model.pkl' for use by app.py.
"""

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib

# ---------------------------------------------
# 1) Load historical race data
# ---------------------------------------------
# Make sure the path matches your project structure
df = pd.read_csv('data/race_results_2015_2025.csv')

# ---------------------------------------------
# 2) Select features and target
# ---------------------------------------------
# Features:
# - grid_position (numerical)
# - driver, track, weather (categorical)
# Target:
# - finishing_position (numerical)
features = ['grid_position', 'driver', 'track', 'weather']
target = 'finishing_position'

X = df[features]
y = df[target]

# ---------------------------------------------
# 3) One-hot encode categorical features
# ---------------------------------------------
# Convert driver, track, weather to dummy variables
X_encoded = pd.get_dummies(X)

# ---------------------------------------------
# 4) Split into training and test sets (optional)
# ---------------------------------------------
# For demonstration, training on entire data is fine
# But you can uncomment below to split:
# X_train, X_test, y_train, y_test = train_test_split(
#     X_encoded, y, test_size=0.2, random_state=42
# )

# ---------------------------------------------
# 5) Train a simple Linear Regression model
# ---------------------------------------------
model = LinearRegression()
model.fit(X_encoded, y)

# ---------------------------------------------
# 6) Save the trained model as 'model.pkl'
# ---------------------------------------------
joblib.dump(model, 'model.pkl')

print("✅ Model trained and saved as 'model.pkl'.")
print(f"✅ Model uses features: {model.feature_names_in_}")
