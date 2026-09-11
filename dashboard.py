import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Student Performance Analysis",
    page_icon="📊",
    layout="wide"
)

# ==================================================
# TITLE
# ==================================================

st.title("📊 Student Performance Analysis")

st.write(
    "Interactive dashboard for analyzing student academic performance."
)

st.info(
    "This dashboard explores how study habits, previous failures, "
    "family background, education, and other factors relate to "
    "students' final academic performance."
)

# ==================================================
# LOAD DATA
# ==================================================

df = pd.read_csv(
    "data/student-mat.csv",
    sep=";"
)

# Keep original age range for the slider
min_age = int(df["age"].min())
max_age = int(df["age"].max())

# ==================================================
# SIDEBAR FILTERS
# ==================================================

st.sidebar.header("🎛️ Filters")

# --------------------------------------------------
# Gender Filter
# --------------------------------------------------

gender_filter = st.sidebar.selectbox(
    "Select Gender",
    ["All", "Female", "Male"]
)

if gender_filter == "Female":
    df = df[df["sex"] == "F"]

elif gender_filter == "Male":
    df = df[df["sex"] == "M"]

# --------------------------------------------------
# Age Filter
# --------------------------------------------------

age_filter = st.sidebar.slider(
    "Select Age",
    min_value=min_age,
    max_value=max_age,
    value=(min_age, max_age)
)

df = df[
    (df["age"] >= age_filter[0]) &
    (df["age"] <= age_filter[1])
]

# --------------------------------------------------
# Study Time Filter
# --------------------------------------------------

study_time_filter = st.sidebar.multiselect(
    "Select Study Time",
    options=[1, 2, 3, 4],
    default=[1, 2, 3, 4],
    format_func=lambda x: {
        1: "<2 hours/week",
        2: "2–5 hours/week",
        3: "5–10 hours/week",
        4: ">10 hours/week"
    }[x]
)

df = df[
    df["studytime"].isin(study_time_filter)
]

# --------------------------------------------------
# Final Grade Filter
# --------------------------------------------------

grade_filter = st.sidebar.slider(
    "Select Final Grade",
    min_value=0,
    max_value=20,
    value=(0, 20)
)

df = df[
    (df["G3"] >= grade_filter[0]) &
    (df["G3"] <= grade_filter[1])
]

# ==================================================
# EMPTY DATA CHECK
# ==================================================

if df.empty:
    st.warning("⚠️ No students match the selected filters.")
    st.stop()

# ==================================================
# KEY METRICS
# ==================================================

total_students = len(df)

average_grade = df["G3"].mean()

highest_grade = df["G3"].max()

lowest_grade = df["G3"].min()

# ==================================================
# KPI CARDS
# ==================================================

st.subheader("📌 Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "👨‍🎓 Total Students",
    total_students
)

col2.metric(
    "📊 Average Grade",
    f"{average_grade:.2f}/20"
)

col3.metric(
    "🏆 Highest Grade",
    highest_grade
)

col4.metric(
    "📉 Lowest Grade",
    lowest_grade
)

# ==================================================
# AUTOMATIC INSIGHT
# ==================================================

st.subheader("💡 Dashboard Insight")

if average_grade >= 12:

    st.success(
        f"Students in the current selection have a strong "
        f"average final grade of {average_grade:.2f}/20."
    )

elif average_grade >= 10:

    st.info(
        f"Students in the current selection have an average "
        f"final grade of {average_grade:.2f}/20."
    )

else:

    st.warning(
        f"Students in the current selection have a relatively "
        f"low average final grade of {average_grade:.2f}/20."
    )

# ==================================================
# PERFORMANCE SUMMARY
# ==================================================

st.subheader("🎯 Performance Summary")

high_performers = len(
    df[df["G3"] >= 15]
)

average_performers = len(
    df[
        (df["G3"] >= 10) &
        (df["G3"] < 15)
    ]
)

low_performers = len(
    df[df["G3"] < 10]
)

col1, col2, col3 = st.columns(3)

