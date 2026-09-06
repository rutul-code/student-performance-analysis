# Student Performance Analysis

## 📊 Project Overview

This project analyzes student academic performance using Python and the UCI Student Performance dataset.

The goal is to explore how different student, family, and school-related factors are associated with final academic performance.

The project uses data analysis and visualization techniques to identify patterns and relationships in student performance.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
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

## 📈 Key Findings

- The average final grade was **10.42 out of 20**.
- Students with fewer previous failures generally had higher average final grades.
- The second-period grade showed a **very strong relationship** with the final grade.
- Study time showed differences in average final grades across groups.
- Students with internet access had a higher average final grade than students without internet access.
- Students who intended to pursue higher education had a higher average final grade.
- Absences showed very little linear correlation with final grade in this dataset.
- Age showed a weak negative correlation with final grade.

> **Note:** These findings describe relationships observed in the dataset and should not be interpreted as proof of causation.

## 📊 Visualizations

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
│   ├── mother_education_vs_final_grade.png
│   ├── fathers_education_vs_final_grade.png
│   ├── school_support_vs_final_grade.png
│   ├── family_support_vs_final_grade.png
│   ├── higher_education_vs_final_grade.png
│   ├── second_period_vs_final_grade.png
│   ├── absences_vs_final_grade.png
│   └── age_vs_final_grade.png
│
├── main.py
├── README.md
└── requirements.txt