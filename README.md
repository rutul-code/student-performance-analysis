# Student Performance Analysis

## 📊 Project Overview

This project analyzes student academic performance using Python and the UCI Student Performance dataset.

The goal is to explore how different student, family, and school-related factors are associated with final academic performance.

The project uses data analysis, visualization, and an interactive Streamlit dashboard to identify patterns and relationships in student performance.

## 🚀 Live Dashboard

Try the interactive Student Performance Analysis dashboard:

👉 **[Open Live Dashboard](https://student-performance-analysis-7nvmad7feyzzwmf23yf8mr.streamlit.app/)**

The deployed dashboard allows users to:

- Filter students by gender
- Filter by age
- Filter by study time
- Filter by final grade
- Explore interactive charts
- Analyze pass/fail performance
- Download filtered student data

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Streamlit
- Git & GitHub

## 📁 Dataset

The dataset used in this project is the **UCI Student Performance Dataset**.

It contains information about students, including:

- Demographic information
- Study time
- Previous failures
- Absences
- Family and school support
- Internet access
- Parental education
- Period grades
- Final grade

The mathematics dataset used in this project contains **395 student records and 33 columns**.

## 🔍 Analysis Performed

The project analyzes student performance using the following factors:

- Study time vs final grade
- Absences vs final grade
- Previous failures vs final grade
- Gender vs final grade
- Internet access vs final grade
- Mother's education vs final grade
- Father's education vs final grade
- School support vs final grade
- Family support vs final grade
- Higher education intention vs final grade
- Age vs final grade
- First, second, and final grade correlations
- Average grade by school
- Grade distribution by gender
- Study time vs previous failures
- Pass/Fail analysis
- Overall pass rate

## 📈 Key Findings

- The average final grade was **10.42 out of 20**.
- Students with fewer previous failures generally had higher average final grades.
- The second-period grade showed a **very strong relationship** with the final grade, with a correlation of approximately **0.90**.
- Study time showed differences in average final grades across groups.
- Students with internet access had a higher average final grade than students without internet access.
- Students who intended to pursue higher education had a higher average final grade.
- Absences showed very little linear correlation with final grade in this dataset.
- Age showed a weak negative correlation with final grade.
- Students from different schools showed differences in average final grades.

> **Note:** These findings describe relationships observed in the dataset and should not be interpreted as proof of causation.

## 📊 Interactive Streamlit Dashboard

The project includes an interactive **Streamlit dashboard** for exploring student performance.

### 🎛️ Dashboard Filters

Users can filter the dataset by:

- Gender
- Age
- Study Time
- Final Grade

The dashboard updates the analysis and key performance indicators based on the selected filters.

### 📌 Dashboard Features

- Key Performance Indicators
- Performance Summary
- Final Grade Distribution
- Average Grade by School
- Pass/Fail Analysis
- Overall Pass Rate
- Correlation Heatmap
- Filtered dataset download

### 📑 Dashboard Tabs

The dashboard is organized into four sections:

1. **📚 Academic Factors**
   - Study Time vs Final Grade
   - Previous Failures vs Final Grade
   - School Support vs Final Grade
   - Average Grade by School
   - Study Time vs Previous Failures

2. **👨‍👩‍👧 Student & Family**
   - Gender vs Final Grade
   - Internet Access vs Final Grade
   - Family Support vs Final Grade
   - Age vs Final Grade
   - Grade Distribution by Gender

3. **🎓 Education**
   - Mother's Education vs Final Grade
   - Father's Education vs Final Grade
   - Higher Education Intention vs Final Grade

4. **📈 Grade Relationships**
   - Second Period Grade vs Final Grade
   - Absences vs Final Grade
   - Correlation Heatmap
   - Pass/Fail Analysis
   - Overall Pass Rate

For this project, students with a final grade of **10 or above** are classified as **Pass**.

## 📈 Visualizations

The project generates visualizations including:

- Average Final Grade by Study Time
- Average Final Grade by Previous Failures
- Average Final Grade by Gender
- Average Final Grade by Internet Access
- Average Final Grade by Mother's Education
- Average Final Grade by Father's Education
- Average Final Grade by School Support
- Average Final Grade by Family Support
- Average Final Grade by Higher Education Intention
- Second Period Grade vs Final Grade
- Absences vs Final Grade
- Age vs Final Grade

All generated charts are stored in the `visualizations/` folder.

## 📂 Project Structure

```text
student-performance-analysis/
│
├── data/
│   └── student-mat.csv
│
├── visualizations/
│   ├── study_time_vs_final_grade.png
│   ├── previous_failures_vs_final_grade.png
│   ├── gender_vs_final_grade.png
│   ├── internet_access_vs_final_grade.png
│   ├── mothers_education_vs_final_grade.png
│   ├── fathers_education_vs_final_grade.png
│   ├── school_support_vs_final_grade.png
│   ├── family_support_vs_final_grade.png
│   ├── higher_education_vs_final_grade.png
│   ├── second_period_grade_vs_final_grade.png
│   ├── absences_vs_final_grade.png
│   └── age_vs_final_grade.png
│
├── main.py
├── dashboard.py
├── README.md
└── requirements.txt