col1.metric(
    "🟢 High Performers",
    high_performers
)

col2.metric(
    "🟡 Average Performers",
    average_performers
)

col3.metric(
    "🔴 Low Performers",
    low_performers
)

# ==================================================
# FINAL GRADE DISTRIBUTION
# ==================================================

st.subheader("📊 Final Grade Distribution")

grade_bins = pd.cut(
    df["G3"],
    bins=[-1, 4, 9, 14, 20],
    labels=[
        "0–4",
        "5–9",
        "10–14",
        "15–20"
    ]
)

grade_distribution = (
    grade_bins
    .value_counts()
    .sort_index()
)

st.bar_chart(
    grade_distribution
)

# ==================================================
# DOWNLOAD FILTERED DATA
# ==================================================

st.subheader("📥 Download Filtered Data")

csv_data = df.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    label="Download Filtered Dataset",
    data=csv_data,
    file_name="filtered_student_data.csv",
    mime="text/csv"
)

# ==================================================
# TABS
# ==================================================

tab1, tab2, tab3, tab4 = st.tabs([
    "📚 Academic Factors",
    "👨‍👩‍👧 Student & Family",
    "🎓 Education",
    "📈 Grade Relationships"
])

# ==================================================
# TAB 1 — ACADEMIC FACTORS
# ==================================================

with tab1:

    st.subheader("📚 Academic Factors")

    # --------------------------------------------------
    # Study Time + Previous Failures
    # --------------------------------------------------

    col1, col2 = st.columns(2)

    # --------------------------------------------------
    # Study Time vs Final Grade
    # --------------------------------------------------

    with col1:

        st.subheader("📚 Study Time vs Final Grade")

        study_time_analysis = (
            df.groupby("studytime")["G3"]
            .mean()
            .round(2)
        )

        study_time_analysis.index = (
            study_time_analysis.index.map({
                1: "<2 hours/week",
                2: "2–5 hours/week",
                3: "5–10 hours/week",
                4: ">10 hours/week"
            })
        )

        st.bar_chart(
            study_time_analysis
        )

    # --------------------------------------------------
    # Previous Failures vs Final Grade
    # --------------------------------------------------

    with col2:

        st.subheader("📉 Previous Failures vs Final Grade")

        previous_failures_analysis = (
            df.groupby("failures")["G3"]
            .mean()
            .round(2)
        )

        previous_failures_analysis.index = (
            previous_failures_analysis.index.map({
                0: "0 failures",
                1: "1 failure",
                2: "2 failures",
                3: "3 failures"
            })
        )

        st.bar_chart(
            previous_failures_analysis
        )

    # --------------------------------------------------
    # School Support
    # --------------------------------------------------

    st.subheader("🏫 School Support vs Final Grade")

    school_support_analysis = (
        df.groupby("schoolsup")["G3"]
        .mean()
        .round(2)
    )

    school_support_analysis.index = (
        school_support_analysis.index.map({
            "no": "No School Support",
            "yes": "School Support"
        })
    )

    st.bar_chart(
        school_support_analysis
    )

    # --------------------------------------------------
    # Average Grade by School
    # --------------------------------------------------

    st.subheader("🏫 Average Grade by School")

    school_analysis = (
        df.groupby("school")["G3"]
        .mean()
        .round(2)
    )

    school_analysis.index = (
        school_analysis.index.map({
            "GP": "Gabriel Pereira",
            "MS": "Mousinho da Silveira"
        })
    )

    st.bar_chart(
        school_analysis
    )

    # --------------------------------------------------
    # Study Time vs Previous Failures
    # --------------------------------------------------

    st.subheader("📚 Study Time vs Previous Failures")

    study_failure = (
        df.groupby("studytime")["failures"]
        .mean()
        .round(2)
    )

    study_failure.index = (
        study_failure.index.map({
            1: "<2 hours/week",
            2: "2–5 hours/week",
            3: "5–10 hours/week",
            4: ">10 hours/week"
        })
    )

    st.bar_chart(
        study_failure
    )

