# Student Performance Analysis

## 📊 Project Overview

This project analyzes student performance using Python and the UCI Student Performance dataset.

The goal is to explore how different factors such as study time, previous failures, internet access, parental education, and other student-related factors are associated with final academic performance.

The analysis is performed using Python, Pandas, NumPy, and Matplotlib.

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
- Period grades
- Final grade

The dataset contains **395 student records and 33 columns** for the mathematics dataset used in this project.

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
- Second-period grade showed a very strong relationship with final grade.
- Study time showed some variation in average final grades across groups.
- Students with internet access had a higher average final grade than students without internet access.
- Students who intended to pursue higher education had a higher average final grade.
- Absences showed very little linear correlation with final grade in this dataset.
- Age showed a weak negative correlation with final grade.

## 📂 Project Structure

```text
student-performance-analysis/
│
├── data/
│   └── student-mat.csv
│
├── visualizations/
│
├── main.py
│
└── README.md