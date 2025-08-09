# Random Forest Classifier Web App

A Flask-based web application that uses a trained Machine Learning model to predict whether a student will pass or fail based on their performance data. This repository demonstrates the implementation of a Random Forest Classifier using Flask and scikit-learn.


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
    └── index.html            # HTML interface for user input


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

### Step 1
<img width="1887" height="906" alt="image" src="https://github.com/user-attachments/assets/f1aad809-6629-4efe-a6b7-23945153b0d7" />

### Step 2 
<img width="1893" height="911" alt="image" src="https://github.com/user-attachments/assets/31f1a9bd-b00f-4fbd-b9e3-9c0bedc101f6" />

### Step 3
<img width="1888" height="907" alt="image" src="https://github.com/user-attachments/assets/27fc4561-81a1-4d9f-a245-1c266529bf59" />


## Future Improvements

Display prediction probabilities

Add support for batch prediction via file upload

Export model performance metrics (accuracy, F1-score)

Host the app on Render/Heroku for public access
