import streamlit as st

st.set_page_config(page_title="Employee Salary Estimator", page_icon="💼")
st.title("💼 Employee Salary Estimator")
st.markdown("Estimate your expected salary based on your profile details.")

# Sidebar Inputs
st.sidebar.header("Enter Employee Details")

experience = st.sidebar.slider("Years of Experience", 0, 30, 2)
education = st.sidebar.selectbox("Highest Education Level", ["High School", "Bachelors", "Masters", "PhD"])
role = st.sidebar.selectbox("Job Role", ["Intern", "Analyst", "Engineer", "Senior Engineer", "Manager", "Director"])
location = st.sidebar.selectbox("Work Location", ["Hyderabad", "Bangalore", "Chennai", "Mumbai", "Delhi", "Pune"])
skills = st.sidebar.multiselect("Skills / Certifications", ["Python", "SQL", "Excel", "Machine Learning", "Cloud", "Communication", "MBA"])
hours_per_week = st.sidebar.slider("Average Weekly Working Hours", 20, 60, 40)

# Base Salary Logic
base_salary = 20000
experience_bonus = experience * 2500

edu_bonus = {
    "High School": 0,
    "Bachelors": 5000,
    "Masters": 10000,
    "PhD": 20000
}[education]

role_bonus = {
    "Intern": 5000,
    "Analyst": 10000,
    "Engineer": 15000,
    "Senior Engineer": 20000,
    "Manager": 25000,
    "Director": 40000
}[role]

location_bonus = {
    "Hyderabad": 4000,
    "Bangalore": 9000,
    "Chennai": 5000,
    "Mumbai": 8000,
    "Delhi": 6000,
    "Pune": 5500
}[location]

# Skill Bonus
skill_bonus = len(skills) * 3000

# Working Hours Adjustment
hours_bonus = (hours_per_week - 40) * 300 if hours_per_week > 40 else 0

# Total Predicted Salary
predicted_salary = base_salary + experience_bonus + edu_bonus + role_bonus + location_bonus + skill_bonus + hours_bonus

# Output
if st.button("💰 Predict Salary"):
    st.success(f"Estimated Salary: ₹ {predicted_salary:,}")
    st.markdown("📊 **Breakdown**")
    st.write(f"- Base Salary: ₹{base_salary:,}")
    st.write(f"- Experience Bonus: ₹{experience_bonus:,}")
    st.write(f"- Education Bonus: ₹{edu_bonus:,}")
    st.write(f"- Role Bonus: ₹{role_bonus:,}")
    st.write(f"- Location Bonus: ₹{location_bonus:,}")
    st.write(f"- Skills Bonus: ₹{skill_bonus:,}")
    if hours_bonus > 0:
        st.write(f"- Overtime Bonus: ₹{hours_bonus:,}")
