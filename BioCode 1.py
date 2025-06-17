import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# App Config
st.set_page_config(page_title="BioBoost AI", layout="wide")

# Logo and Header
col1, col2 = st.columns([1, 8])
with col1:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Green_energy_icon.svg/2048px-Green_energy_icon.svg.png", width=60)
with col2:
    st.markdown("<h2 style='color:#2c6e49;'>BioBoost AI Dashboard</h2>", unsafe_allow_html=True)


# Initialize session state
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'login_attempted' not in st.session_state:
    st.session_state.login_attempted = False

if not st.session_state.authenticated:
    st.title("BioBoost AI Login")
    user = st.text_input("Username", key="user_input")
    pw = st.text_input("Password", type="password", key="pw_input")
    login = st.button("Login")

    if login:
        if user == "abc" and pw == "abc":
            st.session_state.authenticated = True
        else:
            st.session_state.login_attempted = True

    if st.session_state.login_attempted and not st.session_state.authenticated:
        st.error("Invalid credentials. Try username: abc, password: abc")
    st.stop()




# Tabs
tab = st.selectbox("Navigate to section:", [
    "Data Input", "Descriptive Analytics", "Predictive Analytics", "Prescriptive Analytics", "Help"])

# Data Input
if tab == "Data Input":
    st.subheader("Input Feedstock and Conditions")
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
    kpi1, kpi2, kpi3 = st.columns(3)
    kpi1.metric("Avg Daily Output", "102 m³")
    kpi2.metric("Avg Methane %", "65%")
    kpi3.metric("Digestate Produced", "130 kg")
    data = pd.DataFrame({'Day': list(range(1, 11)), 'Biogas Output (m3)': np.random.randint(90, 120, 10)})
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
    st.subheader("Prescriptive Recommendations")
    st.success("Use this optimal blend: 50% Cow Manure, 30% Food Waste, 20% Agri Residue")
    pie_data = pd.DataFrame({"Feedstock": ["Cow Manure", "Food Waste", "Agri Residue"], "Proportion": [50, 30, 20]})
    fig = px.pie(pie_data, names='Feedstock', values='Proportion', title="Optimal Feedstock Mix")
    st.plotly_chart(fig)

# Help
elif tab == "Help":
    st.subheader("How to Use BioBoost AI")
    st.markdown("""
    - **Data Input**: Upload or enter feedstock + weather data
    - **Descriptive**: View plant KPIs and performance charts
    - **Predictive**: Simulate output by adjusting inputs
    - **Prescriptive**: Get smart feedstock recommendations
    """)
