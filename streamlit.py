import streamlit as st

st.text("Hello World")

x = st.slider("x")
# This is a widget

st.write(x, "squared is", x * x)

name = st.text_input("What's your name?")

if name:
    st.write(f"Hello", {name})

else:
    st.text("Please enter your name")

select_contact = st.selectbox(
    "How would you like to be contacted?",
    ["Email", "Home", "Mobile phone"],
    index=None,
    placeholder="Select Contact Choice...",
)


if select_contact:
    st.write("Thank you")
else:
    st.write("Please select Contact")