# ==================================================
# TAB 2 — STUDENT & FAMILY
# ==================================================

with tab2:

    st.subheader("👨‍👩‍👧 Student & Family")

    # --------------------------------------------------
    # Gender + Internet Access
    # --------------------------------------------------

    col1, col2 = st.columns(2)

    # --------------------------------------------------
    # Gender
    # --------------------------------------------------

    with col1:

        st.subheader("👩‍🎓 Gender vs Final Grade")

        gender_analysis = (
            df.groupby("sex")["G3"]
            .mean()
            .round(2)
        )

        gender_analysis.index = (
            gender_analysis.index.map({
                "F": "Female",
                "M": "Male"
            })
        )

        st.bar_chart(
            gender_analysis
        )

    # --------------------------------------------------
    # Internet Access
    # --------------------------------------------------

    with col2:

        st.subheader("🌐 Internet Access vs Final Grade")

        internet_analysis = (
            df.groupby("internet")["G3"]
            .mean()
            .round(2)
        )

        internet_analysis.index = (
            internet_analysis.index.map({
                "no": "No Internet",
                "yes": "Internet Access"
            })
        )

        st.bar_chart(
            internet_analysis
        )

    # --------------------------------------------------
    # Family Support
    # --------------------------------------------------

    st.subheader("👨‍👩‍👧‍👦 Family Support vs Final Grade")

    family_support_analysis = (
        df.groupby("famsup")["G3"]
        .mean()
        .round(2)
    )

    family_support_analysis.index = (
        family_support_analysis.index.map({
            "no": "No Family Support",
            "yes": "Family Support"
        })
    )

    st.bar_chart(
        family_support_analysis
    )

    # --------------------------------------------------
    # Age vs Final Grade
    # --------------------------------------------------

    st.subheader("📊 Age vs Final Grade")

    st.scatter_chart(
        df,
        x="age",
        y="G3"
    )

    # --------------------------------------------------
    # Grade Distribution by Gender
    # --------------------------------------------------

    st.subheader("👩‍🎓 Grade Distribution by Gender")

    gender_grade = (
        df.groupby(["sex", "G3"])
        .size()
        .unstack(fill_value=0)
    )

    gender_grade.index = (
        gender_grade.index.map({
            "F": "Female",
            "M": "Male"
        })
    )

    st.bar_chart(
        gender_grade
    )

# ==================================================
# TAB 3 — EDUCATION
# ==================================================

with tab3:

    st.subheader("🎓 Education")

    # --------------------------------------------------
    # Mother's Education + Father's Education
    # --------------------------------------------------

    col1, col2 = st.columns(2)

    # --------------------------------------------------
    # Mother's Education
    # --------------------------------------------------

    with col1:

        st.subheader(
            "👩 Mother's Education vs Final Grade"
        )

        mother_education_analysis = (
            df.groupby("Medu")["G3"]
            .mean()
            .round(2)
        )

        mother_education_analysis.index = (
            mother_education_analysis.index.map({
                0: "None",
                1: "Primary Education",
                2: "5th–9th Grade",
                3: "Secondary Education",
                4: "Higher Education"
            })
        )

        st.bar_chart(
            mother_education_analysis
        )

    # --------------------------------------------------
    # Father's Education
    # --------------------------------------------------

    with col2:

        st.subheader(
            "👨 Father's Education vs Final Grade"
        )

        father_education_analysis = (
            df.groupby("Fedu")["G3"]
            .mean()
            .round(2)
        )

        father_education_analysis.index = (
            father_education_analysis.index.map({
                0: "None",
                1: "Primary Education",
                2: "5th–9th Grade",
                3: "Secondary Education",
                4: "Higher Education"
            })
        )

        st.bar_chart(
            father_education_analysis
        )

    # --------------------------------------------------
    # Higher Education Intention
    # --------------------------------------------------

    st.subheader(
        "🎓 Higher Education Intention vs Final Grade"
    )

    higher_education_analysis = (
        df.groupby("higher")["G3"]
        .mean()
        .round(2)
    )

    higher_education_analysis.index = (
        higher_education_analysis.index.map({
            "no": "No",
            "yes": "Yes"
        })
    )

    st.bar_chart(
        higher_education_analysis
    )

