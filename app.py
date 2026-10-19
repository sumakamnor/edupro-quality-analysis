
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="EduPro - Quality Analysis", layout="wide")
st.title("📚 EduPro Online - Instructor & Course Quality Analysis")
st.markdown("Internship Project by Suma - Codomax Digital")

uploaded = st.file_uploader("Upload EduPro Excel", type=["xlsx"])
if uploaded:
    xls = pd.ExcelFile(uploaded)
    teachers = pd.read_excel(xls, 'Teachers')
    courses = pd.read_excel(xls, 'Courses')
    trans = pd.read_excel(xls, 'Transactions')
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Teachers", len(teachers))
    col2.metric("Total Courses", len(courses))
    col3.metric("Avg Rating", round(teachers['TeacherRating'].mean(),2))

    st.subheader("🏆 Top 10 Best Teachers")
    st.dataframe(teachers.sort_values('TeacherRating', ascending=False).head(10))

    st.subheader("📈 Experience vs Rating")
    fig1 = px.scatter(teachers, x='YearsOfExperience', y='TeacherRating', color='Expertise', hover_data=['TeacherName'])
    st.plotly_chart(fig1, use_container_width=True)

    st.subheader("📊 Course Category vs Rating")
    fig2 = px.bar(courses.groupby('CourseCategory')['CourseRating'].mean().reset_index(), 
                  x='CourseCategory', y='CourseRating')
    st.plotly_chart(fig2, use_container_width=True)

    st.subheader("📋 Key Insights")
    st.write("1. Experience vs Rating weak correlation - Quality depends on method")
    st.write("2. Best Category:", courses.groupby('CourseCategory')['CourseRating'].mean().idxmax())
