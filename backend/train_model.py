import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

import joblib


# 1. Load dataset
df = pd.read_csv("data/dataset.csv")

print("Dataset loaded successfully!")
print("Shape:", df.shape)


# 2. Separate features and target
X = df.drop("Result", axis=1)
y = df["Result"]


print("\nFeatures:", X.shape)
print("Target:", y.shape)


# 3. Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))


# 4. Create ML model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


# 5. Train model
print("\nTraining model...")

model.fit(X_train, y_train)

print("Model training completed!")


# 6. Make predictions
y_pred = model.predict(X_test)


# 7. Check accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:", accuracy)


# 8. Detailed evaluation
print("\nClassification Report:")
print(classification_report(y_test, y_pred))


# 9. Save model
joblib.dump(model, "model/model.pkl")

print("\nModel saved successfully!")
print("Location: model/model.pkl")