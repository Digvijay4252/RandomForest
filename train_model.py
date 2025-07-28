import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load data
data = pd.read_csv('student_performance.csv')

# Encode Pass column
pass_names = data['Pass'].unique()
pass_map = {name: i for i, name in enumerate(pass_names)}
data['Pass_encoded'] = data['Pass'].map(pass_map)

# Select features and label
X = data[['Hours_Studied', 'Attendance', 'Assignments_Completed', 'Sleep_Hours']]
y = data['Pass_encoded']

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save model and mapping
joblib.dump(model, 'model.pkl')
joblib.dump(pass_map, 'pass_map.pkl')

print('Model and mapping saved successfully.')
