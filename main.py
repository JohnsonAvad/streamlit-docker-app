import streamlit as st

st.markdown(
    """
<style>

.stApp{

       background-color: black;

       color: white



}

    
</style>

""",
    unsafe_allow_html=True,
)















project_title = st.title("Basic Salary Loan Calculator")

# Initialization

if "result" not in st.session_state:
    st.session_state.result = None


principal = st.number_input(
    "Enter principal amount", min_value=300000, max_value=10000000
)

months_number = st.number_input(
    "Enter no. of months", min_value=3, max_value=72, value=3
)

monthly_interest_rate = st.number_input(
    "Enter monthly interest rate(%)", min_value=0.0, max_value=10.0, value=1.0
)

total_interest = (monthly_interest_rate / 100) * months_number * principal

total_amount = principal + total_interest

monthly_rate = total_amount / months_number

# Calculate button
if st.button("Calculate"):
    total_interest = (monthly_rate / 100) * months_number * principal
    total_amount = principal + total_interest
    monthly_payment = total_amount / months_number

    st.session_state.result = {
        "total_amount": total_amount,
        "monthly_payment": monthly_payment

    }    

if st.session_state.result:

    st.subheader("Loan Calculation Results")
    st.write(f"Total Amount: UGX {st.session_state.result['total_amount']:,.2f}")
    st.write(f"Monthly Payment: UGX {st.session_state.result['monthly_payment']:,.2f}")        



