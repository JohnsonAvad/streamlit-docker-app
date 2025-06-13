import streamlit as st  # For our web interface
import requests  # For talking to the backend
import pandas as pd  # For working with the loan history as a DataFrame

# Where to find our backend
BACKEND_URL = "http://localhost:8000"

# Page styles

st.markdown("""
<style>
/* Overall App Styling */
.stApp {
    background-color: #121212;  
    color: #e0e0e0;
    font-family: 'Segoe UI', 'Roboto', sans-serif;  /* Clean and readable */
}

/* Input fields */
input[type="text"], input[type="number"] {
    background-color: #264653;   
    color: #f4f1de;             
    border: 2px solid #2a9d8f;  
    border-radius: 8px;
    padding: 8px 12px;
    font-weight: 600;
    font-size: 16px;
}

/* Labels */
label, [data-baseweb="label"] {
    color: #fcbf49;  /* Golden yellow for contrast */
    font-weight: bold;
    font-size: 18px;
    margin-bottom: 6px;
}
</style>
""", unsafe_allow_html=True)



st.title("Basic Salary Loan Calculator")

# Input fields
applicant_name = st.text_input("Enter applicant's name")    
principal = st.number_input("Loan amount", 300000, 10000000)
months_number = st.number_input("Months", 3, 72, 3)
monthly_interest_rate = st.number_input("Interest rate %", 0.0, 10.0, 1.0)

# Calculate button
if st.button("Calculate"):
    try:
        response = requests.post(
            f"{BACKEND_URL}/calculate/",
            params={
                "applicant_name": applicant_name,
                "principal": principal,
                "months_number": months_number,
                "monthly_interest_rate": monthly_interest_rate
            }
        )
        result = response.json()
        st.subheader("Loan Results")
        st.write(f"Total Amount: UGX {result['total_amount']:,.2f}")
        st.write(f"Monthly Payment: UGX {result['monthly_payment']:,.2f}")
    except requests.exceptions.RequestException as e:
        st.error(f"Error: {str(e)}")

# Show loan history with download option
try:
    records = requests.get(f"{BACKEND_URL}/records/").json()
    if records:
        st.subheader("Loan History")

        # Convert to DataFrame
        df = pd.DataFrame(records)

        # Show styled table
        st.dataframe(df.style.set_properties(**{
            'background-color': '#264653',
            'color': '#f4f1de',
            'border-color': '#2a9d8f'
        }))

        # Download button
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Loan History as CSV",
            data=csv,
            file_name="loan_history.csv",
            mime="text/csv"
        )
except requests.exceptions.RequestException:
    st.warning("Could not load history")
