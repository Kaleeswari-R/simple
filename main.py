import streamlit as st

def add_numbers(num1, num2):
    return num1 + num2

# Creating a Streamlit app
st.title("Add Two Numbers")

# Input fields for the user to enter two numbers
num1 = st.number_input("Enter the first number:")
num2 = st.number_input("Enter the second number:")

# Button to perform the addition when clicked
if st.button("Add Numbers"):
    # Calling the add_numbers function and displaying the result
    result = add_numbers(num1, num2)
    st.write(f"The sum of {num1} and {num2} is: {result}")
