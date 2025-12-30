# Deployment Guide for Streamlit Cloud

## Option 1: Deploy via Streamlit Cloud (Recommended)

### Step 1: Push to GitHub
✅ Already completed! Repository: https://github.com/Naina2006-Vismi/student-performance-project

### Step 2: Deploy on Streamlit Cloud
1. Go to https://share.streamlit.io/
2. Click **"New App"**
3. Select your GitHub repository: `Naina2006-Vismi/student-performance-project`
4. Branch: `main`
5. Main file path: `screenshots/streamlit_app.py`
6. Click **"Deploy!"**

### Step 3: Your app will be live at:
```
https://student-performance-project.streamlit.app
```

---

## Option 2: Deploy via Streamlit Community Cloud

1. Login with your GitHub account at https://share.streamlit.io/
2. Click the **"New App"** button
3. Choose your repository from the dropdown
4. Select the branch (main)
5. Specify the main file path: `screenshots/streamlit_app.py`
6. Click **Deploy**

---

## Required Files for Deployment ✅

| File | Status |
|------|--------|
| `screenshots/requirements.txt` | ✅ Included |
| `screenshots/streamlit_app.py` | ✅ Included |
| `dataset/cleaned_student_performance.csv` | ✅ Included |

---

## Dependencies (already in requirements.txt)
```
pandas
numpy
scikit-learn
streamlit
kagglehub
matplotlib
seaborn
```

---

## After Deployment

Your Streamlit app will be accessible at a public URL like:
- `https://student-performance-project.streamlit.app`

You can then share this link with anyone!

---

## Troubleshooting

If deployment fails:
1. Check that `requirements.txt` has all dependencies
2. Ensure the main file path is correct: `screenshots/streamlit_app.py`
3. Make sure the CSV file is in `dataset/` folder

---

## Local Development

To run locally:
```bash
cd student-performance-project
pip install -r screenshots/requirements.txt
streamlit run screenshots/streamlit_app.py
```

