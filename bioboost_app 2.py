
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Apply custom styles
st.markdown("""
    <style>
        body, .main, .block-container {
            background-color: #fffde7;
        }
        h1, h2, h3, h4, h5, h6, p, div, label {
            font-size: 18px !important;
            font-weight: 600 !important;
        }
        .css-10trblm, .stTextInput > label, .stSelectbox > label {
            color: #2e7d32 !important;
        }
        .css-1cpxqw2, .stRadio > label {
            color: #0d47a1 !important;
        }
        .sidebar .css-1aumxhk {
            background-color: #fffde7;
        }
    </style>
""", unsafe_allow_html=True)

# Logo and Navigation
st.sidebar.image("logo.png", width=100)
tab = st.sidebar.radio("📂 Sections", [
    "Data Input",
    "Descriptive Analytics",
    "Predictive Analytics",
    "Prescriptive Analytics",
    "Help"
])

# Simple Login Page
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

# Tabs Content
if tab == "Data Input":
    st.header("Data Input")
    st.write("Upload daily data or input manually:")
    uploaded_file = st.file_uploader("Upload CSV", type="csv")
    if uploaded_file:
        data = pd.read_csv(uploaded_file)
        st.dataframe(data)
    temp = st.number_input("Temperature (°C)", value=30)
    humidity = st.number_input("Humidity (%)", value=50)

elif tab == "Descriptive Analytics":
    st.header("Descriptive Analytics")
    st.write("Visualizations of historical plant performance.")
    dummy_data = pd.DataFrame({
        "Date": pd.date_range("2024-01-01", periods=10),
        "Biogas Output (m3)": np.random.randint(80, 120, size=10)
    })
    fig = px.line(dummy_data, x="Date", y="Biogas Output (m3)", title="Biogas Output Over Time")
    st.plotly_chart(fig)

elif tab == "Predictive Analytics":
    st.header("Predictive Analytics")
    st.write("Adjust input values to see predicted biogas output.")
    feedstock = st.slider("Feedstock Quantity (kg)", 50, 500, 150)
    temp = st.slider("Temperature (°C)", 20, 60, 35)
    pred_output = 0.25 * feedstock + 0.5 * temp  # Mock formula
    st.metric("Predicted Biogas Output (m3)", round(pred_output, 2))

elif tab == "Prescriptive Analytics":
    st.header("Prescriptive Analytics")
    st.write("Recommendations based on input and predicted output.")
    if 'pred_output' in locals():
        if pred_output < 100:
            st.warning("Increase feedstock or optimize temperature for better yield.")
        else:
            st.success("Your plant is operating near optimal efficiency.")

elif tab == "Help":
    st.header("User Help")
    st.write("Use the left menu to navigate between tabs. Input daily data in the Data Input tab. Use Predictive and Prescriptive tabs for insights.")
