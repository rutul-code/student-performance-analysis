import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("=" * 50)
print("       STUDENT PERFORMANCE ANALYSIS")
print("=" * 50)

# Load dataset
df = pd.read_csv("data/student-mat.csv", sep=";")


# Rename columns professionally
df = df.rename(columns={
    "school": "School",
    "sex": "Gender",
    "age": "Age",
    "address": "Address",
    "famsize": "Family_Size",
    "Pstatus": "Parent_Status",
    "Medu": "Mother_Education",
    "Fedu": "Father_Education",
    "Mjob": "Mother_Job",
    "Fjob": "Father_Job",
    "reason": "Reason_for_Choosing_School",
    "guardian": "Guardian",
    "traveltime": "Travel_Time",
    "studytime": "Study_Time",
    "failures": "Previous_Failures",
    "schoolsup": "School_Support",
    "famsup": "Family_Support",
    "paid": "Extra_Paid_Classes",
    "activities": "Extra_Activities",
    "nursery": "Nursery_Attendance",
    "higher": "Higher_Education",
    "internet": "Internet_Access",
    "romantic": "Romantic_Relationship",
    "famrel": "Family_Relationship",
    "freetime": "Free_Time",
    "goout": "Going_Out",
    "Dalc": "Weekday_Alcohol_Consumption",
    "Walc": "Weekend_Alcohol_Consumption",
    "health": "Health_Status",
    "absences": "Absences",
    "G1": "First_Period_Grade",
    "G2": "Second_Period_Grade",
    "G3": "Final_Grade"
})


# Basic dataset information
print("\n--- Data Types ---")
print(df.dtypes)

print("\n--- Missing Values ---")
print(df.isnull().sum())

print("\n--- Statistical Summary ---")
print(df.describe())


# Study time analysis
print("\n--- Study Time Analysis ---")
print("Average Final Grade:", round(df["Final_Grade"].mean(), 2))
print(df.groupby("Study_Time")["Final_Grade"].mean().round(2))

studytime_avg = df.groupby("Study_Time")["Final_Grade"].mean()

studytime_avg.plot(kind="bar")

plt.title("Average Final Grade by Study Time", fontsize=14)
plt.xlabel("Study Time Group")
plt.ylabel("Average Final Grade")
plt.xticks(rotation=0)
plt.grid(axis="y", linestyle="--", alpha=0.5)

for i, value in enumerate(studytime_avg):
    plt.text(i, value + 0.1, f"{value:.2f}", ha="center")

plt.tight_layout()
plt.savefig("visualizations/study_time_vs_final_grade.png", dpi=300)
plt.show()


# Absences correlation analysis
print("\n--- Absences Analysis ---")
print(df[["Absences", "Final_Grade"]].corr().round(2))


# Previous failures analysis
print("\n--- Previous Failures Analysis ---")
print(df.groupby("Previous_Failures")["Final_Grade"].mean().round(2))

failures_avg = df.groupby("Previous_Failures")["Final_Grade"].mean()

failures_avg.plot(kind="bar")

plt.title("Average Final Grade by Previous Failures", fontsize=14)
plt.xlabel("Number of Previous Failures")
plt.ylabel("Average Final Grade")
plt.xticks(rotation=0)
plt.grid(axis="y", linestyle="--", alpha=0.5)

for i, value in enumerate(failures_avg):
    plt.text(i, value + 0.1, f"{value:.2f}", ha="center")

plt.tight_layout()
plt.savefig("visualizations/previous_failures_vs_final_grade.png", dpi=300)
plt.show()

# Gender analysis
print("\n--- Gender Analysis ---")
print(df.groupby("Gender")["Final_Grade"].mean().round(2))

gender_avg = df.groupby("Gender")["Final_Grade"].mean()

gender_avg.plot(kind="bar")

plt.title("Average Final Grade by Gender", fontsize=14)
plt.xlabel("Gender")
plt.ylabel("Average Final Grade")
plt.xticks(rotation=0)
plt.grid(axis="y", linestyle="--", alpha=0.5)

for i, value in enumerate(gender_avg):
    plt.text(i, value + 0.1, f"{value:.2f}", ha="center")

plt.tight_layout()
plt.savefig("visualizations/gender_vs_final_grade.png", dpi=300)
plt.show()


# Internet access analysis
print("\n--- Internet Access Analysis ---")
print(df.groupby("Internet_Access")["Final_Grade"].mean().round(2))

internet_avg = df.groupby("Internet_Access")["Final_Grade"].mean()

internet_avg.plot(kind="bar")

plt.title("Average Final Grade by Internet Access", fontsize=14)
plt.xlabel("Internet Access")
plt.ylabel("Average Final Grade")
plt.xticks(rotation=0)
plt.grid(axis="y", linestyle="--", alpha=0.5)

for i, value in enumerate(internet_avg):
    plt.text(i, value + 0.1, f"{value:.2f}", ha="center")

plt.tight_layout()
plt.savefig("visualizations/internet_access_vs_final_grade.png", dpi=300)
plt.show()


# Mother's education analysis
print("\n--- Mother's Education Analysis ---")
print(df.groupby("Mother_Education")["Final_Grade"].mean().round(2))

medu_avg = df.groupby("Mother_Education")["Final_Grade"].mean()

medu_avg.plot(kind="bar")

plt.title("Average Final Grade by Mother's Education", fontsize=14)
plt.xlabel("Mother's Education Level")
plt.ylabel("Average Final Grade")
plt.xticks(rotation=0)
plt.grid(axis="y", linestyle="--", alpha=0.5)

