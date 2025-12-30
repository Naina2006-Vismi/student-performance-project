import streamlit as st
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("dataset/cleaned_student_performance.csv")

X = df[['attendance', 'study_hours', 'previous_marks']]
y = df['final_marks']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------------
# Train Models
# -----------------------------
models = {
    "Linear Regression": LinearRegression(),
    "Decision Tree": DecisionTreeRegressor(random_state=42),
    "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42)
}

for model in models.values():
    model.fit(X_train, y_train)

# -----------------------------
# UI Layout
# -----------------------------
st.set_page_config(page_title="Student Academic Planner", layout="centered")

st.title("🎓 Student Performance & Academic Planner")
st.markdown("Plan your **attendance, holidays, and study hours** smartly using AI.")

# -----------------------------
# Model Selection
# -----------------------------
model_name = st.selectbox(
    "Choose Prediction Model",
    list(models.keys())
)

model = models[model_name]

# -----------------------------
# Student Inputs
# -----------------------------
attendance = st.slider("Current Attendance (%)", 50, 100, 75)
study_hours = st.slider("Daily Study Hours", 1, 10, 3)
previous_marks = st.slider("Previous Exam Marks", 0, 100, 70)
planned_holidays = st.slider("Planned Holidays (Classes Missed)", 0, 30, 5)

# -----------------------------
# Attendance Planning Logic
# -----------------------------
TOTAL_CLASSES = 200
new_attendance = (
    (attendance / 100 * TOTAL_CLASSES - planned_holidays)
    / TOTAL_CLASSES
) * 100

new_attendance = max(new_attendance, 0)

# -----------------------------
# Prediction
# -----------------------------
if st.button("📈 Predict Performance"):
    input_data = np.array([[new_attendance, study_hours, previous_marks]])
    prediction = model.predict(input_data)

    st.success(f"Predicted Final Marks: **{prediction[0]:.2f}**")
    st.info(f"Attendance After Holidays: **{new_attendance:.2f}%**")

    # -----------------------------
    # Feedback
    # -----------------------------
    if new_attendance < 75:
        st.warning("⚠️ Attendance below safe limit. Reduce holidays.")
    else:
        st.success("✅ Attendance is safe.")

    if study_hours < 3:
        st.warning("📘 Increase study hours for better results.")

    # -----------------------------
    # Visualization
    # -----------------------------
    st.subheader("📊 Model Insight: Actual vs Predicted")

    test_preds = model.predict(X_test)

    fig, ax = plt.subplots()
    ax.scatter(y_test, test_preds)
    ax.set_xlabel("Actual Marks")
    ax.set_ylabel("Predicted Marks")
    ax.set_title("Actual vs Predicted Marks")

    st.pyplot(fig)