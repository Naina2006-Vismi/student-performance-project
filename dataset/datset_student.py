import kagglehub
import os
import pandas as pd
import numpy as np

# -----------------------------
# STEP 1: Download Dataset
# -----------------------------
path = kagglehub.dataset_download("devansodariya/student-performance-data")
print("Dataset downloaded at:", path)

# -----------------------------
# STEP 2: Find CSV File
# -----------------------------
files = os.listdir(path)
print("Files in dataset:", files)

# Automatically pick first CSV file
csv_file = [f for f in files if f.endswith(".csv")][0]
file_path = os.path.join(path, csv_file)

print("Using file:", csv_file)

# -----------------------------
# STEP 3: Load Dataset
# -----------------------------
df = pd.read_csv(file_path)

print("\nInitial Data Preview:")
print(df.head())

# -----------------------------
# STEP 4: Select Required Columns
# Using actual column names from the dataset
# G1 = Period Grade 1, G2 = Period Grade 2, G3 = Final Grade
# absences = Attendance, studytime = Study Time
# -----------------------------
df = df[
    [
        'absences',      # Attendance
        'studytime',     # Study Hours
        'G2',            # Previous Marks (Period Grade 2)
        'G3'             # Final Marks (Period Grade 3)
    ]
]

# Rename columns for clarity
df.columns = [
    'attendance',
    'study_hours',
    'previous_marks',
    'final_marks'
]

print("\nSelected columns: attendance, study_hours, previous_marks, final_marks")

# -----------------------------
# STEP 5: Handle Missing Values
# -----------------------------
df.fillna(df.mean(), inplace=True)

# -----------------------------
# STEP 6: Remove Invalid Values
# -----------------------------
df = df[
    (df['attendance'] >= 0) & (df['attendance'] <= 100) &
    (df['study_hours'] >= 0) & (df['study_hours'] <= 12) &
    (df['final_marks'] >= 0) & (df['final_marks'] <= 100)
]

# -----------------------------
# STEP 7: Final Clean Dataset Check
# -----------------------------
print("\nCleaned Data Preview:")
print(df.head())

print("\nDataset Shape After Cleaning:", df.shape)

# -----------------------------
# STEP 8: Save Cleaned Dataset
# -----------------------------
cleaned_path = "cleaned_student_performance.csv"
df.to_csv(cleaned_path, index=False)

print("\nCleaned dataset saved as:", cleaned_path)