for i, value in enumerate(medu_avg):
    plt.text(i, value + 0.1, f"{value:.2f}", ha="center")

plt.tight_layout()
plt.savefig("visualizations/mother_education_vs_final_grade.png", dpi=300)
plt.show()


# Father's education analysis
print("\n--- Father's Education Analysis ---")
print(df.groupby("Father_Education")["Final_Grade"].mean().round(2))

fedu_avg = df.groupby("Father_Education")["Final_Grade"].mean()

fedu_avg.plot(kind="bar")

plt.title("Average Final Grade by Father's Education", fontsize=14)
plt.xlabel("Father's Education Level")
plt.ylabel("Average Final Grade")
plt.xticks(rotation=0)
plt.grid(axis="y", linestyle="--", alpha=0.5)

for i, value in enumerate(fedu_avg):
    plt.text(i, value + 0.1, f"{value:.2f}", ha="center")

plt.tight_layout()
plt.savefig("visualizations/fathers_education_vs_final_grade.png", dpi=300)
plt.show()


# School support analysis
print("\n--- School Support Analysis ---")
print(df.groupby("School_Support")["Final_Grade"].mean().round(2))

schoolsup_avg = df.groupby("School_Support")["Final_Grade"].mean()

schoolsup_avg.plot(kind="bar")

plt.title("Average Final Grade by School Support", fontsize=14)
plt.xlabel("School Support")
plt.ylabel("Average Final Grade")
plt.xticks(rotation=0)
plt.grid(axis="y", linestyle="--", alpha=0.5)

for i, value in enumerate(schoolsup_avg):
    plt.text(i, value + 0.1, f"{value:.2f}", ha="center")

plt.tight_layout()
plt.savefig("visualizations/school_support_vs_final_grade.png", dpi=300)
plt.show()


# Family support analysis
print("\n--- Family Support Analysis ---")
print(df.groupby("Family_Support")["Final_Grade"].mean().round(2))

famsup_avg = df.groupby("Family_Support")["Final_Grade"].mean()

famsup_avg.plot(kind="bar")

plt.title("Average Final Grade by Family Support", fontsize=14)
plt.xlabel("Family Support")
plt.ylabel("Average Final Grade")
plt.xticks(rotation=0)
plt.grid(axis="y", linestyle="--", alpha=0.5)

for i, value in enumerate(famsup_avg):
    plt.text(i, value + 0.1, f"{value:.2f}", ha="center")

plt.tight_layout()
plt.savefig("visualizations/family_support_vs_final_grade.png", dpi=300)
plt.show()

# Higher education intention analysis
print("\n--- Higher Education Analysis ---")
print(df.groupby("Higher_Education")["Final_Grade"].mean().round(2))

higher_avg = df.groupby("Higher_Education")["Final_Grade"].mean()

higher_avg.plot(kind="bar")

plt.title("Average Final Grade by Higher Education Intention", fontsize=14)
plt.xlabel("Wants Higher Education")
plt.ylabel("Average Final Grade")
plt.xticks(rotation=0)
plt.grid(axis="y", linestyle="--", alpha=0.5)

for i, value in enumerate(higher_avg):
    plt.text(i, value + 0.1, f"{value:.2f}", ha="center")

plt.tight_layout()
plt.savefig("visualizations/higher_education_vs_final_grade.png", dpi=300)
plt.show()


# First, second and final grade correlation
print("\n--- Grade Correlation Analysis ---")
print(
    df[
        ["First_Period_Grade", "Second_Period_Grade", "Final_Grade"]
    ].corr().round(2)
)


# Second period grade vs final grade
plt.scatter(df["Second_Period_Grade"], df["Final_Grade"])

plt.title("Second Period Grade vs Final Grade", fontsize=14)
plt.xlabel("Second Period Grade")
plt.ylabel("Final Grade")
plt.grid(True, linestyle="--", alpha=0.5)

plt.tight_layout()
plt.savefig("visualizations/second_period_vs_final_grade.png", dpi=300)
plt.show()

# Absences vs final grade
plt.scatter(df["Absences"], df["Final_Grade"])

plt.title("Absences vs Final Grade", fontsize=14)
plt.xlabel("Number of Absences")
plt.ylabel("Final Grade")
plt.grid(True, linestyle="--", alpha=0.5)

plt.tight_layout()
plt.savefig("visualizations/absences_vs_final_grade.png", dpi=300)
plt.show()

# Age vs final grade correlation
print("\n--- Age Analysis ---")
print(df[["Age", "Final_Grade"]].corr().round(2))

age_grade_corr = df[["Age", "Final_Grade"]].corr().iloc[0, 1]

plt.scatter(df["Age"], df["Final_Grade"])

plt.title("Age vs Final Grade", fontsize=14)
plt.xlabel("Age")
plt.ylabel("Final Grade")
plt.grid(True, linestyle="--", alpha=0.5)

plt.tight_layout()
plt.savefig("visualizations/age_vs_final_grade.png", dpi=300)
plt.show()


# Key project metrics
total_students = len(df)
average_grade = df["Final_Grade"].mean()
highest_grade = df["Final_Grade"].max()
lowest_grade = df["Final_Grade"].min()

print("\n--- Key Project Metrics ---")
print("Total Students:", total_students)
print("Average Final Grade:", round(average_grade, 2))
print("Highest Final Grade:", highest_grade)
print("Lowest Final Grade:", lowest_grade)