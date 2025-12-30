# 🎓 Student Performance Prediction App

A machine learning web application that predicts student final marks based on attendance, study hours, and previous exam performance. Built with Python, Streamlit, and scikit-learn.

![Streamlit App](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)

---

## 🌟 Features

- **Interactive Predictions**: Input student metrics and get instant predictions
- **Multiple Models**: Compare Linear Regression, Decision Tree, and Random Forest
- **Visual Insights**: See actual vs predicted performance scatter plots
- **Smart Recommendations**: Get feedback on attendance and study hours

---

## 🚀 Live Demo

**[Student Performance Prediction App](https://student-performance-project.streamlit.app)**

---

## 📁 Project Structure

```
student-performance-project/
├── dataset/
│   ├── datset_student.py          # Dataset download & cleaning script
│   └── cleaned_student_performance.csv  # Clean dataset (395 records)
├── screenshots/
│   ├── streamlit_app.py           # Main Streamlit web application
│   ├── model_comparision.py       # ML model comparison script
│   ├── model_training.py          # Model training script
│   ├── eda_visualization          # EDA visualization script
│   ├── requirements.txt           # Python dependencies
│   ├── correlation_heatmap.png    # Feature correlation heatmap
│   └── actual_vs_predicted.png    # Model performance visualization
├── EXPLANATION.md                 # Project execution guide
├── DEPLOY.md                      # Deployment instructions
└── README.md                      # This file
```

---

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/Naina2006-Vismi/student-performance-project.git
cd student-performance-project
```

2. Install dependencies:
```bash
pip install -r screenshots/requirements.txt
```

3. Run the app locally:
```bash
streamlit run screenshots/streamlit_app.py
```

---

## 📊 Model Performance

| Model | MAE | R² Score |
|-------|-----|----------|
| Linear Regression | 1.26 | 0.79 |
| Decision Tree | 1.13 | 0.83 |
| **Random Forest** | **1.12** | **0.84** |

**Best Model**: Random Forest with R² = 0.84

---

## 🎯 How to Use

1. **Select Model**: Choose from Linear Regression, Decision Tree, or Random Forest
2. **Input Metrics**:
   - Current Attendance (%)
   - Daily Study Hours
   - Previous Exam Marks
   - Planned Holidays (classes missed)
3. **Click Predict**: See your predicted final marks
4. **Get Feedback**: Receive recommendations based on your inputs

---

## 📦 Dependencies

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

## 📈 Features Used

| Feature | Description |
|---------|-------------|
| `attendance` | Student attendance percentage (0-100) |
| `study_hours` | Daily study hours (1-10) |
| `previous_marks` | Previous exam marks (0-100) |
| `final_marks` | Target: Final exam marks (0-100) |

---

## 🔧 Deployment

The app is deployed on **Streamlit Cloud**. To deploy your own version:

1. Push code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io/)
3. Connect your GitHub repository
4. Set main file path: `screenshots/streamlit_app.py`
5. Click Deploy!

---

## 📝 Dataset

- Source: [Kaggle - Student Performance Data](https://www.kaggle.com/datasets/devansodariya/student-performance-data)
- Records: 395 students
- Features: 4 (attendance, study_hours, previous_marks, final_marks)

---

## 👨‍💻 Author

**Naina2006-Vismi**

- GitHub: [@Naina2006-Vismi](https://github.com/Naina2006-Vismi)
- Repository: [student-performance-project](https://github.com/Naina2006-Vismi/student-performance-project)

---

## 📄 License

This project is open source and available under the MIT License.

---

## ⭐ Show Your Support

If you found this project helpful, please give it a ⭐ on GitHub!

---

**Built with ❤️ using Python, Streamlit, and Machine Learning**

