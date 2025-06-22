F1 Race Outcome Predictor with What-If Analysis

A web application that predicts Formula 1 race outcomes based on driver, track, weather, and starting grid position. It includes interactive What-If Analysis and a visual comparison of predictions with historical data.

Features:
1.Select driver, track, weather condition, and grid position.
2.Predict expected race ranking using a trained regression model.
3.Instantly adjust inputs to perform What-If Analysis.
4.Clean, responsive user interface using Bootstrap.

Tech Stack:
Backend: Python, Flask
Machine Learning: Scikit-learn
Data Processing: Pandas, NumPy
Charts: Plotly
Frontend: HTML, CSS (Bootstrap), JavaScript (AJAX)

How to Run Locally:

Clone the repository:
git clone https://github.com/arushijaiswal/Formula1RacePredictor.git
cd Formula1RacePredictor

Create a virtual environment:
python -m venv venv

Activate the virtual environment
# For PowerShell:
.\venv\Scripts\Activate.ps1

# Or for Command Prompt:
venv\Scripts\activate.bat

Install dependencies:
pip install -r requirements.txt
(Or manually: pip install flask pandas scikit-learn numpy plotly joblib)

Train the model:
python model.py

Run the web application:
python app.py

Open in browser:
http://127.0.0.1:5000


Project Structure:
├── app.py
├── model.py
├── data/
│   └── race_results_2015_2025.csv
├── templates/
│   └── index.html
├── static/
│   ├── styles.css
│   └── script.js
├── venv/
└── README.md


Screenshots :
screenshots\webinterface.png
screenshots\outcome.png


Author:
Arushi Jaiswal