# ==================================================
# TAB 4 — GRADE RELATIONSHIPS
# ==================================================

with tab4:

    st.subheader("📈 Grade Relationships")

    # --------------------------------------------------
    # G2 AND G3 CORRELATION
    # --------------------------------------------------

    g2_g3_correlation = (
        df["G2"].corr(df["G3"])
    )

    st.metric(
        "📈 G2–G3 Correlation",
        round(g2_g3_correlation, 2)
    )

    st.caption(
        "A value closer to 1 indicates a stronger positive relationship."
    )

    # --------------------------------------------------
    # Second Period Grade vs Final Grade
    # --------------------------------------------------

    st.subheader(
        "📈 Second Period Grade vs Final Grade"
    )

    col1, col2 = st.columns(2)

    with col1:

        st.scatter_chart(
            df,
            x="G2",
            y="G3"
        )

    with col2:

        st.write("### What this shows")

        st.write(
            "This chart compares students' second-period grades "
            "with their final grades. It helps identify whether "
            "students who performed well earlier also tended to "
            "perform well in the final grade."
        )

    # --------------------------------------------------
    # Absences vs Final Grade
    # --------------------------------------------------

    st.subheader(
        "📉 Absences vs Final Grade"
    )

    col1, col2 = st.columns(2)

    with col1:

        st.scatter_chart(
            df,
            x="absences",
            y="G3"
        )

    with col2:

        st.write("### What this shows")

        st.write(
            "This chart explores the relationship between "
            "student absences and final grades."
        )

    # --------------------------------------------------
    # CORRELATION HEATMAP
    # --------------------------------------------------

    st.subheader("🔥 Correlation Heatmap")

    correlation_columns = [
        "age",
        "studytime",
        "failures",
        "absences",
        "G1",
        "G2",
        "G3"
    ]

    correlation_matrix = df[
        correlation_columns
    ].corr()

    fig, ax = plt.subplots(
        figsize=(8, 6)
    )

    image = ax.imshow(
        correlation_matrix,
        cmap="coolwarm",
        vmin=-1,
        vmax=1
    )

    ax.set_xticks(
        range(len(correlation_columns))
    )

    ax.set_yticks(
        range(len(correlation_columns))
    )

    ax.set_xticklabels(
        correlation_columns
    )

    ax.set_yticklabels(
        correlation_columns
    )

    plt.colorbar(
        image,
        ax=ax
    )

    for i in range(
        len(correlation_columns)
    ):
        for j in range(
            len(correlation_columns)
        ):
            ax.text(
                j,
                i,
                f"{correlation_matrix.iloc[i, j]:.2f}",
                ha="center",
                va="center"
            )

    plt.xticks(
        rotation=45
    )

    plt.tight_layout()

    st.pyplot(fig)

    plt.close(fig)

    # --------------------------------------------------
    # PASS / FAIL ANALYSIS
    # --------------------------------------------------

    st.subheader("✅ Pass / Fail Analysis")

    pass_fail = df["G3"].apply(
        lambda grade: "Pass"
        if grade >= 10
        else "Fail"
    )

    pass_fail_counts = (
        pass_fail.value_counts()
    )

    st.bar_chart(
        pass_fail_counts
    )

    st.caption(
        "For this project, students with a final grade of 10 or above "
        "are classified as Pass."
    )

    # --------------------------------------------------
    # PASS RATE
    # --------------------------------------------------

    st.subheader("📊 Overall Pass Rate")

    pass_count = len(
        df[df["G3"] >= 10]
    )

    pass_rate = (
        pass_count / len(df)
    ) * 100

    st.metric(
        "✅ Pass Rate",
        f"{pass_rate:.2f}%"
    )