# Student Performance Project - Execution Plan

## Execution Order (Step by Step)

### Step 1: Install Dependencies
```bash
pip install -r screenshots/requirements.txt
```

### Step 2: Download and Prepare Dataset
```bash
python dataset/datset_student.py
```
This will:
- Download student performance data from Kaggle
- Clean and process the data
- Save as `cleaned_student_performance.csv`

### Step 3: Run Exploratory Data Analysis
```bash
python screenshots/eda_visualization
```
This will:
- Generate correlation heatmap
- Generate actual vs predicted plot
- Save visualizations to `screenshots/` folder

### Step 4: Compare Models
```bash
python screenshots/model_comparision.py
```
This will:
- Train 3 different models (Linear Regression, Decision Tree, Random Forest)
- Compare their performance (MAE and R² scores)

### Step 5: Launch Streamlit Application
```bash
streamlit run screenshots/streamlit_app.py
```
This will:
- Start the interactive web application
- Allow students to predict their performance based on inputs

## Expected Outputs
- `cleaned_student_performance.csv` - Cleaned dataset
- `screenshots/correlation_heatmap.png` - Feature correlation visualization
- `screenshots/actual_vs_predicted.png` - Model prediction accuracy visualization
- Streamlit web app running at http://localhost:8501

