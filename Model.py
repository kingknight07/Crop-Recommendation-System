# Required libraries
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report
from sklearn.impute import SimpleImputer

# Loading Dataset
train_data = pd.read_csv('train.csv')
test_data = pd.read_csv('test.csv')

# Drop the unwanted column
train_data = train_data.drop(columns=['Unnamed: 0'], errors='ignore')
test_data = test_data.drop(columns=['Unnamed: 0'], errors='ignore')

# Dividing Dataset into input labels i.e X and output label i.e y 
X_train = train_data[['N', 'P', 'K', 'pH', 'rainfall', 'temperature']]
y_train = train_data['Crop']

X_test = test_data[['N', 'P', 'K', 'pH', 'rainfall', 'temperature']]
y_test = test_data['Crop']

# Handling missing values  using SimpleImputer
imputer = SimpleImputer(strategy='mean')
X_train = imputer.fit_transform(X_train)
X_test = imputer.transform(X_test)

# Encoded with the target variable 'Crop' using LabelEncoder
le = LabelEncoder()
y_train = le.fit_transform(y_train)
y_test = le.transform(y_test)

#  Training the Model with RFC
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Predicting
y_pred = rf_model.predict(X_test)

# Evaluation of the model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f"Accuracy: {accuracy * 100:.2f}%")
print("Classification Report:\n", report)
