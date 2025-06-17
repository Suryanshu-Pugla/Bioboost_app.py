import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="BioBoost AI", layout="wide")

# Sidebar Navigation
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Green_energy_icon.svg/2048px-Green_energy_icon.svg.png", width=80)
tab = st.sidebar.radio("Navigate", [
    "User Login", "Data Input", "Descriptive Analytics",
    "Predictive Analytics", "Prescriptive Analytics", "Help"])

# User Login Tab
if tab == "User Login":
    st.title("Welcome to BioBoost AI")
    st.subheader("Fueling Biogas Intelligence")
    login_method = st.selectbox("Choose login method", ["Email", "Google", "Facebook"])
    st.text_input("Username")
    st.text_input("Password", type="password")
    st.button("Login")

# Data Input Tab
elif tab == "Data Input":
    st.title("Input Feedstock Data")
    st.write("Upload daily feedstock data or input manually.")

    uploaded = st.file_uploader("Upload CSV file", type=["csv"])
    if uploaded:
        df = pd.read_csv(uploaded)
        st.dataframe(df)
    else:
        st.write("Or enter data manually:")
        manure = st.number_input("Cow Manure (kg)", min_value=0)
        food_waste = st.number_input("Food Waste (kg)", min_value=0)
        agri_residue = st.number_input("Agri Residue (kg)", min_value=0)

# Descriptive Analytics Tab
elif tab == "Descriptive Analytics":
    st.title("Plant Performance Overview")
    st.subheader("Key Metrics and Visualizations")
    st.write("Sample historical performance:")
    # Mock data
    sample_data = pd.DataFrame({
        'Day': list(range(1, 11)),
        'Biogas (m3)': np.random.randint(80, 120, size=10),
        'Methane (%)': np.random.uniform(50, 70, size=10)
    })
    st.line_chart(sample_data.set_index('Day'))

# Predictive Analytics Tab
elif tab == "Predictive Analytics":
    st.title("Biogas Output Prediction")
    st.subheader("Simulate your feedstock mix")
    
    cow = st.slider("Cow Manure (kg)", 0, 100, 50)
    food = st.slider("Food Waste (kg)", 0, 100, 30)
    residue = st.slider("Agri Residue (kg)", 0, 100, 20)
    
    predicted_yield = 0.03*cow + 0.06*food + 0.02*residue
    st.metric("Predicted Biogas Yield (m³)", f"{predicted_yield:.2f}")

# Prescriptive Analytics Tab
elif tab == "Prescriptive Analytics":
    st.title("Recommendations")
    st.subheader("Based on your current inputs")
    st.write("Suggested mix for optimal biogas output:")
    st.markdown("- Cow Manure: 50%\n- Food Waste: 30%\n- Agri Residue: 20%")
    st.success("Follow this mix to maximize methane production and system stability.")

# Help Tab
elif tab == "Help":
    st.title("Help & Navigation Guide")
    st.markdown("""
        **Tabs Overview:**
        - **Login:** Sign in to access features
        - **Data Input:** Upload or manually enter feedstock data
        - **Descriptive Analytics:** View historical performance
        - **Predictive Analytics:** Simulate future output
        - **Prescriptive Analytics:** Get optimization recommendations
    """)



