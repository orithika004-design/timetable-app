pip install streamlit pandas datetime
import streamlit as st
import pandas as pd
from datetime import datetime

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(
    page_title="Term 6 Timetable",
    layout="wide"
)

st.title("📚 Term 6 Timetable Viewer")

# -------------------------------
# TIMETABLE DATA
# -------------------------------
data = [
    # Week 1
    [1, "Tuesday", "09:00–10:30", "Film & Firm-A", "Prof. Vikas Pathe"],
    [1, "Tuesday", "10:45–12:15", "Film & Firm-A", "Prof. Vikas Pathe"],

    # Week 2
    [2, "Monday", "09:00–10:30", "BEDM-B", "Prof. Amarendu Nandy"],
    [2, "Monday", "10:45–12:15", "BEDM-B", "Prof. Amarendu Nandy"],
    [2, "Wednesday", "03:00–04:30", "SA-A", "Prof. R Vivekananda"],
    [2, "Wednesday", "04:45–06:15", "SA-A", "Prof. R Vivekananda"],

    # Week 3
    [3, "Tuesday", "09:00–10:30", "BEDM-B", "Prof. Amarendu Nandy"],
    [3, "Wednesday", "12:30–02:00", "Film & Firm-A", "Prof. Manish Kumar"],

    # Week 4
    [4, "Thursday", "03:00–04:30", "SA-A", "Prof. R Vivekananda"],
    [4, "Thursday", "04:45–06:15", "Film & Firm-A", "Prof. Ambuj Anand"],

    # Week 5
    [5, "Monday", "09:00–10:30", "BEDM-B", "Prof. Amarendu Nandy"],
    [5, "Tuesday", "12:30–02:00", "Film & Firm-A", "Prof. George Joseph"],

    # Week 6
    [6, "Wednesday", "10:45–12:15", "SA-A", "Prof. R Vivekananda"],

    # Week 7
    [7, "Friday", "03:00–04:30", "BEDM-B", "Prof. Tanusree Dutta"],

    # Week 8
    [8, "Monday", "09:00–10:30", "SA-A", "Prof. Ambuj Anand"]
]

columns = ["Week", "Day", "Time Slot", "Course", "Faculty"]
df = pd.DataFrame(data, columns=columns)

# -------------------------------
# SIDEBAR FILTERS
# -------------------------------
st.sidebar.header("🔍 Filters")

selected_week = st.sidebar.selectbox(
    "Select Week",
    ["All"] + sorted(df["Week"].unique().tolist())
)

selected_course = st.sidebar.multiselect(
    "Select Course",
    df["Course"].unique(),
    default=df["Course"].unique()
)

# -------------------------------
# FILTER LOGIC
# -------------------------------
filtered_df = df.copy()

if selected_week != "All":
    filtered_df = filtered_df[filtered_df["Week"] == selected_week]

filtered_df = filtered_df[filtered_df["Course"].isin(selected_course)]

# -------------------------------
# TODAY VIEW
# -------------------------------
st.subheader("📅 Today’s Classes")

today = datetime.today().strftime("%A")
today_df = filtered_df[filtered_df["Day"] == today]

if today_df.empty:
    st.info("No classes scheduled for today 🎉")
else:
    st.dataframe(today_df, use_container_width=True)

# -------------------------------
# FULL TIMETABLE VIEW
# -------------------------------
st.subheader("🗓 Full Timetable")

st.dataframe(
    filtered_df.sort_values(by=["Week", "Day", "Time Slot"]),
    use_container_width=True
)

# -------------------------------
# FOOTER
# -------------------------------
st.markdown("---")
st.caption("Built using Python & Streamlit | Term 6 Timetable App")
