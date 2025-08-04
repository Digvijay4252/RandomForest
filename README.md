## Random Forest Classifier Web App

A Flask-based web application that uses a trained Machine Learning model to identify whether a given email/message is **Spam** or **Not Spam**.This repository demonstrates the implementation of a Random Forest Classifier using Flask and scikit-learn. It allows users to input student performance data via a web form and predicts whether a student will pass or fail based on a trained Random Forest model.

---

## Project Structure

```
RandomForest/
│
├── app.py                    # Flask app to serve predictions
├── train_model.py            # Script to train and save the Random Forest model
├── model.pkl                 # Trained Random Forest model
├── pass_map.pkl              # Label encoder for target classes
├── student_performance.csv   # Dataset used for model training
├── templates/
│   └── index.html            # HTML interface for user input
└── static/
    └── style.css             # Optional CSS for styling

```

---

## Setup Instructions

1. **Clone the repository**

```
git clone https://github.com/Digvijay4252/RandomForest.git
cd RandomForest
```

Install dependencies

```
pip install -r requirements.txt
```

Run the application

```
python app.py
```

Open in browser

Visit: http://localhost:10000


## Screenshots

<img width="1626" height="911" alt="image" src="https://github.com/user-attachments/assets/d6e776de-740e-4363-ab2c-3805040e751a" />


## Future Improvements

Display prediction probabilities

Add support for batch prediction via file upload

Export model performance metrics (accuracy, F1-score)

Host the app on Render/Heroku for public access
