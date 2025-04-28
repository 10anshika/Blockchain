import streamlit as st

# Initialize an empty ledger list
hospital_ledger = []

# Function to add a patient's visit to the ledger
def add_patient_visit(patient_name, treatment, cost):
    visit = {
        "patient_name": patient_name,
        "treatment": treatment,
        "cost": cost
    }
    hospital_ledger.append(visit)
    st.success(f"Visit added for {patient_name} with treatment {treatment} costing {cost}.")

# Streamlit App
st.title("🏥 Hospital Patient Visit Ledger")

st.header("Add a New Patient Visit")

# Input fields
patient_name = st.text_input("Patient Name")
treatment = st.text_input("Treatment")
cost = st.number_input("Cost", min_value=0)

# Button to add visit
if st.button("Add Visit"):
    if patient_name and treatment and cost >= 0:
        add_patient_visit(patient_name, treatment, cost)
    else:
        st.error("Please fill all fields correctly!")

# Display the hospital ledger
st.header("Hospital Ledger")
if hospital_ledger:
    for visit in hospital_ledger:
        st.write(visit)
else:
    st.info("No patient visits added yet.")
