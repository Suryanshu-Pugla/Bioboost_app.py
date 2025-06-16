import streamlit as st

# Page 1: Welcome
st.set_page_config(page_title="BioBoost AI Prototype")
st.title("BioBoost AI")
st.subheader("Smarter Biogas Prediction Using AI")
st.markdown("Predict methane output using simple plant inputs – no sensors required.")

if st.button("Start Prediction"):
    st.session_state.page = "input"

# Page 2: Input Form
if st.session_state.get("page") == "input":
    st.header("Enter Your Plant Data")
    feedstock = st.selectbox("Feedstock Type", ["Cow dung", "Food waste", "Sludge", "Poultry litter"])
    volume = st.number_input("Daily Input Volume (kg)", min_value=1.0)
    solids = st.slider("Total Solids (%)", 5.0, 20.0, 10.0)
    temp = st.number_input("Digester Temperature (°C)", min_value=10.0, max_value=70.0, value=35.0)
    time = st.number_input("Retention Time (days)", min_value=5, max_value=60, value=30)

    if st.button("Predict Biogas Yield"):
        # Store values and go to result page
        st.session_state.inputs = {"feedstock": feedstock, "volume": volume, "solids": solids, "temp": temp, "time": time}
        st.session_state.page = "output"

# Page 3: Result Screen
if st.session_state.get("page") == "output":
    st.header("Prediction Result")
    inputs = st.session_state.get("inputs", {})

    # Fake prediction logic
    yield_estimate = round(inputs.get("volume", 1) * 0.045, 2)
    energy_output = round(yield_estimate * 4.13, 2)
    savings = round(energy_output * 0.18, 2)

    st.metric("Predicted Methane Yield", f"{yield_estimate} m³/day")
    st.metric("Expected Energy Output", f"{energy_output} kWh/day")
    st.metric("Estimated Cost Saving", f"${savings}/day")

    st.line_chart({"Day": list(range(1, 8)), "Yield (m³)": [yield_estimate + i*0.1 for i in range(7)]})

    st.button("Download Report (PDF)")
    st.button("Back to Start", on_click=lambda: st.session_state.clear())
