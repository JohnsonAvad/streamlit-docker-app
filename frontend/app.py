import streamlit as st  # For our web interface
import requests  # For talking to the backend

# Where to find our backend (matches Docker service name)
BACKEND_URL = "http://localhost:8000"

# Make the page black with white text
st.markdown("""<style>.stApp {background-color: black; color: white}</style>""", 
            unsafe_allow_html=True)

st.title("Basic Salary Loan Calculator")  # Page title

# Input fields
applicant_name = st.text_input("Enter applicant's name")    
principal = st.number_input("Loan amount", 300000, 10000000)
months_number = st.number_input("Months", 3, 72, 3)
monthly_interest_rate = st.number_input("Interest rate %", 0.0, 10.0, 1.0)

if st.button("Calculate"):  # When button is clicked
    try:
        # Send data to backend
        response = requests.post(
            f"{BACKEND_URL}/calculate/",
            params={
                "applicant_name": applicant_name,
                "principal": principal,
                "months_number": months_number,
                "monthly_interest_rate": monthly_interest_rate
            }
        )
        result = response.json()  # Get the response
        # Show results
        st.subheader("Loan Results")
        st.write(f"Total Amount: UGX {result['total_amount']:,.2f}")
        st.write(f"Monthly Payment: UGX {result['monthly_payment']:,.2f}")
    except requests.exceptions.RequestException as e:
        st.error(f"Error: {str(e)}")  # Show errors

# Show loan history
try:
    records = requests.get(f"{BACKEND_URL}/records/").json()
    if records:
        st.subheader("Loan History")
        st.table(records)  # Display as nice table
except requests.exceptions.RequestException:
    st.warning("Could not load history")  # Show warning if fails