import streamlit as st

st.title("🏗️ Project Cost Predictor")
st.write("Input your project details below to see the estimate.")

# Layout with two columns
col1, col2 = st.columns(2)

with col1:
    area = st.number_input("Total Area (sqft)", min_value=0, value=1500)
    
with col2:
    material_quality = st.select_slider(
        'Select Material Quality',
        options=['Economy', 'Standard', 'Luxury']
    )

# Logic based on selection
rates = {"Economy": 150, "Standard": 250, "Luxury": 500}
current_rate = rates[material_quality]

estimate = area * current_rate

st.divider()
st.metric(label="Estimated Budget", value=f"${estimate:,}")
