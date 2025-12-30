import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# -----------------------------
# Load Cleaned Dataset
# -----------------------------
df = pd.read_csv("dataset/cleaned_student_performance.csv")

# -----------------------------
# Features & Target
# -----------------------------
X = df[['attendance', 'study_hours', 'previous_marks']]
y = df['final_marks']

# -----------------------------
# Train-Test Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------------
# Train Model
# -----------------------------
model = LinearRegression()
model.fit(X_train, y_train)

# -----------------------------
# Evaluate Model
# -----------------------------
predictions = model.predict(X_test)

print("MAE:", mean_absolute_error(y_test, predictions))
print("R² Score:", r2_score(y_test, predictions))

# -----------------------------
# Save Model
# -----------------------------
with open("student_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model saved as student_model.pkl")