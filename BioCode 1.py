import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# App Config
st.set_page_config(page_title="BioBoost AI", layout="wide")

# Logo and Branding
col1, col2 = st.columns([1, 8])
with col1:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Green_energy_icon.svg/2048px-Green_energy_icon.svg.png", width=60)
with col2:
    st.markdown("<h2 style='color:#2c6e49;'>BioBoost AI Dashboard</h2>", unsafe_allow_html=True)

# Simulated login (very basic)
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.subheader("User Login")
    user = st.text_input("Username")
    pw = st.text_input("Password", type="password")
    if st.button("Login"):
        if user == "abc" and pw == "abc":
            st.session_state.authenticated = True
            st.experimental_rerun()
        else:
            st.error("Invalid credentials. Try 'abc' / 'abc'.")
    st.stop()

# Navigation tabs
tab = st.selectbox("Navigate to section:", [
    "Data Input", "Descriptive Analytics", "Predictive Analytics", "Prescriptive Analytics", "Help"])

# Data Input Tab
if tab == "Data Input":
    st.subheader("Input Feedstock and Conditions")
    st.write("Upload daily feedstock data or enter manually below.")

    uploaded = st.file_uploader("Upload CSV file", type=["csv"])
    if uploaded:
        df = pd.read_csv(uploaded)
        st.dataframe(df)
    else:
        cow = st.number_input("Cow Manure (kg)", 0)
        food = st.number_input("Food Waste (kg)", 0)
        residue = st.number_input("Agri Residue (kg)", 0)
        temp = st.number_input("Ambient Temperature (°C)", 0.0)
        humid = st.number_input("Humidity (%)", 0.0)

# Descriptive Analytics
elif tab == "Descriptive Analytics":
    st.subheader("Descriptive Analytics")
    st.markdown("Key Metrics for Biogas Plant")
    kpi1, kpi2, kpi3 = st.columns(3)
    kpi1.metric("Avg Daily Output", "102 m³")
    kpi2.metric("Avg Methane %", "65%")
    kpi3.metric("Digestate Produced", "130 kg")

    st.write("Biogas Trends Over Time")
    data = pd.DataFrame({
        'Day': list(range(1, 11)),
        'Biogas Output (m3)': np.random.randint(90, 120, 10)
    })
    fig = px.line(data, x='Day', y='Biogas Output (m3)', title="Daily Biogas Production")
    st.plotly_chart(fig, use_container_width=True)

# Predictive Analytics
elif tab == "Predictive Analytics":
    st.subheader("Predict Biogas Output")
    cow = st.slider("Cow Manure (kg)", 0, 100, 50)
    food = st.slider("Food Waste (kg)", 0, 100, 30)
    residue = st.slider("Agri Residue (kg)", 0, 100, 20)
    temp = st.slider("Ambient Temp (°C)", 10, 40, 25)
    humid = st.slider("Humidity (%)", 20, 90, 60)

    predicted = 0.03*cow + 0.06*food + 0.02*residue + 0.1*(temp-25) - 0.05*(humid-60)
    st.metric("Predicted Biogas Yield (m³)", f"{max(predicted, 0):.2f}")

# Prescriptive Analytics
elif tab == "Prescriptive Analytics":
    st.subheader("Recommendations")
    st.markdown("Use the following blend for optimal output:")
    st.success("50% Cow Manure, 30% Food Waste, 20% Agri Residue")
    pie_data = pd.DataFrame({"Feedstock": ["Cow Manure", "Food Waste", "Agri Residue"],
                             "Proportion": [50, 30, 20]})
    fig = px.pie(pie_data, names='Feedstock', values='Proportion', title="Optimal Mix")
    st.plotly_chart(fig)

# Help Tab
elif tab == "Help":
    st.subheader("How to Use BioBoost AI")
    st.markdown("""
    - **Data Input**: Enter or upload feedstock and environmental conditions
    - **Descriptive Analytics**: View key historical trends and KPIs
    - **Predictive Analytics**: Adjust inputs to simulate biogas output
    - **Prescriptive Analytics**: See ideal ratios and system recommendations
    """)
